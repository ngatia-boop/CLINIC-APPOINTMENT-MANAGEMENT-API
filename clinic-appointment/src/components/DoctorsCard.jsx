export default function DoctorsCard({ doctor, onDelete, onUpdate }) {
  return (
    <div className="p-4 bg-white rounded-xl shadow flex flex-col gap-2">
      <h2 className="text-lg font-bold">{doctor.name}</h2>
      <p>Specialization: {doctor.specialization}</p>
      <p>Phone: {doctor.phone}</p>
      <div className="flex gap-2 mt-2">
        <button
          onClick={() => onUpdate && onUpdate(doctor)}
          className="px-3 py-1 bg-yellow-500 text-white rounded-lg hover:bg-yellow-600 transition"
        >
          Edit
        </button>
        <button
          onClick={() => onDelete && onDelete(doctor.id)}
          className="px-3 py-1 bg-red-600 text-white rounded-lg hover:bg-red-700 transition"
        >
          Delete
        </button>
      </div>
    </div>
  );
}
