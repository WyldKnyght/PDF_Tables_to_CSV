# src/user_interface/main_window.py
import tkinter as tk
from controllers.pdf_manager import PDFManager
from utils.custom_logging import logger, error_handler
from configs.constants import WINDOW_TITLE, WINDOW_SIZE


class PDFExtractorUI:
    """Main UI class for the PDF Table Extractor application."""

    def __init__(self) -> None:
        """Initialize the main application window."""
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.loading_label = None  # Placeholder for loading indicator
        self.pdf_manager = PDFManager(self)  # Initialize the controller
        self.setup_main_window()

    @error_handler
    def setup_main_window(self) -> None:
        """Set up the main window components."""
        logger.info("Setting up main window...")
        
        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        # Button to start PDF processing
        select_pdf_button = tk.Button(button_frame, text="Select PDF", command=self.pdf_manager.start_pdf_processing)
        select_pdf_button.pack(side=tk.LEFT, padx=10)

        # Button to close the application
        close_button = tk.Button(button_frame, text="Close", command=self.close_app)
        close_button.pack(side=tk.LEFT, padx=10)

        # Label to display selected file path
        self.file_label = tk.Label(self.root, text="No file selected")
        self.file_label.pack(pady=10)

        # Text box for messages and status updates
        self.message_text = tk.Text(self.root, height=10, width=100)
        self.message_text.pack(pady=10)

    def show_message(self, message: str) -> None:
        """Display a message in the text box."""
        self.message_text.insert(tk.END, message + "\n")
        self.message_text.see(tk.END)

    def show_loading_indicator(self, message: str) -> None:
        """Show a loading indicator with a custom message."""
        if not self.loading_label:
            self.loading_label = tk.Label(self.root, text=message, fg="blue", font=("Arial", 12))
            self.loading_label.pack(pady=10)

    def hide_loading_indicator(self) -> None:
        """Hide the loading indicator."""
        if self.loading_label:
            self.loading_label.destroy()
            self.loading_label = None

    def close_app(self) -> None:
        """Close the application."""
        logger.info("Closing application...")
        
        # Ensure proper cleanup before exiting
        self.root.destroy()

    def run(self) -> None:
        """Run the main event loop of the application."""
        logger.info("Launching application...")
        self.root.mainloop()
