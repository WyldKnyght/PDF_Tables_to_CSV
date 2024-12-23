# src/controllers/pdf_manager.py
from .pdf_modules.pdf_workflow import PDFWorkflow

class PDFManager:
    """Thin wrapper to orchestrate PDF processing by delegating tasks to modules."""

    def __init__(self, ui: object) -> None:
        self.ui = ui

    def start_pdf_processing(self) -> None:
        """Start the PDF processing workflow."""
        workflow = PDFWorkflow(self.ui)  # Instantiate PDFWorkflow
        workflow.start_pdf_processing()  # Call the method on the instance
