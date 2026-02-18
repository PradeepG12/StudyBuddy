// src/components/GroupCard.jsx
import { useNavigate } from "react-router-dom";

const GroupCard = ({ group }) => {
  const navigate = useNavigate();
  return (
    <div className="bg-white p-4 rounded shadow border hover:shadow-lg transition-all">
      <h2 className="text-xl font-semibold mb-2">{group.name}</h2>
      <button
        onClick={() => navigate(`/chat/group/${group.id}`)}
        className="text-sm text-blue-600 hover:underline"
      >
        Enter Chat
      </button>
    </div>
  );
};

export default GroupCard;
