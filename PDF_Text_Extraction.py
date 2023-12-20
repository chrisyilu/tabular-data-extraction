import pytesseract  # OCR
from pdf2image import convert_from_path


def pdf_to_images(pdf_path):
    # convert PDF to a list of images
    images = convert_from_path(pdf_path)
    return images


def extract_text_from_image(image):
    # use OCR to extract text from the image
    text = pytesseract.image_to_string(image)
    return text
