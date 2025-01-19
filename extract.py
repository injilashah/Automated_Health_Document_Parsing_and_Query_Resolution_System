import fitz  # PyMuPDF
from paddleocr import PaddleOCR
import numpy as np
from PIL import Image

def extract_text_from_pdf(pdf_path):
    # Initialize PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # You can adjust language and settings here

    doc = fitz.open(pdf_path)  # Open the PDF with PyMuPDF
    extracted_text = ""

    # Iterate over each page and convert it to an image
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)

        # Convert the page to an image (pixmap object)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Create an image from the pixmap

        # Convert the image to a numpy array for PaddleOCR
        image_np = np.array(img)
        
        # Apply PaddleOCR to the image
        result = ocr.ocr(image_np, cls=True)

        # Extract text from the OCR result
        for line in result[0]:
            extracted_text += line[1][0] + "\n"  # Append the recognized text

    return extracted_text

