# src/controllers/pdf_modules/extract_tables_from_pdf.py
import tabula
from typing import List
import pandas as pd
from utils.custom_logging import logger, error_handler


@error_handler
def extract_tables_from_pdf(file_path: str, pages: str = 'all') -> List[pd.DataFrame]:
    """
    Extracts tables from a given PDF file.

    Args:
        file_path (str): The path to the PDF file.
        pages (str): Pages to extract tables from (default is 'all').

    Returns:
        List[pd.DataFrame]: A list of DataFrames containing extracted tables.
    """
    logger.info(f"Extracting tables from {file_path}...")
    
    try:
        tables = tabula.read_pdf(file_path, pages=pages, multiple_tables=True)
        
        if not tables or len(tables) == 0:
            logger.warning("No tables found in the provided PDF.")
            return []
        
        logger.info(f"Successfully extracted {len(tables)} table(s).")
        return tables

    except Exception as e:
        logger.error(f"Error during table extraction: {e}")
        raise
