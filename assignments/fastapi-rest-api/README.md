# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and deploy RESTful APIs using the FastAPI framework in Python. Students will create a simple API for managing resources and practice handling requests, responses, and data validation.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and create a basic API endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Install FastAPI and Uvicorn
- Create a main application file (e.g., `main.py`)
- Define a root endpoint (`/`) that returns a JSON welcome message

### 🛠️ Task 2: Create CRUD Endpoints

#### Description
Implement RESTful endpoints to manage a simple resource (e.g., items, books, or users) with Create, Read, Update, and Delete operations.

#### Requirements
Completed program should:
- Define a resource model using Pydantic
- Implement endpoints for:
  - Creating a new resource (`POST`)
  - Reading all resources (`GET`)
  - Reading a single resource by ID (`GET`)
  - Updating a resource by ID (`PUT`)
  - Deleting a resource by ID (`DELETE`)
- Validate input data and return appropriate responses

### 🛠️ Task 3: Run and Test the API

#### Description
Start the FastAPI server and test your endpoints using a tool like curl, httpie, or an API client (e.g., Postman).

#### Requirements
Completed program should:
- Run the API locally using Uvicorn
- Demonstrate successful requests and responses for each endpoint
- Document example requests and responses in the README
