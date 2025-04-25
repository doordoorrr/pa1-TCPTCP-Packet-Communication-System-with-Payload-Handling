# -----------------------------------------------------------
# Author: alexandria burchfiel
# Class: CSC 4200-002
# Date: Febuary 20, 2025
# -----------------------------------------------------------

import socket
import struct

def unpack_packet(conn, header_format):
    header_data = conn.recv(5)      # Receive the fixed-length header (5 bytes)
    if not header_data:             
        return None                 # Return None if no data is received (client disconnected)

    # Unpack the header using the struct module 
    version, header_length, service_type, payload_length = struct.unpack(header_format, header_data)
    # Receive the payload based on the payload length specified in the header
    payload_data = conn.recv(payload_length)    

    # Decode the payload based on the service type
    if service_type == 1:       # Integer payload
        payload = struct.unpack('!i', payload_data)[0]
    elif service_type == 2:     # Float payload
        payload = struct.unpack('!f', payload_data)[0]
    elif service_type == 3:     # String payload
        payload = payload_data.decode('utf-8')
    else:
        payload = "Unknown service type"

    # Create a string summarizing the packet details
    packet_header_as_string = f"Version: {version}, Header Length: {header_length}, Service Type: {service_type}, Payload: {payload}"
    return packet_header_as_string

if __name__ == '__main__':
    host = '0.0.0.0'    # Listen on all interfaces for incoming connections
    port = 12345        # Port number for the server

    # Define header format: Version (1 byte), Header Length (1 byte), 
    # Service Type (1 byte), Payload Length (2 bytes)
    header_format = '!BBBH'

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))    # Bind the socket to the host and port
        s.listen()              # Start listening for incoming connections
        print(f"Server listening on {host}:{port}")
        
        while True:  # Keep the server running
            try:
                conn, addr = s.accept()  # Accept new connections
                print(f"Connected by: {addr}")
                with conn:
                    while True:
                        # Unpack the packet received from the client
                        payload_string = unpack_packet(conn, header_format)
                        if payload_string is None:
                            print(f"Connection closed by {addr}")
                            break  # Exit inner loop if no data

                        print(f"Received: {payload_string}")
                        conn.sendall(payload_string.encode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
                # Handle errors