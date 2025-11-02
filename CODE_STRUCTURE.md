# 📐 Code Structure and Architecture

## Overview

This document provides an in-depth explanation of the code architecture, data flow, and implementation details of the Flood Detection application.

## 🎯 Architecture Layers

### 1. Presentation Layer (Frontend)
**File**: `templates/index.html`

#### Components:
- **HTML Structure**: Form-based interface for image upload
- **CSS Styling**: Modern gradient design with responsive layout
- **JavaScript Functions**:
  - `previewImage()`: Displays uploaded image before prediction
  - `submitImage()`: Handles form submission via AJAX

#### Key Features:
```javascript
// Image preview functionality
function previewImage(event) {
    // Creates FileReader to read image file
    // Displays image in <img> element before prediction
}

// Async prediction request
function submitImage() {
    // Creates FormData with uploaded image
    // Sends POST request to /predict endpoint
    // Displays loading spinner during processing
    // Shows result or error message
}
```

### 2. Application Layer (Backend)
**File**: `app.py`

#### Route Handlers:

##### `GET /` - Home Route
```python
@app.route('/')
def home():
    # Serves the main HTML interface
    # Returns: templates/index.html
```

##### `POST /predict` - Prediction Route
```python
@app.route('/predict', methods=['POST'])
def predict():
    # 1. Validate uploaded file
    # 2. Save temporarily
    # 3. Preprocess image
    # 4. Run model prediction
    # 5. Format results
    # 6. Clean up temporary files
    # 7. Return JSON response
```

#### Helper Functions:

##### `preprocess_image(image_path)`
```python
def preprocess_image(image_path):
    """
    Image Preprocessing Pipeline:
    
    Input: Raw image file (any size, any format)
    Output: Normalized tensor (1, 128, 128, 3)
    
    Steps:
    1. cv2.imread() - Load image from disk
    2. cv2.cvtColor() - Convert BGR → RGB
    3. cv2.resize() - Resize to 128×128
    4. Normalize - Divide by 255 (scale to 0-1)
    5. np.expand_dims() - Add batch dimension
    """
```

### 3. Model Layer
**File**: `model/flood_detection_trained_model.h5`

#### Model Architecture:
```
Input Layer (128, 128, 3)
        ↓
Convolutional Layers (Feature Extraction)
        ↓
Pooling Layers (Dimensionality Reduction)
        ↓
Flatten Layer
        ↓
Dense Layers (Classification)
        ↓
Output Layer (Binary Classification)
```

#### Model Specifications:
- **Framework**: TensorFlow/Keras
- **Type**: Sequential CNN
- **Input Shape**: (None, 128, 128, 3)
- **Output**: Single neuron with sigmoid activation
- **Loss Function**: Binary Crossentropy (inferred)
- **Size**: ~57 MB

### 4. Data Layer
**Directory**: `FloodDataset/`

#### Dataset Organization:
```
FloodDataset/
├── test/
│   ├── damage/       # Positive class (flooded)
│   └── notdamage/    # Negative class (non-flooded)
├── test_another/
├── train_another/
└── validation_another/
```

