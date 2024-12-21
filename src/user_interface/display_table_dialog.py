# src/user_interface/display_table_dialog.py
import tkinter as tk
from typing import List, Dict, Optional
import pandas as pd
from utils.custom_logging import error_handler, logger


@error_handler
def display_table_selection(tables: List[pd.DataFrame]) -> Optional[Dict[str, List[pd.DataFrame]]]:
    logger.info("Displaying and selecting tables...")
    """High-level function to extract tables from a PDF and display them for selection.

    Args:
        tables (List[pandas.DataFrame]): The list of DataFrames to display and select from.

    Returns:
        Optional[Dict[str, List[pd.DataFrame]]]: A dictionary containing extracted tables and selected indices.
        Example: {"tables": [DataFrame1, DataFrame2], "indices": [0, 2]}
        Returns None if no selection is made.
    """
    if not tables:
        raise ValueError("No tables were provided for selection.")

    # Create selection window
    selection_window = tk.Toplevel()
    selection_window.title("Select Tables")
    selection_window.geometry("1280x600")

    # Create frame for content
    border_frame = tk.Frame(selection_window, padx=10, pady=10)
    border_frame.pack(expand=True, fill=tk.BOTH)

    # Create scrollable canvas
    canvas = tk.Canvas(border_frame)
    scrollbar = tk.Scrollbar(border_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    table_vars = []  # To store BooleanVars for checkboxes

    # Dynamically create widgets for each table with limited preview rows
    for i, table in enumerate(tables):
        var = tk.BooleanVar(value=True)  # Default to selected
        table_vars.append(var)

        frame = tk.Frame(scrollable_frame)  # Frame for each table's widgets
        frame.pack(fill=tk.X, padx=5, pady=5)  # Add padding for spacing

        # Checkbox to select/deselect the table
        checkbox = tk.Checkbutton(frame, text=f"Table {i + 1}", variable=var)
        checkbox.pack(side=tk.LEFT)

        # Button to expand/collapse the preview
        expand_button = tk.Button(frame, text="+", command=lambda f=frame: toggle_preview(f))
        expand_button.pack(side=tk.LEFT)

        # Text widget to display a preview of the table (collapsed by default)
        preview_text = tk.Text(frame, height=5, width=80)  # Start with height showing some rows (e.g., 5)
        preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Allow it to expand

        frame.preview_text = preview_text
        frame.is_expanded = False  # Track whether the preview is expanded or collapsed

        try:
            # Display the first few rows of the table as a string
            preview_content = table.head(5).to_string(index=False)  # Show only first 5 rows initially
            preview_text.insert(tk.END, preview_content)
            preview_text.config(state=tk.DISABLED)  # Make it read-only
        except Exception as e:
            preview_text.insert(tk.END, f"Error displaying table: {e}")
            preview_text.config(state=tk.DISABLED)

    @error_handler
    def toggle_preview(frame: tk.Frame) -> None:
        """
        Toggles the preview of a table on and off.

        Args:
            frame (tk.Frame): The frame containing the table preview widgets.
        """
        if frame.is_expanded:
            frame.preview_text.pack_forget()  # Hide the text widget
            frame.is_expanded = False
            frame.children['!button'].config(text="+")  # Change button text to "+"
            frame.preview_text.config(height=0)  # Reset height to collapsed state
        else:
            frame.preview_text.config(height=10)  # Expand to show more rows (e.g., 10)
            frame.preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Show the text widget
            frame.is_expanded = True
            frame.children['!button'].config(text="-")  # Change button text to "-"

    @error_handler
    def on_select() -> None:
        """
        Collects indices of selected tables and closes the dialog.
        
        Returns:
            None: The selected indices are returned when `wait_window` ends.
        """
        nonlocal selected_tables
        
        selected_tables = [i for i,var in enumerate(table_vars )if var.get()]
        
        selection_window.destroy()  # Close dialog after selection

    selected_tables: List[int] = []  # Store selected indices

    button_frame = tk.Frame(border_frame)
    button_frame.pack(side=tk.BOTTOM, pady=(10, 0))  # Add padding at the bottom

    select_button = tk.Button(button_frame, text="Confirm Selection", command=on_select)
    select_button.pack()  # Centered in button_frame by default

    selection_window.wait_window()  # Wait until the window is closed

    return selected_tables
