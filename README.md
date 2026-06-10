<<<<<<< HEAD
# Sanskrit Character Recognition and Digitization using Deep Learning

**Python • TensorFlow/Keras • OpenCV • Computer Vision • OCR • CNN • Tkinter GUI**

An end-to-end Optical Character Recognition (OCR) system developed for digitizing Sanskrit documents written in Devanagari script. The system combines image preprocessing, segmentation, and deep learning-based character recognition to convert scanned Sanskrit text into editable digital text. The final Convolutional Neural Network (CNN) model achieved **92.41% classification accuracy** across **58 Sanskrit character classes** and was deployed through a desktop GUI application.

> Developed as part of a Master of Engineering (Embedded Systems) dissertation at Sardar Vallabhbhai Patel Institute of Technology (SVIT), Gujarat Technological University.
=======
# Sanskrit Character Recognition and Digitization using Soft Computing

An end-to-end Optical Character Recognition (OCR) system that recognizes and digitizes **printed and handwritten Sanskrit (Devanagari) documents** — including poorly maintained manuscripts with faded letters, overlapping characters, touching lines, mixed font sizes, and coloured backgrounds. Unlike most existing Sanskrit OCRs that classify only isolated characters, this system recognizes **characters, words, full sentences, and numeric entities**, and exports the result as an editable text file.

> Developed as an M.E. (Embedded Systems) dissertation at Sardar Vallabhbhai Patel Institute of Technology (SVIT), Gujarat Technological University.
>>>>>>> 5e34aa9ef941a5625cc311d5f7cb6e81e0b1db71

---

## Overview

<<<<<<< HEAD
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
=======
Most of India's ancient literature is written in Sanskrit, and a large fraction of these manuscripts are degraded and undigitized. Digitizing them is hard because Sanskrit contains a very large character set (13 vowels, 34 consonants, plus many compound/composite characters formed by joining half and full consonants) — far more classes than Hindi, which shares the same Devanagari script. A Hindi-trained OCR therefore performs poorly on Sanskrit.

This project builds a Sanskrit-specific OCR pipeline and compares a classical machine-learning classifier (SVM) against a deep-learning classifier (CNN) on the same data, then wraps the best model in a simple GUI for practical use.

## Key Features

- Recognizes Sanskrit **characters, words, and sentences**, not just isolated glyphs.
- Detects **number entities** in addition to text.
- Works on both **white** and **coloured** background documents.
- Robust to **noise, faded text, overlapping lines, touching characters, and varying font sizes** within a single page.
- Compares **SVM (DWT + moment features)** vs **CNN (deep learning)**.
- Outputs an **editable `.txt` file** from a scanned image.
- Trained entirely on **CPU** (no GPU required).

## What Makes It Different

| Capability | Existing systems | This project |
|---|:---:|:---:|
| Method | CNN | CNN |
| GPU required | Yes | **No** |
| Single character | Yes | Yes |
| Words | No | **Yes** |
| Sentences | No | **Yes** |
| Number entity | No | **Yes** |

## Pipeline

```
Scanned document image
        │
        ▼
   Pre-processing      →  noise removal (median / gaussian / bilateral / average filters)
        │
        ▼
   Binarization        →  grayscale → black & white
        │
        ▼
   Segmentation        →  thresholding: line → word → character
        │
        ▼
   Feature extraction  →  Discrete Wavelet Transform (DWT) + moment features
        │
        ▼
   Classification      →  SVM  /  CNN
        │
        ▼
   Editable text file
```

## Dataset

- **~12,912 images** of handwritten Sanskrit characters, organized into **58 classes**.
- Composition: **2,880** numerals, **2,652** vowels, **7,380** consonants.
- More than **200 images per class**.
- Split: **80% training / 20% testing**.

