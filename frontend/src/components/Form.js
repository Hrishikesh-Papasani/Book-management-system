import React, { useState } from "react";
import { Link } from "react-router-dom";

// Alternative to Link, this hook offers a more programmatic way for navigation. Can use either for this application. Using 'Link' by default.
// import { useNavigate } from "react-router-dom";
import '../styles.css';

const Form = () => {
    // State for application => Form data, submission status, response message.
    const [formData, setFormData] = useState({
        userName: "",
        bookName: "",
        authorName: "",
        category: "",
        description: ""
    });

    const [submitted, setSubmitted] = useState(false);
    const [responseMessage, setResponseMessage] = useState("");

    // Event handlers
    const handleChange = (e) => { 
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    // When user clicks the reset button
    const handleReset = () => {
        setFormData({
            userName: "",
            bookName: "",
            authorName: "",
            category: "",
            description: ""
        });
        setSubmitted(false);
    };

    // When user submits the form
    const handleSubmission = async (e) => {
        e.preventDefault(); // Prevent default page reload

        // Post form data to database
        try {
            const response = await fetch("http://localhost:5000/api/submit", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            const result = await response.json();
            if (response.ok) {
                setResponseMessage(result.message);
                setSubmitted(true);
            } else {
                setResponseMessage("Submission failed. Please try again.");
                setSubmitted(false);
            }
        } catch (error) {
            console.error("Error:", error);
            setResponseMessage("An error occurred. Please try again later.");
            setSubmitted(false);
        }
    };

    // Code to use 'useNavigate' hook
    // const navigate = useNavigate();  
    // const handleResult = () => {
    //     navigate('/display');  // Navigate to the display component
    // };

    return (
        <div className="form-container">
            <h1>Enter book details</h1>
            <form onSubmit={handleSubmission}>
                <div className="form-group">
                    <label htmlFor="userName">Enter your name: </label>
                    <input
                        type="text"
                        id="userName"
                        name="userName"
                        placeholder="Your name"
                        value={formData.userName}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="bookName">Enter book name: </label>
                    <input
                        type="text"
                        id="bookName"
                        name="bookName"
                        placeholder="Book name"
                        value={formData.bookName}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="authorName">Enter author name: </label>
                    <input
                        type="text"
                        id="authorName"
                        name="authorName"
                        placeholder="Author name"
                        value={formData.authorName}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="category">Enter book category: </label>
                    <input
                        type="text"
                        id="category"
                        name="category"
                        placeholder="e.g. Fiction, Non-fiction"
                        value={formData.category}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="description">Enter a short description: </label>
                    <textarea
                        id="description"
                        name="description"
                        placeholder="Brief description about the book"
                        value={formData.description}
                        onChange={handleChange}
                    />
                </div>

                <button type="submit">Submit</button>

                <button type="button" onClick={handleReset}>Reset</button>

                {/* <button type="button" onClick={handleResult}>Result</button> New Result button */}

                <Link to="/display">
                    <button type="button">Result</button>
                </Link>
            </form>

            {/* Display response message */}
            {responseMessage && (
                <div className={`response-message ${submitted ? "success" : "error"}`}>
                    <p>{responseMessage}</p>
                </div>
            )}

            {/* Display submitted form data only after it is successfully submitted to the database */}
            {submitted && (
                <div className="submitted-data">
                    <h3>Submitted data: </h3>
                    <b>Name: {formData.userName}</b><br />
                    <b>Book Name: {formData.bookName}</b><br />
                    <b>Author Name: {formData.authorName}</b><br />
                    <b>Category: {formData.category}</b><br />
                    <b>Description: {formData.description}</b>
                </div>
            )}
        </div>
    );
}

export default Form;
