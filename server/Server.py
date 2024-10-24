import socket
import threading
import matplotlib.pyplot as plt
import numpy as np


HOST = 'localhost'
PORT = 65432



plt.ion()  # Etkileşimli modu aç, grafiklerin dinamik olarak güncellenmesini sağlar
x_data = []  
y_data = []  
fig, ax = plt.subplots()  # Yeni bir grafik figürü ve ekseni oluştur
line, = ax.plot(x_data, y_data)  # x ve y verilerine dayalı boş bir çizgi grafiği oluştur


def update_plot(new_data):
    x_data.append(len(x_data))
    y_data.append(new_data)
    line.set_xdata(np.arange(len(x_data)))
    line.set_ydata(y_data)
    ax.relim() # EKSENİ YENİDEN SINIRLAMAYA YARAR
    ax.autoscale_view()
    plt.draw() #Grafik çizimini günceller
    plt.pause(0.01) #grafiği kısa süreliğine dururdurur



    
def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            number = float(data.decode())
            update_plot(number)
        except Exception as e: 
            print(f"Hata: {e}")
            break
        
    client_socket.close()
    
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"sunucu dinleniyor host: {HOST}:{PORT}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Bağlantı alındı: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
        
