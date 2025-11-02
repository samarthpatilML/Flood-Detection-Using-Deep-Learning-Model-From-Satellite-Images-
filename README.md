# 🌊 Flood Detection Using Deep Learning Model From Satellite Images

## 📋 Project Overview

This project uses deep learning to detect flooded areas from satellite images. It employs a Convolutional Neural Network (CNN) trained on satellite imagery to classify regions as either "Flooded" or "Non-Flooded". The application provides a user-friendly web interface for real-time predictions.

## 🎯 Purpose

Natural disasters like floods cause significant damage to lives and property. This tool helps in:
- **Early Detection**: Identify flooded areas quickly from satellite imagery
- **Disaster Response**: Aid emergency responders in assessing affected regions
- **Resource Allocation**: Help authorities prioritize rescue and relief efforts
- **Damage Assessment**: Evaluate the extent of flooding in different areas

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                     Flask Web Application                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐         ┌──────────────────────────────┐ │
│  │   Frontend   │ ──────► │        Backend (app.py)      │ │
│  │ (index.html) │         │  - Image Upload Handler      │ │
│  │              │ ◄────── │  - Image Preprocessing       │ │
│  │  - Upload UI │         │  - Model Prediction          │ │
│  │  - Display   │         │  - Result Formatting         │ │
│  └──────────────┘         └──────────────────────────────┘ │
│                                       │                       │
│                                       ▼                       │
│                            ┌─────────────────────┐          │
│                            │  Trained CNN Model  │          │
│                            │  (Keras/TensorFlow) │          │
│                            │   - Input: 128x128  │          │
│                            │   - RGB Channels    │          │
│                            │   - Binary Output   │          │
│                            └─────────────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-/
│
├── app.py                          # Flask web application (main entry point)
├── requirements.txt                # Python dependencies
├── filestructure.txt              # Visual representation of file structure
│
├── model/                         # Trained model directory
│   └── flood_detection_trained_model.h5   # Pre-trained CNN model (~57MB)
│
├── notebook/                      # Jupyter notebook for training
│   ├── Flood-Detection-Using-Deep-Learning-Satellite-Images.ipynb
│   └── renamed_image_data.csv     # Dataset metadata
│
├── templates/                     # HTML templates for Flask
│   └── index.html                 # Web interface for predictions
│
└── FloodDataset/                  # Training and testing datasets
    ├── test/                      # Test dataset (original split)
    │   ├── damage/               # Flooded area images (87 images)
    │   └── notdamage/            # Non-flooded area images (140 images)
    │
    ├── test_another/             # Additional test dataset
    │   ├── damage/               # Flooded images (44 images)
    │   └── no_damage/            # Non-flooded images (44 images)
    │
    ├── train_another/            # Additional training dataset
    │   ├── damage/               # Flooded images (79 images)
    │   └── notdamage/            # Non-flooded images (140 images)
    │
    └── validation_another/       # Validation dataset
        ├── damage/               # Flooded images (79 images)
        └── notdamage/            # Non-flooded images (140 images)
```

## 🔍 How It Works

### 1. **Image Preprocessing Pipeline**

```python
Image Upload → Read with OpenCV → Convert BGR to RGB → Resize to 128x128
    → Normalize (0-1) → Add Batch Dimension → Ready for Model
```

**Details:**
- **Input Format**: Any standard image format (JPG, PNG, etc.)
- **Color Space Conversion**: OpenCV uses BGR; converted to RGB for model
- **Resizing**: All images standardized to 128×128 pixels
- **Normalization**: Pixel values scaled from [0, 255] to [0, 1]
- **Batch Dimension**: Shape becomes (1, 128, 128, 3) for model input

### 2. **Model Architecture**

The trained model (`flood_detection_trained_model.h5`) is a Convolutional Neural Network:
- **Input Shape**: (128, 128, 3) - RGB images
- **Architecture**: CNN layers with convolution, pooling, and dense layers
- **Output**: Binary classification (Flooded vs Non-Flooded)
- **Activation**: Sigmoid for binary classification
- **Framework**: TensorFlow/Keras

### 3. **Prediction Process**

```
Preprocessed Image → CNN Forward Pass → Probability Score
    → Threshold (0.5) → Classification → Display Result
```

**Output Interpretation:**
- **Probability ≥ 0.5**: Classified as "Flooded Area"
- **Probability < 0.5**: Classified as "Non-Flooded Area"
- **Confidence**: The probability value indicates model confidence (0-1 scale)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM (for model loading)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/samarthpatilML/Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-.git
   cd Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify model file exists**
   ```bash
   ls -lh model/flood_detection_trained_model.h5
   ```
   The model file should be approximately 57MB.

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser
   - Navigate to: `http://localhost:5000` or `http://127.0.0.1:5000`

