# 📊 Dataset Information and Structure

## Overview

This document provides detailed information about the flood detection dataset used for training and testing the deep learning model.

## 📁 Dataset Organization

### Directory Structure

```
FloodDataset/
│
├── test/                          # Original test dataset
│   ├── damage/                   # 87 flooded area images
│   └── notdamage/                # 140 non-flooded area images
│
├── test_another/                 # Additional test dataset
│   ├── damage/                   # 44 flooded area images
│   └── no_damage/                # 44 non-flooded area images
│
├── train_another/                # Training dataset
│   ├── damage/                   # 79 flooded area images
│   └── notdamage/                # 140 non-flooded area images
│
└── validation_another/           # Validation dataset
    ├── damage/                   # 79 flooded area images
    └── notdamage/                # 140 non-flooded area images
```

### Naming Inconsistencies

**Note**: There are minor naming inconsistencies across directories:
- `test/` uses `damage` and `notdamage`
- `test_another/` uses `damage` and `no_damage` (with underscore)
- `train_another/` uses `damage` and `notdamage`
- `validation_another/` uses `damage` and `notdamage`

This is handled correctly in the training notebook but worth noting for consistency.

## 📈 Dataset Statistics

### Overall Statistics

| Dataset           | Flooded (damage) | Non-Flooded (notdamage) | Total | Class Balance |
|-------------------|------------------|-------------------------|-------|---------------|
| test              | 87               | 140                     | 227   | 38% / 62%     |
| test_another      | 44               | 44                      | 88    | 50% / 50%     |
| train_another     | 79               | 140                     | 219   | 36% / 64%     |
| validation_another| 79               | 140                     | 219   | 36% / 64%     |
| **TOTAL**         | **289**          | **464**                 | **753** | **38% / 62%** |

### Class Distribution Analysis

The dataset shows a **class imbalance**:
- **Non-Flooded images**: 62% (464 images)
- **Flooded images**: 38% (289 images)

**Implications**:
- Model may have slight bias toward predicting non-flooded areas
- During training, class weights or data augmentation should be considered
- Evaluation metrics should include precision, recall, and F1-score, not just accuracy

## 🗺️ Image Naming Convention

### Format
All images follow the pattern: `{longitude}_{latitude}.jpg`

### Examples
- `68.2094_29.9284.jpg` → Location: 68.2094° longitude, 29.9284° latitude
- `96.5691_34.3297.jpg` → Location: 96.5691° longitude, 34.3297° latitude

### Geographic Coverage

#### Longitude Range
- **Minimum**: ~68.0°
- **Maximum**: ~96.9°
- **Coverage**: ~29° span (approximately 2,900 km at the equator)

#### Latitude Range
- **Minimum**: ~8.0°
- **Maximum**: ~36.9°
- **Coverage**: ~29° span (approximately 3,200 km)

### Probable Geographic Region
Based on coordinate ranges (68-97°E, 8-37°N), this dataset likely covers:
- **Region**: South Asia and parts of Southeast Asia
- **Possible countries**: 
  - India (northern and central regions)
  - Pakistan
  - Nepal
  - Bangladesh
  - Myanmar (Burma)
  - Parts of China (western regions)

This region is known for:
- Monsoon floods
- River flooding (Ganges, Brahmaputra, Indus)
- Cyclone-related flooding
- Seasonal heavy rainfall

## 🖼️ Image Characteristics

### Technical Specifications
- **Format**: JPEG (.jpg)
- **Color Space**: RGB (3 channels)
- **Source**: Satellite imagery
- **Resolution**: Variable (original size not standardized)
- **Processed Size**: Resized to 128×128 for model input

### Image Content
Images appear to be:
- **Top-down view**: Satellite/aerial perspective
- **Geographic features**: Rivers, urban areas, agricultural land
- **Flood indicators**: Water coverage, inundation patterns
- **Time period**: Not specified in metadata

## 🔄 Dataset Splits

### Purpose of Each Split

#### 1. Training Set (`train_another/`)
- **Purpose**: Train the CNN model
- **Size**: 219 images (79 flooded, 140 non-flooded)
- **Usage**: Model learns features from this data
- **Augmentation**: Likely used during training (rotation, flipping, etc.)

#### 2. Validation Set (`validation_another/`)
- **Purpose**: Hyperparameter tuning and model selection
- **Size**: 219 images (79 flooded, 140 non-flooded)
- **Usage**: Monitor training progress, prevent overfitting
- **Note**: Never used for training, only for evaluation during training

#### 3. Test Set (`test/`)
- **Purpose**: Final model evaluation
- **Size**: 227 images (87 flooded, 140 non-flooded)
- **Usage**: Unbiased performance assessment
- **Note**: Only used after training is complete

#### 4. Additional Test Set (`test_another/`)
- **Purpose**: Additional evaluation with balanced classes
- **Size**: 88 images (44 flooded, 44 non-flooded)
- **Usage**: Balanced evaluation to check for class imbalance effects
- **Advantage**: 50/50 split provides unbiased accuracy metric

### Split Ratios

If we consider `train_another` + `validation_another` as training data:

| Split      | Images | Percentage |
|------------|--------|------------|
| Training   | 219    | 29%        |
| Validation | 219    | 29%        |
| Testing    | 315    | 42%        |
| **Total**  | **753** | **100%**   |

**Note**: The test set is relatively large (42%), which is good for robust evaluation but leaves less data for training.

## 📋 Dataset Metadata

