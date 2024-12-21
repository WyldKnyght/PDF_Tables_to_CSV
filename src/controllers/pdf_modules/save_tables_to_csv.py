# src/controllers/pdf_modules/save_tables_to_csv.py
import os
import pandas as pd
from typing import List
from utils.custom_logging import logger
from configs.constants import RAW_DATA_DIR

def save_tables_to_csv(tables: List[pd.DataFrame], pdf_path: str) -> str:
    """
    Saves all extracted and selected tables to a CSV file.

    Args:
        tables (List[pd.DataFrame]): A list of DataFrames containing extracted and selected tables.
        pdf_path (str): The path to the original PDF file for naming the output.

    Returns:
        str: The path where the CSV was saved.
    """
    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    csv_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".csv"
    output_path = os.path.join(RAW_DATA_DIR, csv_filename)

    combined_df = pd.concat(tables, ignore_index=True)
    
    combined_df.to_csv(output_path, index=False)
    
    logger.info(f"Tables saved successfully at {output_path}.")
    
    return output_path
