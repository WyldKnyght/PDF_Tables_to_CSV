# src/main.py
from user_interface.main_window import PDFExtractorUI
from utils.custom_logging import setup_logging, logger

def main() -> None:
    """Main entry point for the PDF Table Extractor application."""
    setup_logging()  # Setup logging configuration
    logger.info("Starting PDF Table Extractor")

    ui = PDFExtractorUI()
    ui.run()

if __name__ == "__main__":
    main()
