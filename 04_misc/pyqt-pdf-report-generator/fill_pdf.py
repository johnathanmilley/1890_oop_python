from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot

from reportlab.pdfgen.canvas import Canvas

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    error = pyqtSignal(str)
    file_saved_as = pyqtSignal(str)


class Generator(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.

    :param data: The data to add to the PDF for generating.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            outfile = "result.pdf"

            template = PdfReader("template.pdf", decompress=False).pages[0]
            template_obj = pagexobj(template)

            canvas = Canvas(outfile)

            xobj_name = makerl(canvas, template_obj)
            canvas.doForm(xobj_name)

            ystart = 443

            # Prepared by
            canvas.drawString(170, ystart, self.data['name'])

            canvas.save()

        except Exception as e:
            self.signals.error.emit(str(e))
            return

        self.signals.file_saved_as.emit(outfile)