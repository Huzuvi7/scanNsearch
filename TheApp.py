import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import re  # Importing the re module for search and highlight functionality
import time

# Function to load the image
def load_image(image_file):
    img = Image.open(image_file)
    return img

# OCR extraction using easyOCR (with Hindi and English support)
@st.cache_data  # Cache the OCR results to avoid re-running OCR
def extract_text(_image, lang):
    reader = easyocr.Reader(lang, gpu=False)
    result = reader.readtext(np.array(_image), detail=0)  # Use numpy array for OCR input
    extracted_text = " ".join([text for text in result])
    return extracted_text

# Page Configuration and Title
st.set_page_config(page_title="OCR & Document Search (Hindi & English)", page_icon="📝", layout="centered")
st.title("📝 OCR and Document Search App")

# Brief description
st.write("Upload an image, extract text using OCR in English or Hindi, and search for specific keywords in the extracted content. Keywords will be highlighted!")

# Language selection
lang_choice = st.selectbox("Select Language for OCR", options=["English", "Hindi"], index=0)

# Set language code for EasyOCR
lang_code = ['en'] if lang_choice == "English" else ['hi']

# File Uploader
image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if image_file is not None:
    img = load_image(image_file)
    
    # Display uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Progress bar and OCR extraction
    progress_bar = st.progress(0)
    
    with st.spinner(f'Performing OCR in {lang_choice}...'):
        time.sleep(0.5)
        progress_bar.progress(30)
        
        # Actual OCR process
        extracted_text = extract_text(img, lang_code)  # Pass the image and language code to the function
        progress_bar.progress(70)
        
        time.sleep(0.5)
        progress_bar.progress(100)
    
    # Display extracted text
    st.subheader("Extracted Text")
    text_area = st.text_area("OCR Output", extracted_text, height=250)

    # Search functionality with highlight
    search_query = st.text_input("🔍 Search in extracted text", "")
    
    if search_query:
        if re.search(re.escape(search_query), extracted_text, re.IGNORECASE):
            st.success(f"Keyword '{search_query}' found!")
            
            # Highlight keyword in extracted text
            highlighted_text = re.sub(re.escape(search_query), f"**{search_query}**", extracted_text, flags=re.IGNORECASE)
            st.markdown(highlighted_text, unsafe_allow_html=True)
        else:
            st.error(f"Keyword '{search_query}' not found.")
    
    st.write("Search for a specific word using the search input.")
    
# Styling the app to look clean and modern
st.markdown("""
    <style>
    .stTextInput, .stTextArea, .stFileUploader {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
    }
    .stTextInput input, .stTextArea textarea {
        font-size: 14px;
        padding: 10px;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
    .stTextArea textarea {
        line-height: 1.6;
    }
    .stButton button {
        background-color: #0073e6;
        color: white;
        padding: 10px 15px;
        font-size: 14px;
        border-radius: 5px;
        border: none;
    }
    .stButton button:hover {
        background-color: #005bb5;
    }
    .stProgressBar > div {
        border-radius: 8px;
    }
    .css-12w0qpk {
        font-size: 14px;
    }
    .css-1aumxhk {
        padding: 10px 15px;
    }
    .uploadedImage {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)
