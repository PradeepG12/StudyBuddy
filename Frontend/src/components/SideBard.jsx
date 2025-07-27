// src/components/Sidebar.jsx
import { Home, Users, MessageCircle, Folder } from "lucide-react";
import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="h-screen w-64 bg-white shadow-md p-4 border-r">
      <h1 className="text-2xl font-bold mb-6">StudyBuddy+</h1>
      <nav className="flex flex-col gap-4">
        <Link to="/dashboard" className="flex items-center gap-2 text-gray-700 hover:text-blue-600">
          <Home size={20} /> Dashboard
        </Link>
        <Link to="/groups" className="flex items-center gap-2 text-gray-700 hover:text-blue-600">
          <Users size={20} /> My Groups
        </Link>
        <Link to="/chat" className="flex items-center gap-2 text-gray-700 hover:text-blue-600">
          <MessageCircle size={20} /> Chat
        </Link>
        <Link to="/resources" className="flex items-center gap-2 text-gray-700 hover:text-blue-600">
          <Folder size={20} /> Resources
        </Link>
      </nav>
    </div>
  );
};

export default Sidebar;
