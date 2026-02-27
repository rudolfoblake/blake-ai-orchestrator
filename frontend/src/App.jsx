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
    <div className="container">
      <section className="hero">
        <h1 className="title">Blake AI Orchestrator</h1>
        <p className="subtitle">Uma experiência fluida para explorar respostas de IA.</p>
      </section>

      <section className="panel">
        <label htmlFor="prompt" style={{ display: "block", marginBottom: 8, color: "var(--muted)" }}>
          Digite seu prompt
        </label>
        <textarea
          id="prompt"
          className="textarea"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Ex.: Explique o conceito de orquestração de modelos em IA..."
        />
        <div className="actions">
          <button className="button" onClick={handleSubmit} disabled={loading || !prompt.trim()}>
            {loading ? "Enviando…" : "Enviar"}
          </button>
          {error && <span className="error">{error}</span>}
        </div>

        <div className="response">
          <strong>Resposta:</strong>
          <div style={{ marginTop: 8 }}>{response || "—"}</div>
        </div>
      </section>
    </div>
  );
}