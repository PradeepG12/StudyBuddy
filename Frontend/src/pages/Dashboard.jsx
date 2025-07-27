// src/pages/Dashboard.jsx
import { Users, MessageCircle, Folder, Calendar } from "lucide-react";
import Sidebar from "../components/SideBard";
import DashboardCard from "../components/DashBoardCard";

const Dashboard = () => {
  return (
    <div className="flex">
      <Sidebar />
      <main className="flex-1 p-6 bg-gray-50 min-h-screen">
        <h1 className="text-3xl font-semibold mb-6">Welcome back 👋</h1>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <DashboardCard title="My Groups" count={3} icon={<Users />} />
          <DashboardCard title="Messages" count={12} icon={<MessageCircle />} />
          <DashboardCard title="Resources Shared" count={8} icon={<Folder />} />
          <DashboardCard title="Upcoming Tasks" count={2} icon={<Calendar />} />
        </div>

        {/* Optional: Add group list, announcements, calendar preview, etc. */}
      </main>
    </div>
  );
};

export default Dashboard;