## 🔄 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        USER INTERACTION                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  1. User uploads image via web interface (index.html)       │
│     • File selection dialog                                  │
│     • Image preview display                                  │
│     • Click "Predict" button                                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. JavaScript sends POST request to /predict endpoint       │
│     • FormData with image file                               │
│     • XMLHttpRequest (AJAX)                                  │
│     • Shows loading spinner                                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Flask receives and validates request (app.py)            │
│     • Check if 'image' in request.files                      │
│     • Validate file exists                                   │
│     • Save to temp_image.jpg                                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Image Preprocessing (preprocess_image function)          │
│     ┌────────────────────────────────────────────────────┐  │
│     │ a. Load: cv2.imread(temp_image.jpg)               │  │
│     │    → Raw image array (H, W, 3) in BGR             │  │
│     ├────────────────────────────────────────────────────┤  │
│     │ b. Convert: cv2.cvtColor(BGR → RGB)               │  │
│     │    → RGB image array (H, W, 3)                    │  │
│     ├────────────────────────────────────────────────────┤  │
│     │ c. Resize: cv2.resize(→ 128×128)                  │  │
│     │    → Standardized size (128, 128, 3)              │  │
│     ├────────────────────────────────────────────────────┤  │
│     │ d. Normalize: img / 255.0                         │  │
│     │    → Pixel values in range [0, 1]                 │  │
│     ├────────────────────────────────────────────────────┤  │
│     │ e. Batch: np.expand_dims(axis=0)                  │  │
│     │    → Model-ready tensor (1, 128, 128, 3)          │  │
│     └────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Model Prediction (TensorFlow/Keras)                      │
│     ┌────────────────────────────────────────────────────┐  │
│     │ Input: Preprocessed tensor (1, 128, 128, 3)       │  │
│     │         ↓                                          │  │
│     │ CNN Forward Pass through layers:                  │  │
│     │  • Convolutional layers extract features          │  │
│     │  • Pooling layers reduce dimensions               │  │
│     │  • Dense layers classify                          │  │
│     │  • Sigmoid activation outputs probability         │  │
│     │         ↓                                          │  │
│     │ Output: Probability tensor (1, 1) or (1, 2)       │  │
│     │         Range: [0, 1]                              │  │
│     └────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Result Interpretation                                    │
│     ┌────────────────────────────────────────────────────┐  │
│     │ If prediction.shape[-1] == 1:                     │  │
│     │   → Binary sigmoid output                         │  │
│     │   → probability = predictions[0][0]               │  │
│     │   → threshold: >= 0.5 = Flooded                   │  │
│     │                < 0.5 = Non-Flooded                │  │
│     │                                                    │  │
│     │ Else:                                              │  │
│     │   → Multi-class softmax output                    │  │
│     │   → probability = max(predictions)                │  │
│     │   → class_index = argmax(predictions)             │  │
│     └────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  7. Cleanup and Response                                     │
│     • Delete temp_image.jpg                                  │
│     • Format JSON response:                                  │
│       {                                                      │
│         "prediction": "Flooded Area",                        │
│         "probability": 0.876,                                │
│         "status": "success"                                  │
│       }                                                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  8. Display Results to User                                  │
│     • Hide loading spinner                                   │
│     • Show prediction label                                  │
│     • Show confidence score                                  │
│     • Handle any errors gracefully                           │
└─────────────────────────────────────────────────────────────┘
```

## 🔍 Deep Dive: Key Components

### Image Preprocessing Details

#### Why Each Step Matters:

1. **BGR to RGB Conversion**
   ```python
   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   ```
   - OpenCV loads images in BGR format by default
   - Most deep learning models expect RGB format
   - Mismatch causes incorrect predictions (wrong color channels)

2. **Resizing to 128×128**
   ```python
   img = cv2.resize(img, (128, 128))
   ```
   - Model was trained on 128×128 images
   - All inputs must match this size
   - Interpolation handles aspect ratio changes

3. **Normalization**
   ```python
   img = img / 255.0
   ```
   - Converts pixel values from [0, 255] to [0, 1]
   - Neural networks train faster with normalized inputs
   - Prevents numerical instability

4. **Batch Dimension**
   ```python
   img = np.expand_dims(img, axis=0)
   ```
   - Models expect batches, even for single predictions
   - Changes shape from (128, 128, 3) to (1, 128, 128, 3)
   - First dimension represents batch size

### Model Prediction Process

#### Input Processing:
```python
preprocessed_image = preprocess_image(image_path)
# Shape: (1, 128, 128, 3)
# Values: [0.0, 1.0]
```

#### Forward Pass:
```python
predictions = model.predict(preprocessed_image)
# Returns probability or probabilities
# Shape: (1, 1) for binary or (1, num_classes) for multi-class
```

#### Threshold Application:
```python
# For sigmoid output:
if probability >= 0.5:
    result = "Flooded Area"
else:
    result = "Non-Flooded Area"
```

### Error Handling Strategy

#### Try-Catch Structure:
```python
try:
    # Main prediction logic
    # ...
except Exception as e:
    # Catch all errors
    # Log error message
    # Clean up temporary files
    # Return user-friendly error
