import camelot
import pandas as pd

def extract_tables(pdf_path):

    tables = camelot.read_pdf(
        pdf_path,
        pages="all",
        flavor="lattice"  # better for bordered tables
    )

    dfs = []

    for table in tables:
        df = table.df
        dfs.append(df)

    return dfs