import fitz  # PyMuPDF
import os  # Import the os module for file counting

# Input PDF file name and number of pages per split
input_pdf_file = 'FAST-API.pdf'  # Replace with your actual file name
pages_per_split = 5

# Open the input PDF file
pdf_document = fitz.open(input_pdf_file)
total_pages = len(pdf_document)

# Calculate the number of splits
num_splits = total_pages // pages_per_split + (total_pages % pages_per_split > 0)

# List to store the generated file names
generated_files = []

# Iterate through the splits
for split_num in range(num_splits):
    # Determine the page range for this split
    start_page = split_num * pages_per_split + 1
    end_page = min((split_num + 1) * pages_per_split, total_pages)

    # Create a new PDF with the selected pages
    output_pdf = fitz.open()

    for page_num in range(start_page - 1, end_page):
        output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    # Zero-pad the split number for consistent file names (e.g., 001-005.pdf)
    split_num_str = str(split_num + 1).zfill(len(str(num_splits)))

    # Save the split PDF to a new file with zero-padded name
    output_pdf_file = f'{split_num_str}-{end_page}.pdf'
    output_pdf.save(output_pdf_file)

    generated_files.append(output_pdf_file)
    print(f'Saved {output_pdf_file}')

pdf_document.close()
print('Splitting and renaming complete.')

# Calculate the number of generated files
num_generated_files = len(generated_files)
print(f'Total number of generated files: {num_generated_files}')

