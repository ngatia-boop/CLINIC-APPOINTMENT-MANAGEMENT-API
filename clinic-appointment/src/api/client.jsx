// src/api/client.jsx
const BASE = import.meta.env.VITE_API_BASE || "https://clinic-appointment-management-api.onrender.com/";

async function fetchJSON(path, options = {}) {
  const url = `${BASE}${path}`; // ensure trailing slash in backend paths
  const res = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`API Error ${res.status}: ${text}`);
  }

  return res.json();
}

export default {
  get: (path) => fetchJSON(path),
  post: (path, data) =>
    fetchJSON(path, {
      method: "POST",
      body: JSON.stringify(data),
    }),
  put: (path, data) =>
    fetchJSON(path, {
      method: "PUT",
      body: JSON.stringify(data),
    }),
  patch: (path, data) =>
    fetchJSON(path, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),
  delete: (path) =>
    fetchJSON(path, {
      method: "DELETE",
    }),
};
