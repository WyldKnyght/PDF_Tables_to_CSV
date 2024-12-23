# src/controllers/pdf_modules/data_consolidater.py
import pandas as pd
import tabula
from tkinter import filedialog
from typing import Optional, List
from user_interface.display_table_dialog import display_table_selection
from utils.custom_logging import logger, error_handler


class DataConsolidater:
    """Combine all extracted dataframes into a single dataframe."""
    
    def __init__(self, ui: object) -> None:
        self.ui = ui

    @error_handler
    def select_file(self) -> Optional[str]:
        """
        Opens a file dialog for the user to select a PDF file.

        Returns:
            Optional[str]: The path to the selected PDF file, or None if no file was selected.
        """
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return None

        self.ui.file_label.config(text=f"Selected file: {file_path}")
        return file_path

    @error_handler
    def extract_tables(self, file_path: str, pages: str = 'all') -> List[pd.DataFrame]:
        """
        Extracts tables from a given PDF file.

        Args:
            file_path (str): The path to the PDF file.
            pages (str): Pages to extract tables from (default is 'all').

        Returns:
            List[pd.DataFrame]: A list of DataFrames containing extracted tables.
        """
        try:
            tables = tabula.read_pdf(file_path, pages=pages, multiple_tables=True)
            return tables or []
        except Exception as e:
            logger.error(f"Error during table extraction: {e}")
            raise

    @error_handler
    def select_tables(self, tables: List[pd.DataFrame]) -> Optional[List[pd.DataFrame]]:
        """
        Allows users to select which extracted tables to keep.

        Args:
            tables (List[pd.DataFrame]): A list of DataFrames representing extracted tables.

        Returns:
            Optional[List[pd.DataFrame]]: A list of selected DataFrames.
        """
        try:
            selected_indices = display_table_selection(tables)
            return [tables[i] for i in selected_indices] if selected_indices else []
        except Exception as e:
            logger.error(f"Error during table selection: {e}")
