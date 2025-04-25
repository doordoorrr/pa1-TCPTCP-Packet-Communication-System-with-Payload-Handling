# pa1- TCP-Packet-Communication-System-with-Payload-Handling
This project implements a client-server communication system using TCP sockets
This project implements a client-server communication system using TCP sockets. The server listens for incoming connections, receives a custom packet containing a versioned header and various payload types (integer, float, or string), unpacks the packet, and sends a summary response back to the client. The client constructs the packet, based on user input via command-line arguments, and sends it to the server for processing. The system demonstrates the use of the struct module for binary data manipulation and offers a clear example of packet creation and handling in a networked environment.
- Network Communication Design: You’ve designed a system where a client and server communicate over TCP sockets, with clear specifications for packet structure (headers and payload).

- Payload Handling: The system design specifies how different data types (integer, float, string) are handled, which shows a well-thought-out approach to varying data input.

- Packet Structure: You've defined how the header and payload are structured and how they are processed on both ends, which involves decisions on data encoding, decoding, and error handling.
