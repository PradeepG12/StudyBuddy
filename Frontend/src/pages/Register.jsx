import { useState } from "react";                        // Importing React's useState hook to manage form data.
import { useNavigate } from "react-router-dom";         // For navigation after successful registration.

const Register = () => {
  const navigate = useNavigate();                       // Initialize navigation hook.
  
  const [formData, setFormData] = useState({            // State to hold form input values.
    name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;                   // Destructure name and value from input field.
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,                                    // Update state with changed input.
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();                                 // Prevent form refresh on submit.
    try {
      // TODO: Replace with actual API call.
      console.log("Registering user:", formData);       // Simulate API call by logging formData.
      // On success, redirect to login page
      navigate("/login");                               // Navigate to login page after success.
    } catch (err) {
      console.error("Registration failed", err);        // Handle error (placeholder).
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 rounded shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl font-bold mb-6 text-center">Register</h2>
        
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          className="w-full mb-4 px-4 py-2 border rounded"
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          className="w-full mb-4 px-4 py-2 border rounded"
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          className="w-full mb-6 px-4 py-2 border rounded"
        />

        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;
