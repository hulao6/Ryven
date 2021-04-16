from NWENV import *

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...
import importlib.util
package_path = widget_pp(__file__)
spec = importlib.util.spec_from_file_location('matrix_widget.MatrixWidget', package_path+'/matrix_widget.py')
matrix_widget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix_widget)


class ShowMatrix_Node_MainWidget(matrix_widget.MatrixWidget):
    def __init__(self, params):
        super(ShowMatrix_Node_MainWidget, self).__init__(params)
