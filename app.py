"""
Flood Detection Web Application
================================
This Flask application provides a web interface for detecting flooded areas
in satellite images using a pre-trained Convolutional Neural Network (CNN).

Architecture Overview:
- Frontend: HTML/JavaScript interface for image upload
- Backend: Flask server handling image preprocessing and predictions
- Model: Pre-trained CNN model for binary classification

Author: Samarth Patil
Repository: Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images
"""

# Import required libraries
from flask import Flask, request, jsonify, render_template  # Web framework
import tensorflow as tf  # Deep learning framework for model inference
import numpy as np  # Numerical operations for array manipulation
import cv2  # OpenCV for image processing
import os  # Operating system operations for file handling

# Initialize Flask application
app = Flask(__name__)

# ========================
# MODEL INITIALIZATION
# ========================

# Path to the pre-trained model file (~57MB)
# This model was trained on satellite images to classify flooded vs non-flooded areas
MODEL_PATH = "model/flood_detection_trained_model.h5"

# Load the trained Keras model
# The model expects input shape: (batch_size, 128, 128, 3)
# Output: Binary classification (0=Non-Flooded, 1=Flooded)
model = tf.keras.models.load_model(MODEL_PATH)

print("✅ Model loaded successfully!")
print(f"Model input shape: {model.input_shape}")
print(f"Model output shape: {model.output_shape}")

# ========================
# IMAGE PREPROCESSING
# ========================

def preprocess_image(image_path):
    """
    Loads and preprocesses an image for model prediction.
    
    The preprocessing pipeline ensures the image is in the correct format
    for the CNN model, which expects normalized RGB images of size 128x128.
    
    Args:
        image_path (str): Path to the uploaded image file
        
    Returns:
        numpy.ndarray: Preprocessed image with shape (1, 128, 128, 3)
                      Values normalized to range [0, 1]
                      
    Pipeline:
        1. Load image from disk using OpenCV
        2. Convert color space from BGR (OpenCV default) to RGB
        3. Resize to 128x128 pixels (model's expected input size)
        4. Normalize pixel values from [0, 255] to [0, 1]
        5. Add batch dimension for model compatibility
    """
    # Step 1: Read the image file
    # cv2.IMREAD_UNCHANGED preserves the original image format
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Step 2: Convert color space from BGR to RGB
    # OpenCV loads images in BGR format, but our model expects RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Step 3: Resize image to match model's expected input dimensions
    # The model was trained on 128x128 images
    img = cv2.resize(img, (128, 128))
    
    # Step 4: Normalize pixel values to [0, 1] range
    # Neural networks perform better with normalized inputs
    img = img / 255.0
    
    # Step 5: Add batch dimension
    # Model expects shape (batch_size, height, width, channels)
    # np.expand_dims converts (128, 128, 3) to (1, 128, 128, 3)
    img = np.expand_dims(img, axis=0)
    
    return img


# ========================
# ROUTE HANDLERS
# ========================

