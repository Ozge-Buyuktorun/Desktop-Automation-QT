import socket

host = "localhost"
port = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((host, port)) 
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5) #aynı anda max 5 bağlantıya izin.      
    print("socket dinleniyor")
except socket.error as msg:
    print("Hata:",msg)

while True: 

   # Client ile bağlantı kurulursa 
   c, addr = s.accept()      
   print('Gelen bağlantı:', addr)

   # Bağlanan client tarafına hoşgeldin mesajı gönderelim.  
   mesaj = 'Bağlantı için teşekkürler'
   c.send(mesaj.encode('utf-8')) 

   # Bağlantıyı sonlandıralım 
   c.close()