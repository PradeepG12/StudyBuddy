// src/pages/ChatRoom.jsx
import { useEffect, useState, useRef } from "react";
import { useParams } from "react-router-dom";

const ChatRoom = () => {
  const { id } = useParams(); // group id
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const socketRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/ws/chat/group/${id}/`);
    socketRef.current = ws;

    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setMessages((prev) => [...prev, data]);
    };

    return () => ws.close();
  }, [id]);

  const sendMessage = () => {
    if (input.trim()) {
      socketRef.current.send(JSON.stringify({ message: input }));
      setInput("");
    }
  };

  return (
    <div className="flex flex-col h-screen p-6">
      <h1 className="text-xl font-bold mb-4">Group Chat</h1>
      <div className="flex-1 overflow-y-auto border p-4 bg-white rounded">
        {messages.map((msg, i) => (
          <div key={i} className="mb-2">
            <span className="font-semibold">{msg.user || "Anon"}:</span>{" "}
            {msg.message}
          </div>
        ))}
      </div>

      <div className="flex gap-2 mt-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="border px-3 py-2 rounded w-full"
          placeholder="Type a message"
        />
        <button onClick={sendMessage} className="bg-blue-600 text-white px-4 rounded">
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatRoom;
