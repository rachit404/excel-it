import pdfplumber
import pandas as pd

def extract_text_tables(pdf_path):

    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:

            extracted = page.extract_table()

            if extracted:
                df = pd.DataFrame(extracted)
                tables.append(df)

    return tables