```

#### Common Errors Handled:
1. **No file uploaded**: `'image' not in request.files`
2. **Empty filename**: `file.filename == ''`
3. **Invalid image format**: Caught during cv2.imread()
4. **Model prediction failure**: Caught during model.predict()
5. **File system errors**: Caught during file operations

## 📊 Data Structures

### Request Format (POST /predict):
```
Content-Type: multipart/form-data
{
    image: <binary image data>
}
```

### Response Format (Success):
```json
{
    "prediction": "Flooded Area",
    "probability": 0.876,
    "status": "success"
}
```

### Response Format (Error):
```json
{
    "error": "Error message here",
    "status": "failure"
}
```

## 🔧 Configuration Options

### Flask Configuration:
```python
# Development
app.run(debug=True, host='127.0.0.1', port=5000)

# Production (using Gunicorn)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
# -w 4: 4 worker processes
# -b 0.0.0.0:8000: Bind to all interfaces on port 8000
```

### Model Configuration:
- Input size: 128×128×3 (hardcoded)
- Normalization: 0-1 range (hardcoded)
- Threshold: 0.5 (hardcoded in prediction logic)

## 🚀 Performance Considerations

### Bottlenecks:
1. **Model Loading**: ~1-2 seconds at startup (one-time)
2. **Image Preprocessing**: ~100-200ms per image
3. **Model Inference**: ~500ms-1s per image (CPU)
4. **File I/O**: ~50-100ms for save/delete

### Optimization Opportunities:
1. **Use GPU**: TensorFlow will automatically use GPU if available
2. **Batch Processing**: Process multiple images simultaneously
3. **Model Quantization**: Reduce model size without significant accuracy loss
4. **Caching**: Cache preprocessed images if repeated predictions needed
5. **Async Processing**: Use task queue (Celery) for long-running predictions

## 🔐 Security Considerations

### Current Implementation:
- ⚠️ Temporary files use predictable names
- ⚠️ No file type validation
- ⚠️ No file size limits
- ⚠️ Debug mode enabled

### Recommended Improvements:
```python
from werkzeug.utils import secure_filename
import uuid

# Generate unique temporary filename
temp_filename = f"temp_{uuid.uuid4()}.jpg"

# Validate file extension
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
if not allowed_file(file.filename):
    return error_response()

# Limit file size (Flask config)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

## 📈 Scalability

### Current Limitations:
- Single-threaded Flask development server
- Synchronous request handling
- No load balancing
- In-memory model (duplicated per worker)

### Scaling Solutions:
1. **Use Gunicorn with multiple workers**
2. **Deploy behind Nginx reverse proxy**
3. **Implement Redis caching for common predictions**
4. **Use cloud services (AWS Lambda, Google Cloud Functions)**
5. **Containerize with Docker for easy deployment**

## 🧪 Testing Strategy

### Unit Tests Needed:
- `preprocess_image()` function
- Image format conversions
- File upload validation
- Prediction threshold logic

### Integration Tests Needed:
- End-to-end prediction flow
- Error handling scenarios
- API response formats

### Example Test Structure:
```python
def test_preprocess_image():
    # Test image loading
    # Test color conversion
    # Test resizing
    # Test normalization
    # Test batch dimension

def test_predict_endpoint():
    # Test valid image upload
    # Test invalid file formats
    # Test missing file
    # Test prediction accuracy
```

## 📚 Dependencies Explained

| Library    | Purpose                           | Critical Path |
|------------|-----------------------------------|---------------|
| Flask      | Web framework                     | Yes           |
| TensorFlow | Model loading and inference       | Yes           |
| NumPy      | Array operations                  | Yes           |
| OpenCV     | Image preprocessing               | Yes           |
| Werkzeug   | Flask utilities                   | Indirect      |
| Gunicorn   | Production server                 | Production    |
| Matplotlib | Visualization (optional)          | No            |

## 🔄 Code Maintenance

### Adding New Features:
1. **Multiple Image Upload**: Modify frontend form + backend to handle arrays
2. **Batch Prediction**: Loop through multiple images + aggregate results
3. **Confidence Threshold Setting**: Add UI slider + pass to backend
4. **Result History**: Add database + store predictions
5. **Advanced Analytics**: Add visualization of affected areas

### Modifying the Model:
```python
# To use a different model:
MODEL_PATH = "model/new_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Update preprocessing if input size changes:
img = cv2.resize(img, (NEW_WIDTH, NEW_HEIGHT))
```

---

**This architecture ensures modularity, maintainability, and scalability for the flood detection application.**
