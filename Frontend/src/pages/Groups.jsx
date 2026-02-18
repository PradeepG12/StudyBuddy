// src/pages/Groups.jsx

import { useState, useEffect } from "react";
import axios from "../utils/axios";
import GroupCard from "../components/GroupCard";

const Groups = () => {
  const [groups, setGroups] = useState([]);
  const [groupName, setGroupName] = useState("");

  const fetchGroups = async () => {
    const res = await axios.get("/groups/list/");
    setGroups(res.data);
  };

  const createGroup = async () => {
    if (!groupName.trim()) return;
    await axios.post("/groups/cud/", { name: groupName });
    setGroupName("");
    fetchGroups();
  };

  useEffect(() => {
    fetchGroups();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">My Groups</h1>

      <div className="flex gap-2 mb-6">
        <input
          type="text"
          className="border px-3 py-2 rounded w-full"
          placeholder="New Group Name"
          value={groupName}
          onChange={(e) => setGroupName(e.target.value)}
        />
        <button onClick={createGroup} className="bg-blue-600 text-white px-4 rounded">
          Create
        </button>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {groups.map((g) => (
          <GroupCard key={g.id} group={g} />
        ))}
      </div>
    </div>
  );
};

export default Groups;
