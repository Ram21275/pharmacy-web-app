# Pharmacy Web App (Flask, MySQL)

A captivating and useful pharmaceutical web app designed to streamline pharmacy operations. This app provides a user-friendly interface with CRUD functionalities.

## Technologies Used
- Flask
- MySQL

## Features
- User-friendly interface
- CRUD functionalities (Create, Read, Update, Delete)
- Secure user authentication
- Role-based access control
- Search and filter functionality

## Installation Instructions

### Prerequisites
Ensure you have Python, Flask, and MySQL installed on your machine.

### Backend Setup
1. **Clone the repository**:
   ```bash
   git clone 
   ```

2. Navigate to the backend directory:
   ```bash
   cd pharmacy-web-app/backend
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Update the MySQL connection details:
   Open `config.py` and update the MySQL connection details:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'username'
   app.config['MYSQL_PASSWORD'] = 'password'
   app.config['MYSQL_DB'] = 'pharmacy'
   ```

5. Run the backend server:
   ```bash
   flask run
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install the required packages:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm start
   ```

### Database Setup
Create a new MySQL database. Run the provided SQL scripts located in the `database` directory to set up the necessary tables.

## Usage
1. Open your browser and go to [http://localhost:3000](http://localhost:3000).
2. Register a new account or log in with existing credentials.
3. Use the navigation menu to access different functionalities like adding new records, viewing existing records, updating records, and deleting records.

