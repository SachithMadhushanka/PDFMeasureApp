import fitz
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader

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

    def select_file(self):
        self.filepath = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])

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

root = tk.Tk()
app = PDFMeasureApp(root)
root.mainloop()
