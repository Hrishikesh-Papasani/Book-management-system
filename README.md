# Book Management Application

## Project Overview

The Book Management Application is a comprehensive full-stack web application that enables users to submit and manage details of their favorite books. The front-end is developed using React, while the back-end is powered by Flask, serving as a RESTful API that interacts with a SQLite database. This project exemplifies the practical application of React and Python Flask concepts.

## Key Features

- **Book Submission Form:**  
  Users can conveniently input details such as book title, author, and genre through an intuitive React form component.
  
- **Flask API and SQLite Integration:**  
  The Flask back-end offers endpoints for storing and retrieving data from a SQLite database, ensuring persistent storage of user-submitted books.
  
- **Modular Front-End with React:**  
  The front-end architecture is segmented into reusable components, promoting clean code organization and maintainability.
  
- **Navigation:**  
  Users can effortlessly transition between the book submission form and the repository view, utilizing React's capabilities for seamless and non-intrusive page updates.
  
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

#### 1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hrishikesh-Papasani/Book-management-system.git
   cd Book-management-system
   ```

#### 2. **Set up the Flask back-end:**
- Navigate to the back-end directory and install Python dependencies:
```bash
    pip install Flask flask-restful sqlite3
```

- Run the Flask server:
```bash
    python app.py
```

- The Flask API will run on http://localhost:5000.

#### 3. **Set up the React front-end:**

- Navigate to the frontend folder:
```bash
cd frontend
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

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Hrishikesh-Papasani/Book-management-system/blob/main/LICENSE) file for details.
