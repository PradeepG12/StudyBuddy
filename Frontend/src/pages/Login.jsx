// src/pages/Login.jsx
import { useState } from "react";
import { useAuth } from "../context/AuthContext";
import axios from "../utils/axios";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("/login/", { email, password });
      
      const { access_token, refresh_token, user } = res.data.data;

      // ✅ Save tokens and user info to localStorage
      localStorage.setItem("access_token", access_token);
      localStorage.setItem("refresh_token", refresh_token);
      localStorage.setItem("user_id", user);

      login(access_token, refresh_token, user);

      // login(res.data.token); // Adjust based on your API response
      navigate("/dashboard");
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <div className="p-8 max-w-md mx-auto">
      <h1 className="text-xl mb-4">Login</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" className="w-full p-2 border" />
        <input value={password} onChange={e => setPassword(e.target.value)} type="password" placeholder="Password" className="w-full p-2 border" />
        <button type="submit" className="bg-blue-500 text-white w-full p-2">Login</button>
      </form>
    </div>
  );
};

export default Login;
