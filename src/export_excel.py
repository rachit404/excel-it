import pandas as pd

def export_tables(dfs, output_file):

    writer = pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    )

    for i, df in enumerate(dfs):

        sheet = f"Table_{i+1}"

        df.to_excel(
            writer,
            sheet_name=sheet,
            index=False
        )

    writer.close()