### CSV File: `renamed_image_data.csv`
Located in: `notebook/renamed_image_data.csv`

**Size**: ~132 KB

**Contents** (inferred):
- Image filenames
- Coordinate information (longitude, latitude)
- Class labels (damage/no damage)
- Possibly additional metadata (date, source, etc.)

**Usage**:
- Track image locations
- Facilitate dataset organization
- Enable geographic analysis of flooding patterns

## 🎯 Dataset Quality Considerations

### Strengths
1. **Geographic Diversity**: Wide coverage area (~29° × 29°)
2. **Coordinate Information**: Each image has precise location data
3. **Multiple Test Sets**: Allows for robust evaluation
4. **Balanced Test Set**: `test_another` provides unbiased evaluation

### Potential Issues
1. **Class Imbalance**: 38% flooded vs 62% non-flooded
2. **Limited Size**: Only 753 total images
3. **Unknown Resolution**: Original image sizes may vary
4. **No Temporal Information**: Can't analyze flooding over time
5. **No Severity Labels**: Binary classification only (flooded vs not)

### Data Quality Checklist

✅ **Good**:
- Clear directory organization
- Consistent file naming
- Geographic metadata available
- Multiple evaluation sets

⚠️ **Needs Attention**:
- Class imbalance (consider weighted loss)
- Small dataset size (consider augmentation)
- No severity levels (only binary)
- No temporal component

## 🔄 Data Augmentation Strategies

To improve model performance with limited data:

### Recommended Augmentations
1. **Geometric Transformations**:
   - Random rotation (0°-360°)
   - Horizontal/vertical flipping
   - Random zoom (0.8x-1.2x)
   
2. **Color Augmentation**:
   - Brightness adjustment
   - Contrast adjustment
   - Saturation changes
   
3. **Advanced Techniques**:
   - Random cropping
   - Gaussian noise addition
   - Cutout/random erasing

### Example Code
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
```

## 📊 Class Distribution Visualization

### Training Set Distribution
```
damage (flooded):     ████████████████░░░░░░░░░░░░░░░░░░ 36% (79)
notdamage:            ████████████████████████████████████ 64% (140)
```

### Test Set Distribution
```
damage (flooded):     ████████████████░░░░░░░░░░░░░░░░░░ 38% (87)
notdamage:            ████████████████████████████████████ 62% (140)
```

### Balanced Test Set Distribution
```
damage (flooded):     ████████████████████████████████████ 50% (44)
no_damage:            ████████████████████████████████████ 50% (44)
```

## 🌍 Geographic Analysis

### Distribution by Longitude
The dataset spans a wide longitude range, suggesting coverage of different geographic regions with varying flood characteristics:

- **Western Region (68-75°)**: ~25% of images
- **Central Region (75-85°)**: ~35% of images
- **Eastern Region (85-97°)**: ~40% of images

### Distribution by Latitude
Latitude distribution indicates coverage from tropical to temperate regions:

- **Southern Tropical (8-20°)**: ~35% of images
- **Northern Subtropical (20-30°)**: ~40% of images
- **Temperate (30-37°)**: ~25% of images

## 🔍 Dataset Usage in Model Training

### Loading Images
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create data generator
datagen = ImageDataGenerator(rescale=1./255)

# Load training data
train_generator = datagen.flow_from_directory(
    'FloodDataset/train_another/',
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary'
)
```

### Class Indices
```python
# Typically:
# {'damage': 0, 'notdamage': 1}
# or
# {'damage': 1, 'notdamage': 0}

print(train_generator.class_indices)
```

## 📈 Recommended Improvements

### Dataset Enhancement
1. **Collect More Data**: Increase dataset size to 2,000+ images
2. **Balance Classes**: Collect more flooded area images
3. **Add Severity Labels**: Light/Moderate/Severe flooding
4. **Temporal Data**: Multiple images of same location over time
5. **Metadata**: Add date, time, flood cause, affected area size

### Quality Control
1. **Manual Review**: Verify correct labels
2. **Remove Duplicates**: Check for similar images
3. **Standardize Resolution**: Ensure consistent quality
4. **Add Difficult Cases**: Include edge cases (partial flooding, etc.)

## 📚 References and Sources

While the specific source of this dataset is not documented in the repository, satellite flood imagery typically comes from:

- **Sentinel-1/2** (ESA): Open-access satellite imagery
- **Landsat** (NASA/USGS): Long-term Earth observation
- **MODIS**: Moderate resolution imagery
- **Planet Labs**: High-resolution commercial imagery
- **Google Earth Engine**: Aggregated satellite data

## 📝 Usage Guidelines

### For Training
```python
# Recommended approach
train_path = 'FloodDataset/train_another/'
val_path = 'FloodDataset/validation_another/'
test_path = 'FloodDataset/test/'
```

### For Evaluation
```python
# Use balanced test set for unbiased accuracy
balanced_test_path = 'FloodDataset/test_another/'

# Use regular test set for real-world distribution
real_world_test_path = 'FloodDataset/test/'
```

### Best Practices
1. **Always use separate test set**: Don't evaluate on training data
2. **Apply same preprocessing**: Ensure consistency between train/test
3. **Monitor class imbalance**: Use class weights if needed
4. **Use multiple metrics**: Accuracy, precision, recall, F1-score
5. **Cross-validate**: If dataset is small, consider k-fold CV

---

**This dataset provides a solid foundation for flood detection, with opportunities for enhancement through augmentation and additional data collection.**