> The dataset is not redistributed in this repository. Place your image folders under `data/` (one subfolder per class) before training. See [Project Structure](#project-structure).

## Methodology

### 1. Pre-processing (noise removal)
Four smoothing filters were evaluated on documents with salt-and-pepper noise:

- **Average (box) filter** — replaces each pixel with the mean of its neighbourhood.
- **Gaussian filter** — weighted smoothing using a Gaussian kernel.
- **Median filter** — replaces each pixel with the neighbourhood median; best for salt-and-pepper noise.
- **Bilateral filter** — edge-preserving, noise-reducing, but slower.

The **median filter** gave the cleanest results and is used in the final pipeline.

### 2. Segmentation
**Thresholding** separates foreground text from background, producing a binary image that is then segmented into lines, words, and characters.

### 3. Feature extraction (for the SVM path)
- **Discrete Wavelet Transform (DWT)** — derives vertical (`cA`) and diagonal (`cD`) feature vectors.
- **Moment features** — area, perimeter, and centroid from image moments (`Cx = M10/M00`, `Cy = M01/M00`).
- The combined wavelet + moment feature vector (`fr`) is used to train the SVM.

### 4. Classification
- **SVM** — linear SVM trained on (a) wavelet features and (b) wavelet + moment features.
- **CNN** — a 2-block convolutional network (see architecture below); the CNN feeds learned features directly, so no hand-crafted features are needed.

## CNN Architecture

Input images are converted RGB → grayscale and fed as `28×28×1`. Activation: **ReLU**; pooling: **2×2 max-pooling**; **dropout** for regularization; **softmax** over 58 classes.

| Layer | Output shape | Params |
|---|---|---:|
| Conv2D | (27, 27, 64) | 320 |
| MaxPooling2D | (13, 13, 64) | 0 |
| Dropout | (13, 13, 64) | 0 |
| Conv2D | (12, 12, 32) | 8,224 |
| MaxPooling2D | (6, 6, 32) | 0 |
| Dropout | (6, 6, 32) | 0 |
| Flatten | (1152) | 0 |
| Dense | (128) | 147,584 |
| Dropout | (128) | 0 |
| Dense | (58) | 7,482 |
| **Total** | | **163,610** |

## Results

Trained on a 64-bit Intel i3 CPU (no GPU):

| Classifier | Features / Config | Training time | Accuracy |
|---|---|---|---:|
| SVM | Wavelet | 6 min 23 sec | 72.16% |
| SVM | Wavelet + Moment | 6 min 46 sec | 70.37% |
| CNN | 20 epochs | 23 min 04 sec | 90.64% |
| CNN | 50 epochs | 2 hr 11 min | **92.41%** |

The CNN clearly outperforms the SVM. The final system reaches **~92.41% accuracy** and also works on handwritten documents, though accuracy drops for slanted lines and heavily overlapping words.

## Tech Stack

- **Language:** Python 3
- **Deep learning:** TensorFlow / Keras
- **Classical ML:** scikit-learn (SVM)
- **Image processing:** OpenCV
- **Signal/feature processing:** PyWavelets (DWT), NumPy
- **GUI:** Tkinter
- **Environment:** Anaconda Navigator + Spyder

## Project Structure

> Suggested layout — adjust to match your actual files.

```
.
├── data/                  # dataset: one subfolder per class (not tracked)
│   ├── 0001/
│   ├── 0002/
│   └── ...
├── src/
│   ├── preprocessing.py   # filters: median, gaussian, bilateral, average
│   ├── segmentation.py    # thresholding + line/word/char segmentation
│   ├── features.py        # DWT + moment feature extraction
│   ├── train_svm.py       # SVM training
│   ├── train_cnn.py       # CNN training
│   └── gui.py             # Tkinter GUI
├── models/                # saved CNN / SVM models
├── samples/               # example input documents
├── requirements.txt
└── README.md
```
>>>>>>> 5e34aa9ef941a5625cc311d5f7cb6e81e0b1db71

## Setup

```bash
<<<<<<< HEAD
git clone https://github.com/jadejapratiksha/Optical-Character-Recognition.git

cd Optical-Character-Recognition

pip install -r requirements.txt
```

---

## Usage

Launch the GUI application:
=======
# 1. Clone
git clone https://github.com/jadejapratiksha/<repo-name>.git
cd <repo-name>

# 2. (Recommended) create a conda environment
conda create -n sanskrit-ocr python=3.8
conda activate sanskrit-ocr

# 3. Install dependencies
pip install -r requirements.txt
```

Example `requirements.txt`:

```
numpy
opencv-python
scikit-learn
tensorflow
PyWavelets
matplotlib
Pillow
```

## Usage

Launch the GUI:
>>>>>>> 5e34aa9ef941a5625cc311d5f7cb6e81e0b1db71

```bash
python src/gui.py
```

<<<<<<< HEAD
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
=======
The GUI provides the following actions:

- **Train** — trains the classifier and plots model accuracy / loss curves.
- **Browse Image** — select a scanned Sanskrit document to digitize.
- **Segment** — show the segmented and filtered text.
- **Recognize** — recognize letters, words, and sentences.
- **Write Text** — export the recognized text to an editable `.txt` file.
- **Accuracy** — display the current model accuracy.
- **Recognize No. Entity** — extract numeric entities from the document.

## Publications

This work was published in:

- *A Review: Character Recognition and Digitization of Sanskrit Characters* — Journal of The Gujarat Research Society (JGRS), Vol. 21, Issue 13, December 2019.
- *Machine Learning and Deep Learning Approaches for Sanskrit Character Recognition* — Journal of Xidian University, Vol. 14, Issue 05, May 2020.
>>>>>>> 5e34aa9ef941a5625cc311d5f7cb6e81e0b1db71

## Author

**Pratiksha Jadeja**
<<<<<<< HEAD

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
=======
M.E. Embedded Systems — SVIT, Gujarat Technological University
GitHub: [@jadejapratiksha](https://github.com/jadejapratiksha)

Guided by Mr. Saurabh M. Patel, Assistant Professor, E&C Department, SVIT.

## Acknowledgements

Built on prior research in Sanskrit/Devanagari OCR, including Avadesh & Goyal (CNN-based Sanskrit OCR, DAS 2018) and related work in segmentation, feature extraction, and soft-computing classifiers cited in the thesis.

## License

No license is specified yet. Add a `LICENSE` file (for example, the MIT License) if you want others to reuse this code.
>>>>>>> 5e34aa9ef941a5625cc311d5f7cb6e81e0b1db71
