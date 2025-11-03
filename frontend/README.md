# Blake AI Frontend

## Setup

- Instale dependências:
  - `npm install`
- Crie `.env.local` (opcional):
  - `REACT_APP_API_URL=http://localhost:8000`
- Rode o projeto:
  - `npm start`

## Integração

### Desacoplamento
- O frontend é plugável: basta apontar `REACT_APP_API_URL` para qualquer backend compatível.
- A comunicação é feita via REST (`POST /infer`), sem dependência de bundler/específico.

### API
- A função `infer()` em `src/services/api.js` conecta ao endpoint `/infer` do backend e retorna `final_answer`.
- Body: `{ "prompt": "Seu texto aqui" }`
- Resposta: `{ "final_answer": string, "confidence": number, "sources": { provider: text } }`

### Docker
- Também pode ser executado via Docker Compose junto ao backend: `docker compose up --build`