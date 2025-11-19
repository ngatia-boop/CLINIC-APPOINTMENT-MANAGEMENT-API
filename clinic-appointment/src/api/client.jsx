const BASE = import.meta.env.VITE_API_BASE || "https://clinic-appointment-management-api-3.onrender.com";

export async function fetchJSON(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, options);
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`API Error ${res.status}: ${text}`);
  }
  return res.json();
}
