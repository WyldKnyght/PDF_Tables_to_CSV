# src/controllers/pdf_modules/pdf_workflow.py
from typing import Optional, Dict
from .data_consolidater import DataConsolidater
from .pre_processor import PreProcessor
from .save_tables_to_csv import save_tables_to_csv
from utils.custom_logging import logger

class PDFWorkflow:
    """Class to encapsulate the PDF processing workflow."""

    def __init__(self, ui: object):
        self.ui = ui
        self.data_consolidater = DataConsolidater(ui)
        self.pre_processor = PreProcessor(ui)

    def start_pdf_processing(self) -> None:
        logger.info("Starting PDF processing workflow...")
        self.ui.show_loading_indicator("Processing...")
        try:
            self.process_pdf()
        finally:
            self.ui.hide_loading_indicator()

    def process_pdf(self) -> Optional[Dict[str, object]]:
        logger.info("Processing PDF...")

        # Step 1: Data Consolidation
        pdf_path = self.data_consolidater.select_file()
        if not pdf_path:
            return self.log_and_notify("No file selected by user.", "No file selected.")
        
        try:
            tables = self.data_consolidater.extract_tables(pdf_path)
            if not tables:
                return self.log_and_notify("No tables found in the selected PDF.", "No tables were found.")
            logger.info(f"Extracted {len(tables)} tables from the PDF.")
        except Exception as e:
            return self.log_and_notify(f"Error extracting tables: {str(e)}", "An error occurred while extracting tables.")

        selected_tables = self.data_consolidater.select_tables(tables)
        if not selected_tables:
            return self.log_and_notify("No tables selected by user.", "No tables were selected.")

        # Step 2: Pre-process and reset the index
        try:
            pre_processed_tables = self.pre_processor.pre_process_tables(selected_tables)
            logger.info("Tables pre-processed")
        except Exception as e:
            return self.log_and_notify(f"Error pre-processing tables: {str(e)}", "An error occurred while pre-processing.")

        # Final Step: Save standardized tables to CSV
        saved_file_path = save_tables_to_csv(pre_processed_tables, pdf_path)
        
        self.ui.show_message(f"Tables saved successfully at: {saved_file_path}")
        
        return {"tables": pre_processed_tables, "path": saved_file_path}

    def log_and_notify(self, log_message: str, user_message: str) -> None:
        logger.warning(log_message)
        self.ui.show_message(user_message)
