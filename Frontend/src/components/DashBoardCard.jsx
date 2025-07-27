// src/components/DashboardCard.jsx

const DashboardCard = ({ title, count, icon }) => {
  return (
    <div className="bg-white p-4 rounded-2xl shadow hover:shadow-lg transition-all flex items-center justify-between">
      <div>
        <h2 className="text-sm text-gray-500">{title}</h2>
        <p className="text-2xl font-bold">{count}</p>
      </div>
      <div className="text-blue-600">{icon}</div>
    </div>
  );
};

export default DashboardCard;
