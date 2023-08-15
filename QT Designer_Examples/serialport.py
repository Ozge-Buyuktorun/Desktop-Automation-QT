from PyQt5 import QtWidgets
from main import *
import sys
from PyQt5.QtWidgets import QMainWindow, QComboBox, QPushButton, QLabel
from PyQt5.QtSerialPort import QSerialPortInfo

class SerialPortSelection(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Serial Port Selection')
        self.setGeometry(100, 100, 400, 150)

        self.combo_port = QComboBox(self)
        self.combo_port.setGeometry(50, 30, 220, 30)

        self.btn_select = QPushButton('Select Active Port', self)
        self.btn_select.setGeometry(100, 80, 100, 30)
        self.btn_select.clicked.connect(self.select_port)

        self.populate_serial_ports()

    def populate_serial_ports(self):
       self.combo_port.clear()
       available_ports = QSerialPortInfo.availablePorts()
       
       if not available_ports:
           self.combo_port.addItem("No ports available.")
           self.btn_select.setDisabled(True)
       else:
           for port in available_ports:
               port_description = f"{port.portName()} - {port.description()}"
               self.combo_port.addItem(port_description)
               self.btn_select.setEnabled(True)

    def select_port(self):
        selected_port_name = self.combo_port.currentText().split(" - ")[0]
        if selected_port_name:
            print("Selected Port:", selected_port_name)
            
    def on_enter_combo_box(self,event):
        serial_port_window = SerialPortSelection()
        serial_port_window.show()

