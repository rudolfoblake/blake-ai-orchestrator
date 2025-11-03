import React, { useState } from "react";
import { infer } from "./services/api";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await infer(prompt);
      setResponse(result.final_answer);
    } catch (e) {
      setError(e.message || "Error calling API");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Blake AI Orchestrator</h1>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      <button onClick={handleSubmit} disabled={loading || !prompt.trim()}>
        {loading ? "Sending..." : "Send"}
      </button>
      {error && <div style={{ color: "red" }}>{error}</div>}
      <p><b>Response:</b> {response}</p>
    </div>
  );
}