@app.route('/')
def home():
    """
    Home page route - serves the main web interface.
    
    Returns:
        HTML: The index.html template with the image upload form
              and prediction interface
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint - processes uploaded image and returns classification result.
    
    This endpoint:
    1. Validates the uploaded file
    2. Saves the file temporarily
    3. Preprocesses the image for model input
    4. Runs the CNN model prediction
    5. Interprets the results
    6. Returns JSON response with prediction and confidence
    
    Expected POST data:
        - 'image': Image file (multipart/form-data)
        
    Returns:
        JSON response containing:
        - prediction: "Flooded Area" or "Non-Flooded Area"
        - probability: Confidence score (0-1)
        - status: "success" or "failure"
        
    Example success response:
        {
            "prediction": "Flooded Area",
            "probability": 0.876,
            "status": "success"
        }
        
    Example error response:
        {
            "error": "Error message",
            "status": "failure"
        }
    """
    try:
        # ========================
        # STEP 1: VALIDATE INPUT
        # ========================
        # Check if an image file was included in the request
        if 'image' not in request.files:
            return jsonify({
                'error': 'No image uploaded. Please select an image file.',
                'status': 'failure'
            })

        # Get the uploaded file object
        file = request.files['image']
        
        # Check if a file was actually selected
        if file.filename == '':
            return jsonify({
                'error': 'No file selected. Please choose an image.',
                'status': 'failure'
            })

        # ========================
        # STEP 2: SAVE TEMP FILE
        # ========================
        # Save the uploaded image temporarily for processing
        # In production, consider using secure_filename() from werkzeug.utils
        image_path = "temp_image.jpg"
        file.save(image_path)
        print(f"📁 Image saved temporarily at: {image_path}")

        # ========================
        # STEP 3: PREPROCESS IMAGE
        # ========================
        # Convert the image to the format expected by the model
        # Output: (1, 128, 128, 3) normalized array
        preprocessed_image = preprocess_image(image_path)
        print(f"🔄 Image preprocessed. Shape: {preprocessed_image.shape}")

        # ========================
        # STEP 4: RUN MODEL PREDICTION
        # ========================
        # Pass the preprocessed image through the CNN model
        # The model outputs a probability or class scores
        predictions = model.predict(preprocessed_image)
        print(f"🤖 Raw model predictions: {predictions}")

        # ========================
        # STEP 5: INTERPRET RESULTS
        # ========================
        # Handle different output formats (sigmoid vs softmax)
        
        if predictions.shape[-1] == 1:
            # Binary classification with sigmoid activation
            # Output shape: (1, 1)
            # Single probability value: P(Flooded)
            probability = float(predictions[0][0])
            
            # Apply threshold: >= 0.5 is Flooded, < 0.5 is Non-Flooded
            prediction = "Flooded Area" if probability >= 0.5 else "Non-Flooded Area"
            
        else:
            # Multi-class classification with softmax activation
            # Output shape: (1, num_classes)
            # Multiple probability values, one per class
            probability = float(np.max(predictions))
            class_index = int(np.argmax(predictions))
            
            # Assuming class 1 = Flooded, class 0 = Non-Flooded
            prediction = "Flooded Area" if class_index == 1 else "Non-Flooded Area"

        print(f"✅ Prediction: {prediction} (Confidence: {probability:.3f})")

        # ========================
        # STEP 6: CLEANUP
        # ========================
        # Remove the temporary image file to save disk space
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"🗑️ Temporary file removed")

        # ========================
        # STEP 7: RETURN RESULT
        # ========================
        # Send JSON response back to the client
        return jsonify({
            'prediction': prediction,
            'probability': round(probability, 3),  # Round to 3 decimal places
            'status': 'success'
        })

    except Exception as e:
        # ========================
        # ERROR HANDLING
        # ========================
        # Catch any unexpected errors and return informative message
        error_message = str(e)
        print(f"❌ Error occurred: {error_message}")
        
        # Clean up temp file if it exists
        if os.path.exists("temp_image.jpg"):
            os.remove("temp_image.jpg")
        
        return jsonify({
            'error': f'Error processing image: {error_message}',
            'status': 'failure'
        })


# ========================
# APPLICATION STARTUP
# ========================

if __name__ == '__main__':
    """
    Main entry point for the Flask application.
    
    Configuration:
    - debug=True: Enables auto-reload on code changes and detailed error pages
                  Set to False in production!
    - host='0.0.0.0': Makes the app accessible from other machines on the network
                      (optional, default is localhost only)
    - port=5000: Default Flask port (can be changed if needed)
    
    To run the application:
        python app.py
        
    Then navigate to:
        http://localhost:5000 or http://127.0.0.1:5000
        
    For production deployment, use a WSGI server like Gunicorn:
        gunicorn -w 4 -b 0.0.0.0:8000 app:app
    """
    print("\n" + "="*60)
    print("🌊 FLOOD DETECTION APPLICATION")
    print("="*60)
    print("🚀 Starting Flask server...")
    print("📡 Access the application at: http://localhost:5000")
    print("⚠️  Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    # Start the Flask development server
    # WARNING: Do not use debug=True in production!
    app.run(debug=True)