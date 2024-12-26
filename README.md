# FINAL_PROJECT_IT120
Check daw ni: # AppA and AppB Documentation

## Overview

This repository contains two Django applications, *AppA* and *AppB*, designed to work together for secure user messaging and authentication.  
- *AppA*: Functions as the recipient of secure messages.  
- *AppB*: Serves as the sender and user-facing interface for messaging and authentication.

---

## AppA

### Purpose

AppA is designed to securely receive messages from AppB. It acts as a dedicated recipient and does not handle message sending, ensuring a streamlined and secure communication process.

### Key Features

- *Message Reception*: Receives messages exclusively from AppB through a controlled API endpoint.  
- *Data Validation*: Validates incoming messages to ensure integrity and authenticity.  
- *Encryption Handling*: Decrypts received messages securely using robust algorithms.  
- *Middleware Integration*: Includes middleware for authentication and decryption of messages.

### Security Features

- *Source Validation*: Processes messages only from AppB.  
- *Encryption*: Protects messages in transit using AES-256 encryption.  
- *Authentication*: Verifies message origin with JSON Web Tokens (JWT).  
- *Integrity Checks*: Ensures messages have not been tampered with during transmission.

### Directory Structure


appA/
├── manage.py # Django command-line utility
├── db.sqlite3 # Local SQLite database
├── user_messages/ # Message processing functionalityHere's the converted content in README.md format:

# AppA and AppB Documentation

## Overview

This repository contains two Django applications, **AppA** and **AppB**, designed to work together for secure user messaging and authentication.
- **AppA**: Functions as the recipient of secure messages.
- **AppB**: Serves as the sender and user-facing interface for messaging and authentication.

---

## AppA

### Purpose

AppA is designed to securely receive messages from AppB. It acts as a dedicated recipient and does not handle message sending, ensuring a streamlined and secure communication process.

### Key Features

- **Message Reception**: Receives messages exclusively from AppB through a controlled API endpoint.
- **Data Validation**: Validates incoming messages to ensure integrity and authenticity.
- **Encryption Handling**: Decrypts received messages securely using robust algorithms.
- **Middleware Integration**: Includes middleware for authentication and decryption of messages.

### Security Features

- **Source Validation**: Processes messages only from AppB.
- **Encryption**: Protects messages in transit using AES-256 encryption.
- **Authentication**: Verifies message origin with JSON Web Tokens (JWT).
- **Integrity Checks**: Ensures messages have not been tampered with during transmission.

### Directory Structure

appA/
├── manage.py # Django command-line utility
├── db.sqlite3 # Local SQLite database
├── user_messages/ # Message processing functionality
└── users/ # User management functionality

---

## AppB

### Purpose

AppB serves as the user-facing application, providing authentication and secure message-sending capabilities. It communicates with *AppA* to deliver encrypted messages.

### Key Features

- *User Authentication*: Implements user registration and login functionality using JWT.
- *Message Sending*: Enables users to send secure messages to AppA through a controlled API.
- *Message Encryption*: Ensures messages are encrypted before transmission to maintain confidentiality.
- *Frontend Integration*: Provides user-friendly HTML templates and RESTful API endpoints for seamless interaction.
- *Environment Configuration*: Loads settings securely from environment variables for enhanced security.


### Security Features

- *Encryption*: Encrypts all outgoing messages to protect sensitive data.
- *Authentication*: Utilizes JWT to verify user identity and authorize message-sending operations.
- *Rate Limiting*: Limits the frequency of message-sending requests to prevent abuse.


### Directory Structure

appB/
├── manage.py # Django command-line utility
├── db.sqlite3 # Local SQLite database
├── appb/ # Core application code (views, models, serializers)
└── project_b/ # Project-wide settings and configurations
└── users/           # User management functionality


Here's the converted content in README.md format:

# AppA and AppB Documentation

## Overview

This repository contains two Django applications, **AppA** and **AppB**, designed to work together for secure user messaging and authentication.
- **AppA**: Functions as the recipient of secure messages.
- **AppB**: Serves as the sender and user-facing interface for messaging and authentication.

---

## AppA

### Purpose

AppA is designed to securely receive messages from AppB. It acts as a dedicated recipient and does not handle message sending, ensuring a streamlined and secure communication process.

### Key Features

- **Message Reception**: Receives messages exclusively from AppB through a controlled API endpoint.
- **Data Validation**: Validates incoming messages to ensure integrity and authenticity.
- **Encryption Handling**: Decrypts received messages securely using robust algorithms.
- **Middleware Integration**: Includes middleware for authentication and decryption of messages.

### Security Features

- **Source Validation**: Processes messages only from AppB.
- **Encryption**: Protects messages in transit using AES-256 encryption.
- **Authentication**: Verifies message origin with JSON Web Tokens (JWT).
- **Integrity Checks**: Ensures messages have not been tampered with during transmission.

### Directory Structure


appA/
├── manage.py # Django command-line utility
├── db.sqlite3 # Local SQLite database
├── user_messages/ # Message processing functionality
└── users/ # User management functionality

---

## AppB

### Purpose

AppB serves as the user-facing application, providing authentication and secure message-sending capabilities. It communicates with *AppA* to deliver encrypted messages.

### Key Features

- *User Authentication*: Implements user registration and login functionality using JWT.
- *Message Sending*: Enables users to send secure messages to AppA through a controlled API.
- *Message Encryption*: Ensures messages are encrypted before transmission to maintain confidentiality.
- *Frontend Integration*: Provides user-friendly HTML templates and RESTful API endpoints for seamless interaction.
- *Environment Configuration*: Loads settings securely from environment variables for enhanced security.


### Security Features

- *Encryption*: Encrypts all outgoing messages to protect sensitive data.
- *Authentication*: Utilizes JWT to verify user identity and authorize message-sending operations.
- *Rate Limiting*: Limits the frequency of message-sending requests to prevent abuse.


### Directory Structure

plaintext
appB/
├── manage.py # Django command-line utility
├── db.sqlite3 # Local SQLite database
├── appb/ # Core application code (views, models, serializers)
└── project_b/ # Project-wide settings and configurations

---

## Running the Application

1. **Clone the Repository**Clone the project repository to your local machine:

shellscript
git clone https://github.com/tina-cmd/FINAL_PROJECT_IT120.git


2. *Install Dependencies*
Install the required Python libraries using pip:

shellscript
pip install -r requirements.txt


3. *Navigate to the Project Directory*
Run the applications in separate terminals:

For AppA:

shellscript
cd appA
python manage.py migrate
python manage.py runserver

For AppB:

shellscript
cd appB
python manage.py migrate
python manage.py runserver 8001


4. *Access the Applications*

1. AppA: Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)
2. AppB: Open your browser and navigate to [http://127.0.0.1:8001](http://127.0.0.1:8001)


---

## Additional Notes

### Environment Variables

Ensure all required environment variables (e.g., database connection strings, JWT secrets) are properly configured. Use a .env file to securely manage these variables.

### Testing

Run the test suite to verify the functionality of the application:

shellscript
python manage.py test

### Deployment

For production environments:

- Configure a web server like Gunicorn or Nginx.
- Use a production-grade database, such as PostgreSQL, instead of SQLite.