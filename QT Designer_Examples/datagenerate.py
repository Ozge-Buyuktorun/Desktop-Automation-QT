from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QWidget,QComboBox,QMessageBox
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer 
import sys, os
import random
import string
import socket
from ethernet import *

class DataGeneratorApp(QMainWindow):
    data_counter=1  #initialize data counter
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Generator Application")
        layout = QVBoxLayout()
        layout.setGeometry(QtCore.QRect(100, 100, 150, 300))
        
        self.data_size_label = QLabel("Data Size (KB):")
        layout.addWidget(self.data_size_label)
        
        self.data_size_input = QComboBox()
        size_list = ["16B", "32B", "512B", "4KB", "16KB", "512KB", "1MB", "16MB", "512MB"]
        self.data_size_input.addItems(size_list)  
        layout.addWidget(self.data_size_input)
        
        self.generated_data_dict = {} #dictionary to store generated data
        
        #export file
        self.export_file = QPushButton("Export File")
        layout.addWidget(self.export_file)
        
        #generate data button
        self.generate_button = QPushButton("Generate Data")
        self.generate_button.clicked.connect(self.generate_data)
        self.export_file.clicked.connect(self.convert_to_file)
        self.generated_data_text = QLabel("")
        self.generated_data_text.setFixedSize(200,100)
        self.generated_data_text.setWordWrap(True)

        # self.generated_data_text.setMaximumHeight(80) #Max Width 200 pixels limitation.
        layout.addWidget(self.generated_data_text)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.export_file)

        self.export_file.clicked.connect(self.convert_to_file)

        self.list_widget = QLineEdit()
        layout.addWidget(self.list_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        #timer
        self.send_timer = QTimer(self)
        self.send_timer.timeout.connect(self.send_data)
        self.send_internal = 1  #default interval in seconds
        #send button
        self.send_button = QPushButton("Send Data")
        layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.start_sending)                                               
    def generate_data(self):
        selected_size_text = self.data_size_input.currentText()
        data_size_kb = int(selected_size_text[:-2]) #Remove KB and convert to int
        data_size_bytes = data_size_kb * 1024   #calculate data size in bytes.
        letters = string.ascii_letters
        data1 = ''.join(random.choice(letters) for _ in range(data_size_bytes))
        self.generated_data_text.setText(data1)       
        print("data1",data1)
        
        data_key =f"data{len(self.generated_data_dict) + 1}"  #class level attribute.
        self.generated_data_dict[data_key] = data1
        DataGeneratorApp.data_counter += 1
        
        self.list_widget.setText(data1)
        self.list_widget.setGeometry(300,300,200,80)
        return data1
        #data1 : generated dummy data according to selected data size
    def convert_to_file(self):
        generated_data = self.generate_data()
        if generated_data:
            desktop_path = os.path.expanduser("C:/Users/PC_N_761/Documents/deneme/")
            # Use a cross-platform approach for desktop path. desktop_path = os.path.expanduser("C~/Desktop")
            file_path = os.path.join(desktop_path, 'random_data.bin')
            
            with open(file_path, 'wb') as file:
                file.write(self.generated_data_text.text().encode())  # Assuming generated_data is a string
                
            self.main.tx.setText(generated_data)  # Set the generated data to the tx field in the main window
                
            QMessageBox.information(self, "Success", f"Random data saved as '{file_path}'")
        else:
            QMessageBox.critical(self, "Error", "Please generate data before sending")
        return
    def send_data(self):
        selected_data_key = self.data_size_input.currentText()
        data_to_send = self.generated_data_dict.get(selected_data_key)
        
        if data_to_send:
            print("Sending data:", data_to_send)
        else:
            print("No data to send for the selected key.")
    def start_sending(self):
        self.send_timer.start(self.send_interval * 1000)  #convert to miliseconds
    def stop_sending(self):
        self.send_timer.stop()
