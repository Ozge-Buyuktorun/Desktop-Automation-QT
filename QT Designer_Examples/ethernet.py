import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QLabel, QMessageBox, QInputDialog, QComboBox
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtCore import Qt
from datagenerate import *
import socket

class EthernetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        #ethernet page's UI side
        self.setWindowTitle("Ethernet App")
        self.setGeometry(200, 200, 600, 600)

        layout = QVBoxLayout()

        self.ip_label = QLabel("Server IP:")
        self.ip_input = QLineEdit()
        self.ip_label.setFont(QFont("Corbel",12))
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)  
        
        self.port_label = QLabel("Port Number:")
        self.port_input = QLineEdit()
        self.port_label.setFont(QFont("Corbel",12))
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)
        
        self.data_size_label = QLabel("Data Size (KB):")
        layout.addWidget(self.data_size_label)

        self.generated_data_label = QLabel("Generated data:")
        self.generated_data_text = QLineEdit(" Generated data")
        layout.addWidget(self.generated_data_label)
        layout.addWidget(self.generated_data_text)
        
        generate_button = QPushButton("Generate Data", self.centralwidget)
        generate_button.setGeometry(Qt.QRect(10, 270, 150, 30))
        generate_button.clicked.connect(self.show_generated_data())  # Lambda işlevi ile show_generated_data() çağrısı

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def get_recommended_message(self, available_ports):
        if available_ports:
            recommended_ports = available_ports[:20]
            recommended_message = "Recommended IP and Ports:\n"
            for ip, port in recommended_ports:
                recommended_message += f"- {ip} : {port}\n"
            return recommended_message
        else:
            return "No available ports found."
    def get_available_ports(self):
        result = []
        try:
            cmd_output = subprocess.check_output(["netstat", "-an"], shell=True)
            cmd_output = cmd_output.decode("utf-8")
            lines = cmd_output.split('\n')

            for line in lines:
                parts = line.split()
                if len(parts) >= 5:
                    ip_port = parts[1]
                    ip, port = ip_port.rsplit(":", 1)
                    result.append((ip, port))
        except subprocess.CalledProcessError as e:
            print("Error while running netstat: ", e)
        return result
    def send_data_over_ethernet(self, target_ip, target_port, data):
        try:
            target_port = int(target_port)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target_ip, target_port))
                s.send(data.encode())
                received_data = s.recv(1024).decode()
                print("Sent data over Ethernet:", data)
                print("Received data over Ethernet:", received_data)
            print("The process is done")
        except socket.error as e:
            print("Socket creation error: ", e)

        # target_ip = self.ip_input.text()
        # target_port = self.port_input.text()

        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #     s.connect((target_ip, target_port))
        #     s.sendall(data)
        #     received_data = s.recv(1024).decode()
        # print("Sent data over Ethernet:", data)
        # print("Received data over Ethernet:", received_data)
        # return print("The process is done")
