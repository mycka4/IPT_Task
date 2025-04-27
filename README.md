**Introduction**
This task is about guessing the correct PIN of the given web application connected to the web server by using a function called Brute Force Strategy. Brute Force is applied in the Python script to ensure that all possible ways of trying PINs from 000-999 are attempted. The Python script will serve as a tool for the user to know the PIN.
In a detailed way, this project is a Python script that connects to a server using raw sockets to brute-force a 3-digit PIN (from 000 to 999) via HTTP POST requests. It automates testing all possible PINs and detects when the correct PIN is found based on the server's response.
Project Structure
•	Web server.app – This is a given server
•	pword.py — Main script to perform the brute-force attack
•	README.md — This file
**How it Works**
The server should run in the background in order to listen to the active ports then run the Python scripts. Optionally, you can go to Chrome then access the web app at 127.0.0.1:8888.
The script:
1.	Opens a TCP socket connection to the server
2.	Sends a POST request to the server endpoint /verify with the PIN as form data (application/x-www-form-urlencoded)
3.	Checks the server's response for positive keywords like "Access granted"
4.	If the correct PIN is found, the script prints it and stops
5.	Otherwise, it keeps trying all possible PINs (000 → 999)
**Server Requirements**
•	Server must listen on localhost (127.0.0.1) and port 8888
•	Server must accept POST requests at the path /verify
•	Server should respond with a success message (e.g., "Success! Found the correct PIN") when the correct PIN is submitted
**Usage Instructions**
1.	Make sure your server is running and ready to accept connections on 127.0.0.1:8888
2.	Run the client script
3.	The script will start trying all PINs automatically. Once the correct PIN is found, it will print the result and exit
4.	Adjust the brute-force speed for faster or slower attempts
**Important Notes**
•	Ethical use only! This script is for educational and authorized testing purposes only
•	Always ensure you have permission before testing servers you do not own
•	The script uses low-level sockets, not requests or http.client, for learning raw HTTP communication
