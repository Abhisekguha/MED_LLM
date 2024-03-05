import easyocr

def ocr_from_image(input_file):
    try:
        # Initialize the OCR reader
        reader = easyocr.Reader(['en'])  # Specify the languages to use (e.g., English)

        # Perform OCR on the image
        result = reader.readtext(input_file)

        # Extract the text from the OCR result
        text = ' '.join([entry[1] for entry in result])
        return text
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
input_file = r'path_name.jpg'
text = ocr_from_image(input_file)
if text:
    print("Extracted Text:")
    print(text)
else:
    print("OCR failed to extract text from the image.")
