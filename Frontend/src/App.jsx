import './App.css'
import { Routes, Route } from "react-router-dom";

import { AuthProvider } from "./context/AuthContext";

import PrivateRoute from "./components/PrivateRoute";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from './pages/Dashboard';
import Groups from './pages/Groups';
import ChatRoom from './pages/ChatRoom';

const App = () => {
  return (
    <AuthProvider>
      <Routes>
        <Route
          path="*"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/groups"
          element={
            <PrivateRoute>
              <Groups />
            </PrivateRoute>
          }
        />
        <Route
          path="/chat/group/:group_id"
          element={
            <PrivateRoute>
              <ChatRoom />
            </PrivateRoute>
          }
        />

        {/* Private route: Dashboard, only visible if logged in */}
      </Routes>
    </AuthProvider>
  );
};


export default App
