import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Configure Tesseract executable path if needed
# Uncomment the following line and set the path to your Tesseract installation if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to process the image and extract text
def extract_text_from_image(image):
    # Convert the image to grayscale for better OCR performance
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    
    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(gray_image)
    
    return extracted_text

# Function to draw text overlay on the image
def draw_text_on_image(image, text):
    # Create a copy of the original image
    overlay_image = image.copy()

    # Define position and font for the overlay text
    position = (10, 30)  # Position for overlay text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 0, 0)  # Red color for the overlay
    thickness = 2

    # Add text overlay
    cv2.putText(overlay_image, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

    return overlay_image

# Streamlit app layout
st.title("Augmented Reality with OCR")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text from the image
    if st.button("Extract Text"):
        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_image(image)
            overlay_image = draw_text_on_image(np.array(image), extracted_text)

            st.success("Text extraction complete!")
            st.image(overlay_image, caption="Image with Extracted Text Overlay", use_column_width=True)
            st.text_area("Extracted Text", extracted_text, height=200)

# Note: The following line is not needed in Streamlit apps
# if __name__ == "__main__":
#     st.run()
