# src/controllers/pdf_modules/pre_processor.py
import pandas as pd
from typing import List


class PreProcessor:
    """Pre-process the combined dataframe."""
    
    def __init__(self, ui: object) -> None:
        self.ui = ui

    def pre_process_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Pre-process a single dataframe by removing blank rows and resetting the index.

        Args:
            df (pd.DataFrame): The input dataframe to pre-process.

        Returns:
            pd.DataFrame: The cleaned dataframe.
        """
        # Step 1: Remove completely blank rows
        df = df.dropna(how="all")

        # Step 2: Reset index for continuity
        df = df.reset_index(drop=True)

        return df

    def pre_process_tables(self, tables: List[pd.DataFrame]) -> List[pd.DataFrame]:
        """
        Pre-process a list of dataframes by removing blank rows and resetting the index.

        Args:
            tables (List[pd.DataFrame]): A list of dataframes to pre-process.

        Returns:
            List[pd.DataFrame]: A list of cleaned dataframes.
        """
        return [self.pre_process_dataframe(table) for table in tables]
