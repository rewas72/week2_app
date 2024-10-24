import socket  
import time  
import random 

HOST = 'localhost'  
PORT = 65432       

# İstemciyi başlat
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Sunucuya bağlan
    
    while True:
        # Rastgele sayı üret ve gönder
        random_number = random.uniform(0, 100)  
        client_socket.sendall(str(random_number).encode())  
        time.sleep(1)  