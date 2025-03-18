import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_folder, output_pdf):

    try:
        if not os.path.exists(pdf_folder):
            print(f"Error: The folder '{pdf_folder}' does not exist.")
            return

        if not os.path.isdir(pdf_folder):
            print(f"Error: '{pdf_folder}' is not a valid directory.")
            return

        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
        pdf_files.sort() 
        
        if not pdf_files:
            print("No PDF files found in the folder.")
            return

        merger = PdfMerger()
        for pdf in pdf_files:
            try:
                merger.append(os.path.join(pdf_folder, pdf))
                print(f"Added: {pdf}")
            except Exception as e:
                print(f"Error adding {pdf}: {e}")

        output_pdf = os.path.abspath(output_pdf) 
        merger.write(output_pdf)
        merger.close()
        print(f"Merged PDF saved as: {output_pdf}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder containing PDFs: ").strip()
    output_file = input("Enter the output PDF file name (including .pdf): ").strip()
    
    if not output_file.lower().endswith(".pdf"):
        print("Error: Output file name must end with '.pdf'.")
    else:
        merge_pdfs(folder_path, output_file)
