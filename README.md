# PDF Measurement Application

## Overview

The PDF Measurement Application is a simple tool to measure and display the number of pages and the dimensions of each page in a selected PDF file. This application is built using Python and leverages the `PyPDF2` library to read PDF files and `PyMuPDF` (also known as `fitz`) to measure the dimensions of the pages.

## Features

- Select a PDF file to measure.
- Measure the number of pages in the PDF.
- Measure the width and height of each page in pixels.
- Display the results in a user-friendly message box.

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- PyPDF2
- PyMuPDF (fitz)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-measurement-app.git
   cd pdf-measurement-app
   ```

2. **Install the required Python packages:**
   ```bash
   pip install PyPDF2 PyMuPDF
   ```

## Usage

1. **Run the application:**
   ```bash
   python pdf_measure_app.py
   ```

2. **Use the application:**
   - Click the "Select File" button to choose a PDF file.
   - Click the "Measure" button to start measuring the selected PDF file.
   - The application will display the number of pages and the dimensions of each page in a message box.

## Script Explanation

### Importing Libraries
```python
import fitz
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
```
- **fitz**: Used to measure the dimensions of each page.
- **tkinter**: Used for the graphical user interface.
- **filedialog** and **messagebox**: Used for file selection and displaying messages.
- **PyPDF2**: Used to read the PDF and get the number of pages.

### PDFMeasureApp Class
#### Initialization
```python
class PDFMeasureApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Measurement")

        self.label = tk.Label(master, text="Select a PDF file to measure:")
        self.label.pack()

        self.button = tk.Button(master, text="Select File", command=self.select_file)
        self.button.pack()

        self.measure_button = tk.Button(master, text="Measure", command=self.measure)
        self.measure_button.pack()

        self.filepath = None
```
- Initializes the main window with a title, label, and buttons for file selection and measurement.

#### File Selection
```python
def select_file(self):
    self.filepath = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
```
- Opens a file dialog to select a PDF file and stores the selected file path.

#### Measuring Pages and Dimensions
```python
def measure(self):
    if not self.filepath:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    try:
        # Measure number of pages
        with open(self.filepath, 'rb') as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)

        dimensions_info = []
        # Measure dimensions of each page
        pdf_document = fitz.open(self.filepath)

        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            page_dimension = page.bound()
            width = page_dimension[2] - page_dimension[0]  # Calculate width
            height = page_dimension[3] - page_dimension[1]  # Calculate height
            dimensions_info.append((page_num + 1, width, height))

        pdf_document.close()

        # Display dimensions info
        messagebox.showinfo("Measurement Complete", f"PDF Measurement Complete!\n\nTotal Pages: {num_pages}\n\nPage Dimensions (pixels):\n{dimensions_info}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
```
- Checks if a file is selected. If not, shows an error message.
- Reads the PDF file to get the number of pages using `PyPDF2`.
- Uses `fitz` to open the PDF and measure the dimensions of each page.
- Displays the number of pages and the dimensions of each page in a message box.

### Main Loop
```python
root = tk.Tk()
app = PDFMeasureApp(root)
root.mainloop()
```
- Creates the main application window and starts the Tkinter event loop.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
