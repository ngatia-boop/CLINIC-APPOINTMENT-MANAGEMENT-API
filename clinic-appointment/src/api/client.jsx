// src/api/client.jsx
const BASE = import.meta.env.VITE_API_BASE;

export async function fetchJSON(path, options = {}) {
  if (!BASE) throw new Error("API base URL is not defined. Check your .env or Vercel environment variables.");

  const res = await fetch(`${BASE}${path}`, options);
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`API Error ${res.status}: ${text}`);
  }
  return res.json();
}
