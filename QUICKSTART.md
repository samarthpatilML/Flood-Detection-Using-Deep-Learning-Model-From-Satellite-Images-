# 🚀 Quick Start Guide

## Get Up and Running in 5 Minutes

This guide will help you quickly set up and run the Flood Detection application.

## Prerequisites

Before you begin, ensure you have:
- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- **pip** package manager (comes with Python)
- **4GB+ RAM** (for model loading)
- **500MB+ free disk space**

### Check Your Python Version
```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.8.x` or higher

## Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/samarthpatilML/Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-.git
cd Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Installation may take 5-10 minutes** as it downloads TensorFlow (~500MB) and other packages.

#### If you encounter issues:
```bash
# Use pip3 if pip doesn't work
pip3 install -r requirements.txt

# Or create a virtual environment first (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Verify Model File
```bash
ls -lh model/flood_detection_trained_model.h5
```

You should see a file of approximately **57 MB**.

### Step 4: Run the Application
```bash
python app.py
```

**Expected Output:**
```
============================================================
🌊 FLOOD DETECTION APPLICATION
============================================================
🚀 Starting Flask server...
📡 Access the application at: http://localhost:5000
⚠️  Press CTRL+C to stop the server
============================================================

✅ Model loaded successfully!
Model input shape: (None, 128, 128, 3)
Model output shape: (None, 1)
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Step 5: Open Your Browser
Navigate to: **http://localhost:5000** or **http://127.0.0.1:5000**

You should see the Flood Detection web interface!

## Using the Application

### Upload and Predict

1. **Click "Choose File"** button
2. **Select a satellite image** from your computer
   - Supported formats: JPG, PNG, JPEG
   - The image will preview automatically
3. **Click "Predict"** button
4. **Wait for results** (1-2 seconds)
   - A loading spinner will appear
5. **View the prediction**:
   ```
   Prediction: Flooded Area
   Probability: 0.876
   ```

### Test with Sample Images

Try testing with images from the dataset:

**Flooded Area Example:**
```bash
# Navigate to: FloodDataset/test/damage/
# Upload any image like: 68.2094_29.9284.jpg
```

**Non-Flooded Area Example:**
```bash
# Navigate to: FloodDataset/test/notdamage/
# Upload any image like: 68.0302_26.143.jpg
```

## Troubleshooting

### Issue: "Port 5000 is already in use"

**Solution 1**: Stop the process using port 5000
```bash
# On Linux/Mac
lsof -ti:5000 | xargs kill -9

# On Windows
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

**Solution 2**: Change the port in `app.py`
```python
# At the bottom of app.py, change:
app.run(debug=True)
# to:
app.run(debug=True, port=5001)
```
Then access at: http://localhost:5001

### Issue: "No module named 'flask'" or similar

**Solution**: Reinstall dependencies
```bash
pip install --upgrade -r requirements.txt
```

Or install individually:
```bash
pip install Flask==3.0.3
pip install tensorflow==2.16.1
pip install numpy==1.26.4
pip install opencv-python==4.10.0.84
```

### Issue: "Model file not found"

**Solution**: Verify the model file exists
```bash
# Check if file exists
ls model/flood_detection_trained_model.h5

# If missing, you may need to:
# 1. Re-clone the repository with Git LFS enabled
# 2. Download the model file separately
# 3. Retrain the model using the notebook
```

### Issue: TensorFlow installation fails

**Solution**: Try installing CPU-only version
```bash
pip install tensorflow-cpu==2.16.1
```

### Issue: Application crashes on prediction

**Possible causes**:
1. **Insufficient RAM**: Close other applications
2. **Corrupted image**: Try a different image
3. **Wrong image format**: Use JPG or PNG

**Check logs** in the terminal for error messages.

### Issue: Predictions seem incorrect

**Possible causes**:
1. **Image quality**: Use clear satellite imagery
2. **Wrong image type**: Model expects aerial/satellite views
3. **Lighting conditions**: Ensure good visibility

## Next Steps

### 1. Read the Documentation
- **[README.md](README.md)**: Full project overview
- **[CODE_STRUCTURE.md](CODE_STRUCTURE.md)**: Architecture deep dive
- **[DATASET_INFO.md](DATASET_INFO.md)**: Dataset details

### 2. Explore the Code
- Open `app.py` to see the application logic
- Check `templates/index.html` for the web interface
- Review `notebook/` for model training code

### 3. Experiment
- Try different satellite images
- Modify the confidence threshold
- Adjust the image preprocessing

### 4. Deploy to Production
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn (production server)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Command Reference

### Starting the Application
```bash
python app.py
```

### Stopping the Application
Press **CTRL + C** in the terminal

### Checking Dependencies
```bash
pip list
```

### Updating Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Running in Background (Linux/Mac)
```bash
nohup python app.py &
```

### Viewing Logs (if running in background)
```bash
tail -f nohup.out
```

## Performance Tips

### For Faster Predictions
1. **Use GPU**: Install TensorFlow with GPU support
2. **Close unnecessary applications**: Free up RAM
3. **Use smaller images**: Resize before upload (though model will resize anyway)

### For Better Accuracy
1. **Use high-quality images**: Clear satellite imagery
2. **Ensure proper lighting**: Avoid night images or heavy clouds
3. **Use recent images**: Flood conditions change over time

## Common Workflows

### Workflow 1: Quick Test
```bash
# 1. Start application
python app.py

# 2. Open browser: http://localhost:5000
# 3. Upload test image from FloodDataset/test/damage/
# 4. View results
# 5. Stop with CTRL+C
```

### Workflow 2: Batch Processing
```python
# Create a custom script to process multiple images
import os
from app import preprocess_image, model

image_folder = "FloodDataset/test/damage/"
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_folder, filename)
        preprocessed = preprocess_image(image_path)
        prediction = model.predict(preprocessed)
        print(f"{filename}: {prediction[0][0]:.3f}")
```

### Workflow 3: Development
```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make code changes

# 4. Test changes
python app.py

# 5. Deactivate when done
deactivate
```

## Getting Help

### Resources
- **GitHub Issues**: [Report bugs or ask questions](https://github.com/samarthpatilML/Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-/issues)
- **Documentation**: Check README.md and other .md files
- **Code Comments**: Read inline comments in app.py

### Before Asking for Help
1. Check this Quick Start guide
2. Read the error message carefully
3. Search existing GitHub issues
4. Include error logs when reporting issues

## Success Checklist

- [ ] Python 3.8+ installed and working
- [ ] Repository cloned successfully
- [ ] Dependencies installed without errors
- [ ] Model file exists (57 MB)
- [ ] Application starts without errors
- [ ] Web interface loads in browser
- [ ] Can upload and preview images
- [ ] Predictions return results
- [ ] Understand how to stop the server

---

**🎉 Congratulations! You're ready to use the Flood Detection application!**

For more detailed information, see the [full README](README.md).
