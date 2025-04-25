# -----------------------------------------------------------
# Author: alexandria burchfiel
# Class: CSC 4200-002
# Date: Febuary 20, 2025
# -----------------------------------------------------------

import argparse
import socket
import struct

# Function to create a packet based on input parameters
def create_packet(version, header_length, service_type, payload):
    # Prepare the payload depending on service type
    if service_type == 1:  # Integer payload
        packed_payload = struct.pack('!i', int(payload))
    elif service_type == 2:  # Float payload
        packed_payload = struct.pack('!f', float(payload))
    elif service_type == 3:  # String payload
        packed_payload = payload.encode('utf-8')
    else:
        raise ValueError("Invalid service type")

    # Determine the length of the payload
    payload_length = len(packed_payload)
    
    # Pack the header (Version, Header Length, Service Type, Payload Length)
    header = struct.pack('!BBBH', version, header_length, service_type, payload_length)
    
    # Return the full packet (header + payload)
    return header + packed_payload

if __name__ == '__main__':
    # Set up argument parsing for user input
    parser = argparse.ArgumentParser(description="Client for packet creation and sending.")
    parser.add_argument('--version', type=int, required=True, help='Packet version')
    parser.add_argument('--header_length', type=int, required=True, help='Length of the packet header')
    parser.add_argument('--service_type', type=int, required=True, help='Service type of the payload (1 for int, 2 for float, 3 for string)')
    parser.add_argument('--payload', type=str, required=True, help='Payload to be packed into the packet')
    parser.add_argument('--host', type=str, default='localhost', help='Server host')
    parser.add_argument('--port', type=int, default=12345, help='Server port')

    args = parser.parse_args()

    try:
        # Create the packet based on command line arguments
        packet = create_packet(args.version, args.header_length, args.service_type, args.payload)

        # Connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((args.host, args.port))
            print(f"Connected to server at {args.host}:{args.port}")

            # Send the packet to the server
            s.sendall(packet)

            # Receive and print the response from the server
            response = s.recv(1024)
            print(f"Received from server: {response.decode('utf-8')}")
    
    except Exception as e:
        print(f"Error occurred: {e}")