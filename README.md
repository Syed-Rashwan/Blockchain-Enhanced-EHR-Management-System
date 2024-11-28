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


## Components

### Blockchain
- **contracts/**: Contains the smart contracts that define the logic for managing EHR data on the blockchain.
- **network/**: Configuration files for setting up and connecting to the blockchain network.
- **scripts/**: Utility scripts for deploying the smart contracts and interacting with the blockchain.

### Backend
- **app.py**: The main application file for the backend, handling API requests and business logic.
- **requirements.txt**: Lists the Python dependencies required for the backend application.
- **models.py**: Defines the database models used to manage data on the server side.

### Frontend
- **src/**: Contains the source code for the frontend application built with Vue.js.
  - **App.vue**: The main Vue.js component that serves as the entry point for the application.
  - **main.js**: The entry point for initializing the Vue.js application.
  - **components/**: A directory for reusable Vue.js components that can be used throughout the application.

### Configuration Files
- **package.json**: Contains the Node.js dependencies and scripts for managing the frontend application.
- **vue.config.js**: Configuration settings for the Vue.js application.

## Getting Started

### Prerequisites
- Node.js and npm installed for the frontend.
- Python and pip installed for the backend.
- Access to an Ethereum node (local or testnet) for the blockchain.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/EHR-Management-System.git
   cd EHR-Management-System

2. **Setup the backend:**
```bash
cd backend
pip install -r requirements.txt
```
3. **Setup the frontend:**

```bash

cd frontend
npm install
```
Deploy the smart contracts: Navigate to the blockchain/scripts directory and run the deployment scripts as needed.

4. **Run the applications:**

- **Start the backend server:**
```bash
python app.py
```
- **Start the frontend application:**
```bash
npm run serve
```

### Usage

Access the frontend application through the provided local server URL.

Interact with the EHR management features, utilizing the blockchain for secure data management.


### Contributing
Feel free to contribute to this project by submitting issues or pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
