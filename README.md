# Augmented Reality with OCR

## Project Description
This project implements an augmented reality system using Optical Character Recognition (OCR) to extract and overlay text from images. Users can upload images, extract text with Tesseract OCR, and view the text overlaid on the original image, simulating an augmented reality experience.

Features:
- **Image Upload**: Users can upload images in JPG, JPEG, or PNG formats for processing.
- **Text Extraction**: Tesseract OCR is used to extract text from the uploaded images, improving accuracy by converting the image to grayscale.
- **Text Overlay**: The extracted text is visually overlaid on the image, providing an augmented view.
- **User-Friendly Interface**: The application is built with Streamlit, allowing users to easily upload images and extract text.

## Installation Instructions
To set up the project locally, clone the repository and install the required packages:

```bash 
git clone git@github.com:haroon423/augmented-reality-ocr.git
cd augmented-reality-ocr
pip install -r requirements.txt
streamlit run app.py