import pytesseract
import cv2
from pdf2image import convert_from_path
import pandas as pd

def ocr_pdf(pdf_path):

    images = convert_from_path(pdf_path)

    tables = []

    for img in images:

        img = cv2.cvtColor(
            cv2.array(img),
            cv2.COLOR_BGR2GRAY
        )

        text = pytesseract.image_to_string(img)

        rows = text.split("\n")

        data = [row.split() for row in rows if row]

        if data:
            df = pd.DataFrame(data)
            tables.append(df)

    return tables