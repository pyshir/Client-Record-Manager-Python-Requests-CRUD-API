# Client Record Manager — Python Requests CRUD API
## jahid (whatsapp: 8801309495010)

A practical Python API automation project built with the `requests` library.

This project simulates a **client record management system** where users can create, read, replace, update, and delete records through HTTP API requests.

The project was built as a hands-on exercise to understand how real-world API automation works using Python.

---

## 🚀 Project Overview

The application provides a command-line interface (CLI) for managing records through the following HTTP methods:

| Operation      | HTTP Method | Purpose                     |
| -------------- | ----------- | --------------------------- |
| View Record    | `GET`       | Retrieve an existing record |
| Create Record  | `POST`      | Create a new record         |
| Replace Record | `PUT`       | Replace/update a record     |
| Update Record  | `PATCH`     | Partially update a record   |
| Delete Record  | `DELETE`    | Delete a record             |

The API used in this project is **JSONPlaceholder**, a free fake REST API designed for testing and learning.

---

## 🛠️ Technologies Used

* Python 3
* Requests
* REST API
* HTTP Methods
* JSON
* Exception Handling
* CLI / Terminal Interface
* Object-Oriented Programming

---

## 📁 Project Structure

```text
client-record-manager/
│
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Enter the project directory

```bash
cd client-record-manager
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Requests

```bash
pip install requests
```

---

## ▶️ Run the Project

```bash
python main.py
```

The application displays:

```text
========== Client Record Manager ==========

1. View Record
2. Create Record
3. Replace Record
4. Update Record
5. Delete Record
6. Exit

Choose an option:
```

---

# 🔄 API Operations

## 1. GET — View Record

The `GET` method retrieves an existing record.

Example:

```text
Input post Id: 5
```

The application sends:

```http
GET /posts/5
```

and displays the record information.

Example output:

```text
Record Found.......!

Id: 5
Title: nesciunt quas odio
Body: repudiandae veniam quaerat...
UserID: 1
```

---

## 2. POST — Create Record

The `POST` method creates a new record.

The application sends data using JSON:

```python
req.post(
    self.link,
    headers=self.headers,
    timeout=10,
    json=payloads
)
```

Example payload:

```json
{
    "title": "New Client",
    "body": "Client information",
    "userId": 1
}
```

---

## 3. PUT — Replace Record

`PUT` is used when the intention is to replace/update the complete record representation.

Example:

```python
req.put(
    url,
    headers=self.headers,
    json=payloads,
    timeout=10
)
```

Conceptually:

```text
Existing Record
       ↓
     PUT
       ↓
Replacement Record
```

---

## 4. PATCH — Partial Update

`PATCH` is used when only part of a record needs to be changed.

For example, updating only the title:

```json
{
    "title": "Updated Client Name"
}
```

The application allows the user to select which field to update:

```text
1. Title
2. Body
```

This demonstrates the difference between **full replacement with PUT** and **partial modification with PATCH**.

---

## 5. DELETE — Delete Record

The `DELETE` method removes a record through the API.

Example:

```python
req.delete(
    url,
    headers=self.headers,
    timeout=10
)
```

After successful deletion:

```text
********Successfully deleted********
```

---

# 🛡️ Error Handling

The project uses Requests' exception hierarchy for HTTP/request-level failures:

```python
except req.exceptions.RequestException as error:
    print(error)
```

Each API operation also uses:

```python
response.raise_for_status()
```

This allows unsuccessful HTTP responses such as `4xx` and `5xx` to be handled as exceptions.

The application also validates numeric Post IDs before constructing the API URL:

```python
try:
    post_id = int(input('Input post Id: '))
except ValueError:
    print("Number Only")
    continue
```

---

# ⏱️ Timeout Handling

Every HTTP request uses a timeout:

```python
timeout=10
```

This prevents the application from waiting indefinitely for a server response.

---

# 🔎 Request Inspection

The project is designed to work with Requests' request/response objects.

Useful request information includes:

```python
response.request.method
response.request.url
response.request.body
```

These can be used to inspect the actual outgoing HTTP request during debugging and API automation.

---

# 🧠 What I Learned

Through this project, I practiced:

* HTTP fundamentals
* REST API concepts
* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`
* JSON request bodies
* JSON responses
* HTTP status codes
* `raise_for_status()`
* Request timeouts
* Requests exception handling
* URL construction
* CLI menu design
* Basic Object-Oriented Programming
* API debugging
* Difference between PUT and PATCH

---

# 🎯 Project Goal

This is not intended to be a production database management system.

The goal is to build practical experience with **Python API automation** and understand how a client application communicates with a REST API.

The project follows a simplified real-world workflow:

```text
User
  ↓
CLI Menu
  ↓
Select Operation
  ↓
Build Request
  ↓
HTTP Request
  ↓
API
  ↓
HTTP Response
  ↓
Validate Response
  ↓
Display Result
```

---

# ⚠️ API Note

This project uses JSONPlaceholder:

```text
https://jsonplaceholder.typicode.com/
```

JSONPlaceholder is a fake REST API intended for testing and learning.

Therefore, POST/PUT/PATCH/DELETE operations should be treated as API practice rather than persistent production data management.

---

# 🔮 Future Improvements

Possible future improvements include:

* Reusable `get_post_id()` validation function
* Better JSON validation
* Separate handling for HTTP, JSON, and Python errors
* Request/response logging
* Better input validation
* Centralized API request handling
* Configuration management
* Authentication support
* Pagination
* Retry mechanism
* File upload/download
* Automated API reports
* Unit tests
* Production API integration

---

## 👨‍💻 Author

**Jahid**

Learning Python, API Automation, and practical backend automation through real-world projects.
