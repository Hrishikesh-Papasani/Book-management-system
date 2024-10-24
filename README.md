# Book Management Application

## Project Overview

The **Book Management Application** is a full-stack web application designed to allow users to submit and manage details of their favorite books. The front-end is built with React, and the back-end is powered by Flask, serving as a RESTful API to interact with a SQLite database. This project showcases a practical implementation of React and Python Flask concepts.

## Key Features

- **Book Submission Form:**  
  Users can input details such as the book title, author, and genre using a React form component.
  
- **Flask API and SQLite Integration:**  
  The Flask back-end provides endpoints to store and retrieve data from a SQLite database, enabling persistent storage of user-submitted books.

- **Modular Front-End with React:**  
  The front-end is divided into reusable components, ensuring clean code organization and maintainability.

- **Navigation:**  
  Users can navigate between the form to add new books and a page to view all books stored in the database.

## Technology Stack

- **Front-End:**  
  React (JavaScript, JSX, React Router, state management)
  
- **Back-End:**  
  Flask (Python, Flask-RESTful)

- **Database:**  
  SQLite (for data storage)

## Getting Started

### Prerequisites

- **Node.js** and **npm** (for running the React front-end)
- **Python 3.x** (for running the Flask back-end)
- **SQLite** (pre-installed with Python)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Set up the Flask back-end:**
- Navigate to the back-end directory and install Python dependencies:
```bash
    pip install Flask flask-restful sqlite3
```

- Run the Flask server:
```bash
    python app.py
```

- The Flask API will run on http://localhost:5000.

3. **Set up the React front-end:**

- Navigate to the client folder:
```bash
cd client
```
- Install front-end dependencies:
```bash
npm install
```

- Start the React development server:
```bash
npm start
```

- The React app will run on http://localhost:3000.


## Running the Application
Once both the React front-end and Flask back-end are running:

1. **Submit a Book**:
Navigate to the form page on http://localhost:3000 and enter details about your favorite book. The data will be sent to the Flask API and stored in the SQLite database.

2. **View Stored Books**:
Navigate to the page where all books are displayed, allowing you to view the list of books stored in the database.

## Available Scripts
In the project directory, you can run:

<b>npm start</b>
Runs the React app in development mode. Open http://localhost:3000 to view it in your browser. The page will automatically reload when you make changes.

<b>npm run build</b>
Builds the React app for production, creating optimized files in the build folder.

<b>python app.py</b>
Runs the Flask back-end API in development mode on http://localhost:5000.

## Future Enhancements

- Implement full CRUD operations for books (e.g., editing and deleting entries).
- Add input validation and error handling.
- Improve UI styling and responsiveness.
- Expand the database capabilities to include user authentication and authorization.

## License
This project is licensed under the MIT License. See the LICENSE file for details.