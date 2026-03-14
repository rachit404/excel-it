from src.extract_tables import extract_tables
from src.pdf_utils import extract_text_tables
from src.ocr_pipeline import ocr_pdf
from src.export_excel import export_tables


PDF_FILE = "input/ticket.pdf"
OUTPUT_FILE = "output/result.xlsx"


def run_pipeline():

    tables = extract_tables(PDF_FILE)

    if not tables:
        tables = extract_text_tables(PDF_FILE)

    if not tables:
        tables = ocr_pdf(PDF_FILE)

    export_tables(tables, OUTPUT_FILE)

    print("Conversion completed")


if __name__ == "__main__":
    run_pipeline()