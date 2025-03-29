import socket

# Define a mapping of paths to their responses
path_mapping = {
    "/": "Welcome to the Home Page!",
    "/about": "This is the About Page.",
    "/contact": "Feel free to contact us at contact@example.com."
}

def parse_http_request(request):
    """
    Parse the HTTP request to extract the method, path, and version.
    """
    lines = request.split("\r\n")
    # The first line of the request contains the method, path, and version
    method, path, version = lines[0].split(" ")
    return method, path, version, lines

def handle_get_request(path):
    """
    Handle GET requests based on the path.
    """
    if path in path_mapping:
        response_body = path_mapping[path]
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
    else:
        response = "HTTP/1.1 404 Not Found\r\nContent-Length: 15\r\n\r\nPath Not Found"
    return response

def handle_post_request(path, data):
    """
    Handle POST requests and return the response.
    """
    if path == "/submit":
        response_body = f"Data received: {data}"
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
    else:
        response = "HTTP/1.1 404 Not Found\r\nContent-Length: 15\r\n\r\nPath Not Found"
    return response

def handle_request(request):
    """
    Handle the HTTP request, including GET and POST methods.
    """
    method, path, version, lines = parse_http_request(request)
    
    if method == "GET":
        return handle_get_request(path)
    elif method == "POST":
        # For POST, retrieve the body data (if any)
        body_data = ""
        if len(lines) > 1:
            body_data = lines[-1]  # POST data is typically after the headers
        return handle_post_request(path, body_data)
    else:
        return "HTTP/1.1 405 Method Not Allowed\r\nContent-Length: 25\r\n\r\nMethod Not Allowed"

def main():
    # Set up the server socket to listen for incoming connections
    server_socket = socket.create_server(("localhost", 4221))
    print("Server is running on localhost:4221...")

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        with client_socket:
            # Read data from the client (HTTP request)
            data = client_socket.recv(1024)
            request = data.decode()

            if request:
                print(f"Received request: {request}")

                # Handle the request and generate a response
                response = handle_request(request)

                # Send the response back to the client
                client_socket.sendall(response.encode())

if __name__ == "__main__":
    main()
