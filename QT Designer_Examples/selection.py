from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
import sys
from main import *
from serialport import *
from main import *

class Selection:   
    def __init__(self,Ui_MainWindow):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(Ui_MainWindow)
        
        self.baudrate_box = self.ui.baudrate_box
        self.port_box = self.ui.port_box
        self.parity_box = self.ui.parity_box
        self.stopbit_box = self.ui.stopbit_box
        self.databits_box =self.ui.databits_box
        self.flow_box = self.ui.flow_box
    def get_selected_data(self):
         #settings kısmındaki verileri kaydeder.
        selected_data = {
            'baudrate_box' : self.baudrate_box.currentIndex(),
            'port_box' : self.port_box.currentIndex(),
            'parity_box' : self.parity_box.currentIndex(),
            'stopbit_box' : self.stopbit_box.currentIndex(),      
            'databits_box' : self.databits_box.currentIndex(),   
            'flow_box': self.flow_box.currentIndex(),
        }
        return selected_data
    def process_selected_data(self):
        selected_data =self.get_selected_data()  
             
        baudrate = selected_data.get('baudrate',None)
        print("Selected Baudrate:", 'baudrate')
