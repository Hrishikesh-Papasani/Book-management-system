import React from 'react';
import { useParams, Link } from 'react-router-dom'; 
import '../styles.css';

const Home = () => {
  // Get the username from the URL using useParams
  const { username } = useParams();

  return (
    <div>
      <h1>Welcome {username || 'User'}!</h1>
      <p>
        Fill a form about your favorite book: <Link to="/Form">Form</Link> 
      </p>
    </div>
  );
};

export default Home;
