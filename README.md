# Simple HTTP Server

This is a basic HTTP server implementation in Python. It handles simple `GET` and `POST` requests, processes them, and sends appropriate HTTP responses. This project is intended to demonstrate how to create a simple web server using Python's `socket` library.

## Features

- Handles `GET` requests to serve content.
- Handles `POST` requests to process submitted data.
- Responds with appropriate HTTP status codes and messages.
- Supports basic routing for different paths (e.g., `/`, `/about`, `/submit`).
- Responds with `400 Bad Request` for paths not found.

## Requirements

- Python 3.x (preferably Python 3.7 or higher)
- No external libraries are required, as this project uses Python's built-in `socket` library.

## Getting Started

## Code Structure
codecrafters-http-server-python/
│
├── app/
│   ├── main.py               # The main Python server script
│
├── Procfile                  # Tells Heroku how to run the server
├── requirements.txt          # Lists dependencies (even if empty)
└── README.md                 # Project documentation

## How to Run the Server Locally
Ensure Python is Installed:
This code runs on Python 3.x, so make sure you have Python installed on your local machine. You can check if Python is installed by running:  python --version

## Clone the Project (if you haven't already):
git clone https://github.com/your-username/codecrafters-http-server-python.git
cd codecrafters-http-server-python
## Run the Server:
Navigate to the app directory where main.py is located, and run the server using the following command:
python app/main.py
## the terminal:
Server is running on http://localhost:4221/
## Testing the Server:

Using a web browser: Open a web browser and visit http://localhost:4221/. You should see the "Welcome to the Home Page!" message. You can also visit http://localhost:4221/about to see the "About Us" page.

## Using curl: You can test the server with curl from the command line.

Example of a GET request:

## bash
curl http://localhost:4221/
Example of a POST request (assuming your server handles POST on /submit):

## bash
curl -X POST http://localhost:4221/submit -d "name=John&age=30"
