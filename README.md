# 📊 Excel-It

Convert PDF documents to Excel spreadsheets with ease. **Excel-It** intelligently extracts tables and text from PDFs using advanced table detection and OCR capabilities.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

## ✨ Features

- 🎯 **Smart Table Detection** - Automatically extracts tables from PDF documents
- 📄 **Multi-Method Extraction** - Uses camelot, pdfplumber, and OCR for maximum compatibility
- 🔄 **Fallback Pipeline** - Seamlessly switches between extraction methods if one fails
- 📊 **Excel Export** - Converts extracted tables to formatted Excel spreadsheets
- 🚀 **Easy to Use** - Simple API with minimal configuration required

## 🛠️ Tech Stack

- **PDF Processing**: Camelot, pdfplumber
- **OCR**: Tesseract, pytesseract
- **Data Processing**: Pandas
- **Excel Export**: openpyxl
- **Image Processing**: OpenCV, Pillow

## 📋 Requirements

Before installation, ensure you have:
- **Python 3.8 or higher**
- **Tesseract OCR** (for OCR functionality)

### Installing Tesseract OCR

#### Windows
1. Download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer and follow the setup wizard
3. Note the installation path (default: `C:\Program Files\Tesseract-OCR`)

#### macOS
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rachit404/excel-it.git
   cd excel-it
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Tesseract path** (Windows only)
   
   If you installed Tesseract to a non-default location, edit `main.py` and add:
   ```python
   import pytesseract
   pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

## 📖 Quick Start

### Basic Usage

1. **Place your PDF file** in the `input/` folder
2. **Update the filename** in `main.py`:
   ```python
   PDF_FILE = "input/your_file.pdf"
   ```
3. **Run the script**:
   ```bash
   python main.py
   ```
4. **Find your Excel file** in the `output/` folder

### Example

```python
from src.extract_tables import extract_tables
from src.export_excel import export_tables

# Extract tables from PDF
tables = extract_tables("input/document.pdf")

# Export to Excel
export_tables(tables, "output/result.xlsx")
```

## 📁 Project Structure

```
excel-it/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── input/                 # Place PDF files here
├── output/                # Extracted Excel files saved here
└── src/
    ├── extract_tables.py   # Table extraction module
    ├── pdf_utils.py        # PDF utility functions
    ├── ocr_pipeline.py     # OCR processing pipeline
    └── export_excel.py     # Excel export functionality
```

## 🔍 How It Works

Excel-It uses a **three-tier extraction pipeline**:

1. **Camelot-Based Detection** - First attempts to extract tables using advanced table detection
2. **Text-Based Extraction** - Falls back to pdfplumber for text-based PDFs
3. **OCR Processing** - Uses Tesseract OCR as a final fallback for scanned documents

This ensures maximum compatibility with various PDF formats and quality.

## ⚙️ Troubleshooting

### "pytesseract.TesseractNotFoundError"
- **Windows**: Verify Tesseract is installed and update the path in `main.py`
- **macOS/Linux**: Run `which tesseract` to verify installation

### "No tables found"
- Ensure your PDF contains structured tables
- Check PDF file format and quality
- For scanned PDFs, OCR will be used automatically

### Module import errors
- Verify virtual environment is activated
- Run `pip install -r requirements.txt` again

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 📧 Support

For issues, questions, or feedback, please open an issue on GitHub.

---

**Made with ❤️ by [rachit404](https://github.com/rachit404)**