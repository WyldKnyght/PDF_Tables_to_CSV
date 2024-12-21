# src\controllers\pdf_modules\display_tables_from_pdf.py
from typing import List
import pandas as pd
from user_interface.display_table_dialog import display_table_selection
from utils.custom_logging import logger


def display_tables(tables: List[pd.DataFrame]) -> None:
    """
    Displays extracted tables in a dialog for user preview.

    Args:
        tables (List[pd.DataFrame]): A list of DataFrames representing extracted tables.
    """
    logger.info("Displaying extracted tables...")
    display_table_selection(tables)
