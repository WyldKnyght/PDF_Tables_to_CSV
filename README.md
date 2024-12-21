# PDF Tables to CSV

## Overview

PDF Tables to CSV is a Python application designed for **local** extraction of tables from PDF files and saving them as CSV files. 

This application allows users to work with sensitive data without the risk of exposing personal information online, ensuring complete privacy and security.

## Features

- **Local Processing**: All operations are performed locally on your machine, eliminating the risk of data leaks associated with online services.
- **PDF Selection**: Easily select PDF files through a user-friendly file dialog.
- **Table Extraction**: Automatically extract tables from the selected PDF files.
- **Table Preview**: View extracted tables and select which ones to keep before saving.
- **CSV Export**: Save selected tables as CSV files in a user-defined output directory.

## Requirements

To run this application, you need the following:

- Python 3.x
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/wyldknyght/PDF_Tables_to_CSV.git
   cd PDF_Tables_to_CSV
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Locate the `.env_temp` file in the root directory.
   - Create a copy of this file and rename it to `.env`.
   - Open the `.env` file and replace `ADD_YOUR_PATH_HERE` with the actual path to your project root.

   Note: The `.env` file is crucial for the application to function correctly. Make sure to set it up properly before running the application.

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. In the application window:
   - Click on "Select PDF" to choose your PDF file.
   - The application will extract tables from the PDF and display them for selection.
   - Review the extracted tables and select the ones you want to save.
   - Confirm your selection of tables.

3. The application will automatically save the CSV file:
   - Default location: `docs/cleaned_data/{original_pdf_name}.csv`
   - This path is relative to the PROJECT_ROOT specified in your `.env` file.

    Note: If you want to change the save location, you need to update the CLEANED_DATA_PATH in your `.env` file. After changing the .env file, restart the application for the changes to take effect.

## Configuration

You can configure various settings in `src/configs/constants.py`:

- `WINDOW_TITLE`: Title of the application window.
- `WINDOW_SIZE`: Size of the application window.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tabula](https://github.com/chezou/tabula-py): For table extraction from PDFs.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): For building the GUI.
