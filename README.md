🌊 Flood Detection Web App using Deep Learning

This project is a Flask-based web application that predicts whether a given aerial image shows a Flooded or Non-Flooded area using a trained TensorFlow/Keras model.
Users can upload an image, and the app returns a prediction along with the probability.

🚀 Features

🧠 Deep learning model trained to detect flooded areas

🖼️ Upload any image for real-time prediction

⚡ Fast Flask backend API

💅 Modern UI with live preview and loading spinner

🔒 Handles image preprocessing and cleanup safely

🏗️ Tech Stack
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Flask (Python)
Model	TensorFlow / Keras
Image Processing	OpenCV & NumPy
📁 Project Structure
flood-detection-app/
│
├── app.py                     # Flask app
├── model/
│   └── flood_detection_trained_model.h5   # Trained CNN model
├── templates/
│   └── index.html             # Frontend UI
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/flood-detection-app.git
cd flood-detection-app

2️⃣ Create a virtual environment (recommended)
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your trained model

Place your trained model file inside the model/ folder and name it:

model/flood_detection_trained_model.h5

5️⃣ Run the app
python app.py


Then open your browser and visit:

http://127.0.0.1:5000

🧠 Model Details

The model is a Convolutional Neural Network (CNN) trained to classify images as:

Flooded Area

Non-Flooded Area

Input images are resized to 128x128 and normalized before prediction.

🖼️ Usage

Launch the app in your browser.

Upload an aerial image.

Click Predict.

The result shows:

The predicted label (Flooded Area / Non-Flooded Area)

The confidence probability (e.g., 0.87)

📦 Requirements
Flask==3.0.3
tensorflow==2.17.0
opencv-python==4.10.0.84
numpy==1.26.4


Install all using:

pip install -r requirements.txt

⚡ Example Response

Input: Aerial photo of a river region after rainfall
Output:

Prediction: Flooded Area
Probability: 0.91

🧰 Troubleshooting

Error: "An error occurred while processing the image"
→ Ensure your model path is correct and image format is supported (.jpg, .png).

All predictions show "Flooded Area"
→ Check model training balance or threshold logic (>= 0.5 in app.py).

TensorFlow not found
→ Reinstall using pip install tensorflow.

🌟 Future Improvements

✅ Add color-coded results (red for Flooded, green for Non-Flooded)

✅ Add confidence bar visualization

🔄 Integrate real-time webcam prediction

☁️ Deploy on AWS / Render / Hugging Face Spaces

👨‍💻 Author

Developed by: @samarthpatilML For
Role: Python Developer | Deep Learning Enthusiast
Tech Stack: Flask · TensorFlow · OpenCV · HTML/CSS/JS
