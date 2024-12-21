# src\controllers\pdf_manager.py
from typing import Optional, Dict
from .pdf_modules.select_pdf import PDFSelector
from .pdf_modules.extract_tables_from_pdf import extract_tables_from_pdf
from .pdf_modules.select_tables_from_pdf import select_tables
from .pdf_modules.save_tables_to_csv import save_tables_to_csv
from utils.custom_logging import logger


class PDFManager:
    """Thin wrapper to orchestrate PDF processing by delegating tasks to modules."""

    def __init__(self, ui: object) -> None:
        """
        Initializes the PDFManager with a UI object.

        Args:
            ui (object): The UI interface for user interaction.
        """
        self.ui = ui

    def start_pdf_processing(self) -> None:
        """Start the PDF processing workflow."""
        logger.info("Starting PDF processing workflow...")
        self.ui.show_loading_indicator("Processing...")
        try:
            self.process_pdf()
        finally:
            self.ui.hide_loading_indicator()

    def process_pdf(self) -> Optional[Dict[str, object]]:
        logger.info("Processing PDF...")

        # Step 1: Select a PDF file
        pdf_selector = PDFSelector(self.ui)
        pdf_path = pdf_selector.select_pdf()
        if not pdf_path:
            logger.warning("No file selected by user.")
            return None

        # Step 2: Extract tables from the selected PDF
        tables = extract_tables_from_pdf(pdf_path)
        if not tables:
            return self.log_and_notify(
                "No tables found in the selected PDF.",
                "No tables were found in the selected PDF.",
            )
        
        # Step 3: Display tables and allow user selection
        selected_tables = select_tables(tables)  # This function now handles both display and selection
        if not selected_tables:
            return self.log_and_notify(
                "No tables selected by user.", "No tables were selected."
            )
        
        # Step 4: Save selected tables to CSV
        saved_file_path = save_tables_to_csv(selected_tables, pdf_path)

        self.ui.show_message(f"Tables saved successfully at: {saved_file_path}")

        return {"tables": selected_tables, "path": saved_file_path}


    def log_and_notify(self, log_message: str, user_message: str) -> None:
        """
        Logs a warning message and displays a notification to the user.

        Args:
            log_message (str): The message to log as a warning.
            user_message (str): The message to display to the user.
        
        Returns:
            None
        """
        logger.warning(log_message)
        self.ui.show_message(user_message)
