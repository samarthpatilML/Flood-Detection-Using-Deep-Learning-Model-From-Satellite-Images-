from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)

# ✅ Load the trained model (make sure path exists)
MODEL_PATH = "model/flood_detection_trained_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# ✅ Preprocess the uploaded image
def preprocess_image(image_path):
    """
    Loads and preprocesses image for model prediction.
    """
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))  # adjust to match your model input
    img = img / 255.0  # normalize to [0,1]
    img = np.expand_dims(img, axis=0)  # add batch dimension
    return img


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Check if file is uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded', 'status': 'failure'})

        file = request.files['image']

        # ✅ Save temp file
        image_path = "temp_image.jpg"
        file.save(image_path)

        # ✅ Preprocess image
        preprocessed_image = preprocess_image(image_path)

        # ✅ Model prediction
        predictions = model.predict(preprocessed_image)
        print("Raw model predictions:", predictions)  # Debug line for console

        # ✅ Handle sigmoid or softmax outputs
        if predictions.shape[-1] == 1:
            # Binary classification (sigmoid output)
            probability = float(predictions[0][0])
            prediction = "Flooded Area" if probability >= 0.5 else "Non-Flooded Area"
        else:
            # Multi-class (softmax output)
            probability = float(np.max(predictions))
            class_index = int(np.argmax(predictions))
            prediction = "Flooded Area" if class_index == 1 else "Non-Flooded Area"

        # ✅ Clean up
        os.remove(image_path)

        # ✅ Return result
        return jsonify({
            'prediction': prediction,
            'probability': round(probability, 3),
            'status': 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failure'})


if __name__ == '__main__':
    app.run(debug=True)
# ✅ Run the app