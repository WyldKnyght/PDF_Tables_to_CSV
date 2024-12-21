# src\controllers\pdf_modules\select_pdf.py
from tkinter import filedialog
from typing import Optional
from utils.custom_logging import logger


class PDFSelector:
    """Handles selecting a PDF file through a file dialog."""

    def __init__(self, ui: object) -> None:
        self.ui = ui

    def select_pdf(self) -> Optional[str]:
        """
        Opens a file dialog for the user to select a PDF file.

        Returns:
            Optional[str]: The path to the selected PDF file, or None if no file was selected.
        """
        logger.info("Selecting a PDF file...")
        
        try:
            file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if not file_path:
                logger.warning("No file selected.")
                self.ui.show_message("No PDF file selected.")
                return None
            
            self.ui.file_label.config(text=f"Selected file: {file_path}")
            logger.info(f"Selected PDF file: {file_path}")
            return file_path
        
        except Exception as e:
            logger.error(f"Error selecting PDF file: {e}")
            self.ui.show_message(f"An error occurred while selecting a PDF: {e}")
            return None
