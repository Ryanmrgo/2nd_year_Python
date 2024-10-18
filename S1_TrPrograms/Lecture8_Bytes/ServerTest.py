import socket
import threading

def server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_address = ('localhost', 8888)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(*server_address))
    
    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        
        try:
            print('Connection from', client_address)
            
            # Receive data from the client
            data = connection.recv(1024)
            print('Received data:', data.decode('utf-8'))
            
            # Reverse the message
            reversed_message = data[::-1]
            
            # Send the reversed message back to the client
            connection.sendall(reversed_message)
            
        finally:
            # Clean up the connection
            connection.close()
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

'''

if __name__ == "__main__":
    

    server()
    message = "Hello, server!"
    client(message)
'''
if __name__ == "__main__":
    # Start the server in a separate thread
    server_thread = threading.Thread(target=server)
    server_thread.start()

    # Wait for a moment to ensure the server has started
    import time
    time.sleep(1)

    # Now, run the client
    message = "Hello, server!"
    client(message)


