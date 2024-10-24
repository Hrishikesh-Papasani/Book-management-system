import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';    
import Form from './components/Form';    
import Display from './components/Display'; 
import './styles.css'; 

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Route for Home page with optional username route parameter */}
          <Route path="/:username?" element={<Home />} />

          {/* Route for Form page */}
          <Route path="/form" element={<Form />} />

          {/* Route for Display page */}
          <Route path="/display" element={<Display />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
