import { useState } from "react";                        
import { useNavigate } from "react-router-dom";         
import axiosInstance from "../utils/axios";

const Register = () => {
  const navigate = useNavigate();                       
  
  const [formData, setFormData] = useState({            
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;                   
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,                                    
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();                                 
    try {
      console.log("Registering user:", formData);       
      const payload = {
        first_name: formData.first_name,
        last_name: formData.last_name,
        email: formData.email,
        password: formData.password
      }
      await axiosInstance.post("/signup/", payload)
      navigate("/login");                               
    } catch (err) {
      console.error("Registration failed", err);        
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
          name="fisrt_name"
          placeholder="First Name"
          value={formData.first_name}
          onChange={handleChange}
          className="w-full mb-4 px-4 py-2 border rounded"
        />

        <input
          type="text"
          name="last_name"
          placeholder="Last Name"
          value={formData.last_name}
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
