# **Blockchain Enhanced EHR System (Electronic Health Records System)**

## **Overview**
The **Blockchain Enhanced EHR System** is a blockchain-based solution for securely storing and managing electronic health records. This decentralized application (DApp) ensures data integrity, transparency, and access control for patients and healthcare providers.

## **Features**
- **Decentralized Storage**: Health records are securely stored on the blockchain.
- **Role-Based Access Control**: Different levels of access for patients, doctors, and administrators.
- **Data Privacy**: Only authorized users can view or modify records.
- **Interactive Frontend**: User-friendly interface for managing health records.
- **Audit Logging**: Tracks interactions with the system for security and compliance.

---

## **Project Structure**

### **Backend**
The backend handles API interactions, connects to the blockchain, and processes business logic.

```
Backend/
│
├── app.py            # Flask application for API routes
├── models.py         # Database models and auxiliary data structures
├── requirements.txt  # Dependencies for running the backend
└── package-lock.json # Dependency lock file (optional)
```

### **Blockchain**
The blockchain folder contains smart contract code and related scripts.

```
Blockchain/
│
├── Contracts/
│   └── EHR.sol       # Smart contract for managing health records
│
├── Network/
│   ├── development.json  # Configuration for local blockchain
│   └── mainnet.json      # Configuration for production blockchain
│
└── Scripts/
    ├── deploy.py     # Script for deploying the smart contract
    ├── interact.py   # Script for interacting with the smart contract
    └── test.py       # Script for testing the smart contract
```

### **Frontend**
The frontend provides an interface for users to interact with the system.

```
Frontend/
│
├── Components/
│   ├── app.js        # Main JavaScript logic for interacting with APIs
│   ├── auth.js       # Authentication and role management logic
│   └── records.js    # Functions for managing health records
│
├── index.html        # Main HTML file for the application
├── style.css         # Stylesheet for the application
└── README.md         # Documentation for the frontend (optional)
```

---

## **Getting Started**

### **1. Prerequisites**
- **Python** (v3.8 or later)
- **Node.js** (v14 or later)
- **Ganache CLI** (for local blockchain testing)
- **Metamask** (for frontend interaction with the blockchain)

### **2. Installation**

#### Backend
1. Navigate to the `Backend` folder:
   ```bash
   cd Backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```

#### Blockchain
1. Navigate to the `Blockchain/Scripts` folder:
   ```bash
   cd Blockchain/Scripts
   ```
2. Deploy the smart contract:
   ```bash
   python deploy.py
   ```
3. Note the deployed contract address and update the configuration files (`development.json` or `mainnet.json`).

#### Frontend
1. Navigate to the `Frontend` folder:
   ```bash
   cd Frontend
   ```
2. Serve the frontend:
   - Use a local server or open `index.html` directly in a browser.

---

## **Usage**

1. **Deploy the Smart Contract**:
   - Use `deploy.py` to deploy the `EHR.sol` contract to a blockchain network.
2. **Run the Backend**:
   - Start the Flask server and ensure it connects to the deployed contract.
3. **Access the Frontend**:
   - Open the `index.html` file in a browser.
4. **Interact with the System**:
   - **Patients**: Add and view health records.
   - **Doctors**: Access records with permissions.
   - **Admins**: Monitor system activity.

---

## **Testing**

1. Navigate to the `Blockchain/Scripts` folder:
   ```bash
   cd Blockchain/Scripts
   ```
2. Run the test script:
   ```bash
   python test.py
   ```
3. Verify the outputs and ensure the contract behaves as expected.

---

## **Enhancements**
### **Planned Features**
- File upload for medical reports.
- Enhanced role-based dashboards.
- Notifications for updates or alerts.

### **UI Improvements**
- Use a CSS framework (e.g., Bootstrap or Tailwind CSS) for responsiveness.
- Add animations and transitions for better UX.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

## **Contributors**
- **Syed Rashwan** (Project Lead)
