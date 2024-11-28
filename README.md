# Blockchain Enhanced EHR Management System

## Overview
This project is a simple implementation of a Blockchain Enhanced Electronic Health Record (EHR) Management System using Ethereum smart contracts and a Flask backend.

## Project Structure
- **backend/**: Contains the backend code including smart contracts and Flask app.
- **frontend/**: Contains the HTML, CSS, and JavaScript files for the user interface.

## Setup Instructions
1. Install the required packages:
   ```bash
   pip install -r backend/requirements.txt

2. Deploy the smart contract using the deploy.py script.

3. Run the Flask app:
``` python backend/app.py ``` 

4. Open frontend/index.html in a web browser to access the application.

## Usage:

Add patient records by filling out the form and clicking "Add Record".

View all records displayed below the form.


This structure provides a foundational setup for a Blockchain Enhanced EHR Management System. You can expand upon this by adding features such as user authentication, more detailed record management, and enhanced security measures.

### Project Structure

📂 EHR-Management-System/ ├── 📁 blockchain/ # Blockchain-related files and directories │ ├── 📁 contracts/ # Smart contracts │ ├── 📁 network/ # Blockchain network configurations │ └── 📁 scripts/ # Scripts for deploying/interacting with blockchain ├── 📁 backend/ # Backend files │ ├── 📄 app.py # Main backend application file │ ├── 📄 requirements.txt # Python dependencies for the backend │ └── 📄 models.py # Database models ├── 📁 frontend/ # Frontend application │ ├── 📁 src/ # Source files for the frontend │ │ ├── 📄 App.vue # Main Vue.js app file │ │ ├── 📄 main.js # Entry point for the frontend application │ │ └── 📁 components/ # Reusable Vue.js components ├── 📄 package.json # Node.js dependencies and scripts └── 📄 vue.config.js # Vue.js configuration file
