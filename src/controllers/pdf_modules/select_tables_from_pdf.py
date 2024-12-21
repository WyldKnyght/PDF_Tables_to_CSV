# src/controllers/pdf_modules/select_tables_from_pdf.py
from typing import Optional, List
import pandas as pd
from user_interface.display_table_dialog import display_table_selection
from utils.custom_logging import logger

def select_tables(tables: List[pd.DataFrame]) -> Optional[List[pd.DataFrame]]:
    """
    Allows users to select which extracted tables to keep.

    Args:
        tables (List[pd.DataFrame]): A list of DataFrames representing extracted tables.

    Returns:
        Optional[List[pd.DataFrame]]: A list of selected DataFrames.
    """
    logger.info("Displaying and selecting tables...")

    try:
        selected_indices = display_table_selection(tables)
        
        if not selected_indices:
            logger.warning("No tables were selected by the user.")
            return []
        
        return [tables[i] for i in selected_indices]

    except Exception as e:
        logger.error(f"Error during table selection: {e}")
        return None
