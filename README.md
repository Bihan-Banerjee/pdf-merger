# PDF Merger

## Description
This Python script merges all PDF files in a specified folder into a single PDF. It automatically sorts the PDFs alphabetically before merging and provides error handling for missing or invalid directories.

## Features
- Merges all PDFs in a folder into one file
- Automatically sorts PDFs alphabetically before merging
- Error handling for missing folders, invalid directories, and non-PDF files

## Prerequisites
Ensure you have Python installed along with the required library:

```sh
pip install pypdf2
```

## Usage
1. Clone the repository or download the script.
2. Run the script:

```sh
python merge_pdfs.py
```

3. Enter the folder path containing the PDFs.
4. Provide the output file name (must end with `.pdf`).
5. The merged PDF will be saved in the specified location.

## Example
```
Enter the folder containing PDFs: /path/to/pdfs
Enter the output PDF file name (including .pdf): merged_output.pdf
Merged PDF saved as: /absolute/path/to/merged_output.pdf
```

## Error Handling
- If the folder does not exist, the script will notify you.
- If no PDFs are found, it will display an appropriate message.
- If an invalid file name is entered, an error message will be shown.
