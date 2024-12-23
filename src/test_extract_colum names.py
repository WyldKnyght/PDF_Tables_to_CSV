from controllers.pdf_modules.column_standardizer import ColumnStandardizer

# Initialize column standardizer
standardizer = ColumnStandardizer(ui=None)

# Extract column names
pdf_path = r"M:\dev_env\PDF_Tables_to_CSV\.myfiles\Sample_PDF.pdf"
extracted_columns = standardizer.extract_column_names(pdf_path)

# Print results
print("\nExtracted Column Names:")
for i, columns in enumerate(extracted_columns, start=1):
    print(f"Page {i}: {columns}")
