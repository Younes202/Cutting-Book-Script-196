import fitz  # PyMuPDF

# Input PDF file name and number of pages per split
input_pdf_file = 'FAST-API.pdf'  # Replace with your actual file name
pages_per_split = 5

# Open the input PDF file
pdf_document = fitz.open(input_pdf_file)
total_pages = len(pdf_document)

# Calculate the number of splits
num_splits = total_pages // pages_per_split + (total_pages % pages_per_split > 0)

# Iterate through the splits
for split_num in range(num_splits):
    # Determine the page range for this split
    start_page = split_num * pages_per_split
    end_page = min((split_num + 1) * pages_per_split, total_pages)

    # Create a new PDF with the selected pages
    output_pdf = fitz.open()

    for page_num in range(start_page, end_page):
        output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    # Save the split PDF to a new file
    output_pdf_file = f'{split_num * pages_per_split + 1}-{end_page}.pdf'
    output_pdf.save(output_pdf_file)

    print(f'Saved {output_pdf_file}')

pdf_document.close()
print('Splitting and renaming complete.')

