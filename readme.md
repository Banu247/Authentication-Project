# SecureAuth FastAPI: A Mini Authentication System

This mini project serves as a basic authentication system using FastAPI, SQLAlchemy, and cryptography for encryption and decryption. The project allows users to perform the following actions:

1. **Create User:**
   - Users can be created by providing a unique username and a password. The password is encrypted using the cryptography library before being stored in the database.

2. **Fetch Users:**
   - The system provides an endpoint to fetch a list of users. The response includes user IDs and usernames.

3. **Delete Users:**
   - Users can be deleted by providing their username or to delete all the users need to specify "all" . The system ensures the existence of the user before proceeding with the deletion.

3. **Login:**
Users can log in to the system by providing their username and password. The login endpoint is designed to authenticate users securely and enforce certain password restrictions

## Project Components

- **FastAPI:** A modern, fast web framework for building APIs with Python.
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Cryptography:** A library for secure communication and data encryption and decryption.

## Usage

1. **Installation:**
   - Install the required dependencies using:
     ```
     pip install fastapi sqlalchemy cryptography
     ```

2. **Run the Application:**
   - Execute the main FastAPI application file to start the server:
     ```
     uvicorn main:app --reload
     ```

3. **Endpoints:**
   - Access the following endpoints:
     - **Create User:** `POST /user-creation`
     - **Fetch Users:** `GET /fetch-users`
     - **Delete User:** `DELETE /delete-user/{user}`
     - **Login:**  `POST /login`

## Encryption and Decryption

- The project utilizes the cryptography library to encrypt and decrypt user passwords, ensuring the security of stored credentials.

Feel free to explore and adapt this mini project based on your authentication requirements!

---

# Further updates

# User Interface (UI) Integration:

* Create a user-friendly interface for interacting with the authentication system, enabling easy user registration, login, and profile management.
# Security Enhancements:

* Continuously review and enhance security measures to protect against potential vulnerabilities, ensuring the confidentiality and     integrity of user data.
