import socket

def client(message):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    server_address = ('localhost', 8888)
    client_socket.connect(server_address)
    
    try:
        # Send data to the server
        client_socket.sendall(message.encode('utf-8'))
        
        # Receive the response from the server
        data = client_socket.recv(1024)
        print('Received from server:', data.decode('utf-8'))
        
    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    message = "Hello, server!"
    client(message)
