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

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/http-server.git

