# Sanskrit Character Recognition and Digitization using Deep Learning

**Python • TensorFlow/Keras • OpenCV • Computer Vision • OCR • CNN • Tkinter GUI**

An end-to-end Optical Character Recognition (OCR) system developed for digitizing Sanskrit documents written in Devanagari script. The system combines image preprocessing, segmentation, and deep learning-based character recognition to convert scanned Sanskrit text into editable digital text. The final Convolutional Neural Network (CNN) model achieved **92.41% classification accuracy** across **58 Sanskrit character classes** and was deployed through a desktop GUI application.

> Developed as part of a Master of Engineering (Embedded Systems) dissertation at Sardar Vallabhbhai Patel Institute of Technology (SVIT), Gujarat Technological University.

---

## Overview

Sanskrit manuscripts and printed literature contain a large character set, including vowels, consonants, compound characters, and numerical symbols. Existing OCR systems primarily focus on isolated character recognition and often struggle with degraded documents, varying fonts, colored backgrounds, and handwritten content.

This project develops a Sanskrit-specific OCR pipeline capable of recognizing Sanskrit characters, words, complete sentences, and numerical entities from scanned document images. The work evaluates both traditional machine-learning approaches and deep-learning techniques, with CNN providing the highest recognition accuracy.

---

## Key Features

* Sanskrit OCR system for digitizing printed Sanskrit documents.
* Recognition of characters, words, and complete sentences.
* Detection of numerical entities within documents.
* Support for white and colored background document images.
* Image preprocessing and noise removal using multiple filtering techniques.
* Threshold-based segmentation for character extraction.
* CNN-based classification achieving 92.41% accuracy.
* Desktop GUI developed using Python Tkinter.
* Export recognized text to editable text files.
* Trained entirely on CPU without requiring GPU acceleration.

---

## Dataset

The OCR model was trained using a Sanskrit character dataset containing approximately **12,912 images** distributed across **58 classes**.

| Category   | Images |
| ---------- | -----: |
| Numerals   |  2,880 |
| Vowels     |  2,652 |
| Consonants |  7,380 |
| Total      | 12,912 |

* More than 200 samples per class.
* 80% training and 20% testing split.
* Dataset includes multiple writing styles and font variations.

> The complete dataset is not included in this repository due to size limitations.

---

## OCR Pipeline

```text
Input Document Image
        │
        ▼
Image Preprocessing
        │
        ▼
Noise Removal
        │
        ▼
Threshold-Based Segmentation
        │
        ▼
Character Extraction
        │
        ▼
CNN Classification
        │
        ▼
Text Recognition
        │
        ▼
Editable Text Output
```

---

## Image Processing Techniques

### Noise Removal

The following filtering techniques were evaluated:

* Median Filter
* Gaussian Filter
* Bilateral Filter
* Average Filter

The median filter provided the best performance for removing salt-and-pepper noise while preserving character boundaries.

### Segmentation

Threshold-based segmentation converts grayscale document images into binary representations and separates foreground text from the background for recognition.

---

## Deep Learning Model

The OCR engine uses a Convolutional Neural Network (CNN) implemented using TensorFlow and Keras.

### Model Highlights

* Input image size: 32 × 32 grayscale images
* 58 output classes
* Convolution and pooling layers
* Dropout regularization
* Dense fully connected layers
* Softmax classification output

Training configuration:

* Optimizer: Adam
* Loss Function: Categorical Cross-Entropy
* Epochs: 50
* Batch Size: 32

---

## Results

| Model                           |   Accuracy |
| ------------------------------- | ---------: |
| SVM (Wavelet Features)          |     72.16% |
| SVM (Wavelet + Moment Features) |     70.37% |
| CNN (20 Epochs)                 |     90.64% |
| CNN (50 Epochs)                 | **92.41%** |

The CNN significantly outperformed traditional machine-learning approaches and was selected as the final OCR engine.

---

## GUI Application

The project includes a desktop GUI developed using Tkinter.

The GUI supports:

* Training the CNN model
* Loading document images
* Performing segmentation
* Recognizing Sanskrit text
* Exporting recognized text
* Viewing training accuracy and loss plots

---

## Repository Structure

```text
Optical-Character-Recognition/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── gui.py
│   ├── train_cnn.py
│   └── predict.py
│
├── screenshots/
│   ├── gui_output.png
│   ├── plot1.png
│   ├── plot2.png
│
├── sample_data/
│   ├── sample_input_1.png
│   └── sample_input_2.png
│
└── docs/
    └── THESIS1.pdf
```

---

## Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* Scikit-Learn
* Pillow (PIL)
* Tkinter
* PyTesseract

---

## Setup

```bash
git clone https://github.com/jadejapratiksha/Optical-Character-Recognition.git

cd Optical-Character-Recognition

pip install -r requirements.txt
```

---

## Usage

Launch the GUI application:

```bash
python src/gui.py
```

Available GUI functions:

* Train
* Browse Image
* Segment
* Recognize
* Write Text
* Export Recognized Output

---

## Key Contributions

* Developed an end-to-end OCR system for Sanskrit document digitization.
* Designed image preprocessing and segmentation pipelines for noisy document images.
* Built and trained a CNN classifier achieving 92.41% recognition accuracy.
* Created a desktop GUI for image processing and text extraction.
* Evaluated traditional SVM and deep-learning approaches for Sanskrit OCR.
* Enabled automatic conversion of scanned Sanskrit documents into editable digital text.

---

## Author

**Pratiksha Jadeja**

M.S. VLSI and Embedded Systems
Arizona State University

Former M.E. Embedded Systems
Sardar Vallabhbhai Patel Institute of Technology (SVIT)

GitHub: https://github.com/jadejapratiksha

---

### Additional Requirement

Install Tesseract OCR separately:

https://github.com/UB-Mannheim/tesseract/wiki

Update the Tesseract executable path in `gui.py` if required.

## Acknowledgements

This work was inspired by ongoing research in Sanskrit OCR, document digitization, computer vision, and deep learning-based character recognition systems.

---

## License

This project is intended for educational and research purposes.
