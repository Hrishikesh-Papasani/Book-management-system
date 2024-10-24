import React, { useEffect, useState } from 'react';
import '../styles.css'; 

const Display = () => {
  const [books, setBooks] = useState([]);  // State to hold book data
  const [loading, setLoading] = useState(true);  // State to handle loading state

  // Fetch the books data from the backend when the component mounts (runs only once)
  useEffect(() => {
    const fetchBooks = async () => {
        try {
            console.log('Fetching books...');
            const response = await fetch('http://localhost:5000/api/books');

            if (!response.ok) throw new Error('Network response was not ok');

            const data = await response.json();
            console.log('Fetched books:', data);
            setBooks(data.books);
        } catch (error) {
            console.error('Error fetching books:', error);
        } finally {
            setLoading(false);
        }
    };

    fetchBooks();
}, []);


  // Conditional rendering based on whether data is loading or not
  if (loading) {
    return <p>Loading books...</p>;
  }

  return (
    <div>
      <h1>Submitted Favorite Books</h1>

      {/* Check if there are any books */}
      {books.length > 0 ? (
        <table border="1" cellPadding="10" cellSpacing="0">
          <thead>
            <tr>
              <th>ID</th>
              <th>User Name</th>
              <th>Book Name</th>
              <th>Author Name</th>
              <th>Category</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {/* Loop through the books and render them in the table */}
            {books.map((book, index) => (
              <tr key={index}>
                <td>{book.id}</td>
                <td>{book.user_name}</td>
                <td>{book.book_name}</td>
                <td>{book.author_name}</td>
                <td>{book.category}</td>
                <td>{book.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No books have been submitted yet.</p>
      )}
    </div>
  );
};

export default Display;