3. **Make predictions**
   - Click "Choose File" to upload a satellite image
   - Click "Predict" button
   - View the classification result and confidence score

### Expected Output

```
Prediction: Flooded Area
Probability: 0.876
```

or

```
Prediction: Non-Flooded Area
Probability: 0.234
```

## 📊 Dataset Information

### Image Naming Convention
Images are named with coordinates: `{longitude}_{latitude}.jpg`
- Example: `68.2094_29.9284.jpg` represents location at 68.2094°, 29.9284°

### Dataset Statistics

| Dataset           | Flooded Images | Non-Flooded Images | Total |
|-------------------|----------------|--------------------|-------|
| test              | 87             | 140                | 227   |
| test_another      | 44             | 44                 | 88    |
| train_another     | 79             | 140                | 219   |
| validation_another| 79             | 140                | 219   |

### Data Characteristics
- **Format**: JPG images
- **Source**: Satellite imagery
- **Geographic Coverage**: Coordinates ranging from ~68° to ~97° longitude
- **Classes**: Binary (damage/flooded vs notdamage/non-flooded)

## 🔧 Technical Details

### Dependencies

| Package         | Version | Purpose                              |
|-----------------|---------|--------------------------------------|
| Flask           | 3.0.3   | Web framework for the application    |
| TensorFlow      | 2.16.1  | Deep learning framework              |
| NumPy           | 1.26.4  | Numerical computations               |
| OpenCV-Python   | 4.10.0  | Image processing operations          |
| Gunicorn        | 22.0.0  | Production WSGI server (optional)    |
| Matplotlib      | 3.9.2   | Visualization (optional)             |
| Werkzeug        | 3.0.3   | Flask compatibility utilities        |

### API Endpoints

#### `GET /`
- **Description**: Serves the main web interface
- **Returns**: HTML page with upload form

#### `POST /predict`
- **Description**: Processes uploaded image and returns prediction
- **Input**: 
  - Form-data with key `image` containing image file
- **Output**: JSON response
  ```json
  {
    "prediction": "Flooded Area" | "Non-Flooded Area",
    "probability": 0.876,
    "status": "success" | "failure"
  }
  ```
- **Error Response**:
  ```json
  {
    "error": "Error message",
    "status": "failure"
  }
  ```

### Model Training

The model was trained using the Jupyter notebook:
`notebook/Flood-Detection-Using-Deep-Learning-Satellite-Images.ipynb`

**Training Process:**
1. Data loading and preprocessing
2. Data augmentation for better generalization
3. CNN architecture design and compilation
4. Model training with train/validation split
5. Model evaluation and performance metrics
6. Saving the trained model as .h5 file

## 🎨 Web Interface Features

- **Clean, Modern Design**: Gradient background with centered card layout
- **Responsive**: Works on desktop and mobile devices
- **Image Preview**: See uploaded image before prediction
- **Loading Indicator**: Spinner animation during processing
- **Real-time Results**: Instant display of prediction and probability
- **Error Handling**: User-friendly error messages

## 🐛 Troubleshooting

### Common Issues

1. **Model file not found**
   ```
   Error: Unable to load model
   Solution: Ensure model/flood_detection_trained_model.h5 exists
   ```

2. **Memory error during model loading**
   ```
   Solution: Ensure at least 4GB RAM available
   ```

3. **Port already in use**
   ```
   Solution: Change port in app.py: app.run(port=5001)
   ```

4. **Image upload fails**
   ```
   Solution: Check image format (JPG, PNG supported)
             Ensure file size < 10MB
   ```

## 🔬 Model Performance

The model demonstrates good performance on satellite imagery:
- **Input Requirements**: 128×128 RGB images
- **Processing Time**: ~1-2 seconds per image
- **Accuracy**: Depends on image quality and flood visibility

**Limitations:**
- May struggle with partially flooded areas
- Performance varies with image resolution and clarity
- Works best with clear satellite imagery

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment (using Gunicorn)
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker Deployment (if Dockerfile added)
```bash
docker build -t flood-detection .
docker run -p 5000:5000 flood-detection
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Model accuracy enhancement
- Additional data augmentation
- Multi-class classification (severity levels)
- Batch processing capability
- API documentation
- Mobile application

## 📄 License

This project is open-source. Please check the repository for license details.

## 👤 Author

Samarth Patil
- GitHub: [@samarthpatilML](https://github.com/samarthpatilML)

## 🙏 Acknowledgments

- Satellite imagery datasets for training
- TensorFlow and Keras communities
- Flask framework developers

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Open an issue on GitHub
3. Review the code comments in `app.py`

---

**Built with ❤️ for disaster response and humanitarian aid**
