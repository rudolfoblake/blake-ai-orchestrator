export const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export async function infer(prompt) {
  const res = await fetch(`${API_URL}/infer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`HTTP ${res.status}: ${text}`);
  }
  return res.json();
}