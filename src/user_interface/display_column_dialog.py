# src/user_interface/display_column_dialog.py
import tkinter as tk
from typing import List
from utils.custom_logging import error_handler, logger

@error_handler
def display_column_confirmation(column_names: List[List[str]]) -> List[List[str]]:
    """
    Display a dialog for confirming or renaming column names.

    Args:
        column_names (List[List[str]]): The list of column names.

    Returns:
        List[List[str]]: A list of confirmed or renamed column names.
    """
    logger.info("Displaying column confirmation dialog...")

    # Setup dialog window
    confirmation_window = tk.Toplevel()
    confirmation_window.title("Confirm Column Names")
    confirmation_window.geometry("800x600")

    # Create scrollable frame
    canvas = tk.Canvas(confirmation_window)
    scrollbar = tk.Scrollbar(confirmation_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Instructions for the user
    instructions = tk.Label(scrollable_frame, text="Please select a column name for each table (only one selection per column name across all tables):", wraplength=700)
    instructions.pack(pady=10)

    # Radiobutton variables for global uniqueness
    selected_columns = {}
    all_columns = {col for table in column_names for col in table}  # All unique column names
    column_selection_vars = {col: tk.IntVar(value=0) for col in all_columns}  # 0 means unselected

    # Store selected names per table
    table_selections = []

    # Create widgets for each table
    for table_idx, table_columns in enumerate(column_names):
        table_label = tk.Label(scrollable_frame, text=f"Table {table_idx + 1} Columns:")
        table_label.pack(anchor="w", pady=5)

        # List to store the selection for this table
        table_selection = tk.StringVar(value="")  # Holds the selected column name for this table
        table_selections.append(table_selection)

        for col_idx, col in enumerate(table_columns):
            frame = tk.Frame(scrollable_frame)
            frame.pack(fill=tk.X, padx=5, pady=2)

            # Radiobutton for selecting the column
            rb = tk.Radiobutton(
                frame,
                text=col,
                variable=table_selection,
                value=col,
                command=lambda c=col: update_column_selection(c, column_selection_vars, table_selections)
            )
            rb.pack(anchor="w")

    # Update column selection to enforce uniqueness
    def update_column_selection(selected, column_vars, table_vars):
        """
        Enforce unique column selection across all tables.

        Args:
            selected (str): The selected column name.
            column_vars (dict): Dictionary of column selection variables.
            table_vars (list): List of StringVars for each table's selection.
        """
        # Mark all instances of the selected column as selected (1) and disable them
        for col, var in column_vars.items():
            if col == selected:
                var.set(1)  # Mark as selected
            else:
                # If any other column is selected elsewhere, ensure it remains active
                var.set(0)
        
        # Update the enabled state of all radiobuttons
        for table_var in table_vars:
            if table_var.get() != selected:
                table_var.set("")  # Reset conflicting selections

    # Confirmation button
    def on_confirm():
        nonlocal selected_columns
        # Gather selected column names for each table
        selected_columns = [table_selection.get() for table_selection in table_selections]
        confirmation_window.destroy()

    confirm_button = tk.Button(confirmation_window, text="Confirm Column Names", command=on_confirm)
    confirm_button.pack(side=tk.BOTTOM, pady=10)

    selected_columns = []  # To store the final column selections

    confirmation_window.wait_window()  # Wait until the window is closed

    return selected_columns
