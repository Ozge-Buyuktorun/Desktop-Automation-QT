import socket

#Socket oluşturulması
s = socket.socket()

#bağlanılacak adres ve port 
host = "localhost"
port= 12345

try: 
    #bağlantıyı yap. 
    s.connect((host, port))
    print("Bağlanıldı")
    
    
    #server dan yanıt al 
    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))
    
    #bağlantıyı kapat
    s.close()
    
except socket.error as msg:
    print( "[Server aktif değil.] Mesaj:", msg)
    


