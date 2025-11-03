# Blake AI Frontend

## Setup

- Install dependencies:
  - `npm install`
- Create `.env.local` (optional):
  - `REACT_APP_API_URL=http://localhost:8000`
- Run the project:
  - `npm start`

## Integration

### Decoupling
- Frontend is pluggable: just point `REACT_APP_API_URL` to any compatible backend.
- Communication is via REST (`POST /infer`), with no bundler-specific dependency.

### API
- The `infer()` function in `src/services/api.js` hits the backend `/infer` endpoint and returns `final_answer`.
- Body: `{ "prompt": "Your text here" }`
- Response: `{ "final_answer": string, "confidence": number, "sources": { provider: text } }`

### Docker
- Can be run with Docker Compose alongside the backend: `docker compose up --build`

---

## PT-BR

### Setup
- Instale dependências: `npm install`
- Crie `.env.local` (opcional): `REACT_APP_API_URL=http://localhost:8000`
- Rode: `npm start`

### Integração
- O frontend é plugável: basta apontar `REACT_APP_API_URL` para qualquer backend compatível.
- Comunicação via REST (`POST /infer`), sem dependência de bundler específico.

### API
- A função `infer()` em `src/services/api.js` chama `/infer` no backend e retorna `final_answer`.
- Body: `{ "prompt": "Seu texto aqui" }`
- Resposta: `{ "final_answer": string, "confidence": number, "sources": { provider: text } }`

### Docker
- Também pode ser executado via Docker Compose com o backend: `docker compose up --build`