# ResearchBot Server

This is the backend server for the ResearchBot application. It is a FastAPI application responsible for user authentication, data management, and running the automated research workflows.

---

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)

---

## Getting Started

Follow these instructions to get the server up and running on your local machine.

### Prerequisites

- Python 3.9+
- MongoDB
- An Alpha Vantage API Key for stock data.

### Installation

1.  **Clone the repository** (or ensure you are in the `Server` directory).

2.  **Create and activate a Python virtual environment:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install the required dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables.** Create a file named `.env` in the `Server` directory and add the following content. Replace the placeholder values with your actual credentials.

    ```
    MONGO_URI=mongodb://localhost:27017/
    SECRET_KEY=your_super_secret_and_random_string_for_jwt
    ALPHA_VANTAGE_API_KEY=YOUR_ALPHA_VANTAGE_API_KEY
    ```

---

## Running the Server

Once the installation is complete, you can run the server with the following command:

```powershell
uvicorn main:app --reload
```

The API will be running at `http://localhost:8000`.

---

## API Documentation

With the server running, interactive API documentation (provided by Swagger UI) is automatically generated and available at:

**`http://localhost:8000/docs`**

This interface allows you to explore and interact with all the API endpoints, view the expected request and response models, and test the functionality directly from your browser.

The API is organized into the following sections:
- **Authentication & Users**
- **User Settings**
- **Companies**
- **Articles**
- **Market Data**

---

## Project Structure

The server follows a modular structure designed for clarity and scalability:

```
Server/
|-- app/                  # Main application module
|   |-- api/              # API endpoint definitions
|   |-- core/             # Core logic, config, and exceptions
|   |-- db/               # Database connection
|   |-- models/           # Pydantic data models
|   |-- services/         # Business logic and external service interactions
|-- tests/                # Application tests
|-- .gitignore            # Git ignore file
|-- main.py               # Main FastAPI application entry point
|-- requirements.txt      # Project dependencies
```
