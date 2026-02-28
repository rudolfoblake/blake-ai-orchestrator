# ⚙️ **Contributing to Blake Labs Projects**

Thank you for wanting to contribute.  
Blake Labs builds under three pillars: **Technology, Art & Integrity** — every commit must reflect those values.  
We value precision, transparency, and clean engineering. Every contribution shapes the ecosystem.

---

## 1. Core Principles
- Respect, collaboration, and security awareness.  
- Discussions based on data and logic — not ego.  
- Quality > Quantity: smaller, reliable commits over noisy changes.  
- If it breaks security or leaks data, it’s rejected instantly.

---

## 2. Getting Started
Fork the repository and create a descriptive branch:

- `feat/<short-description>` → new feature  
- `fix/<short-description>` → bug fix (for `staging`)  
- `hotfix/<short-description>` → urgent fix for `main`  
- `docs/<short-description>` → documentation  
- `chore/<short-description>` → maintenance  

Set up your local environment:

- Orchestrator → `cd orchestrator && python -m pip install -r requirements.txt`  
- Frontend → `cd frontend && npm install` (Node 18+)

Run locally:

- Orchestrator → `uvicorn app.main:app --port 8000`  
- Frontend → `npm start`

---

## 3. Commit Style
Follow **Conventional Commits** — clear, lowercase, and atomic.

Examples:
- `feat(api): add inference endpoint`
- `fix(db): correct transaction rollback on staging`
- `hotfix(auth): patch token validation on main`
- `docs(readme): clarify setup process`

Allowed prefixes → `feat`, `fix`, `hotfix`, `docs`, `chore`, `refactor`, `test`.

---

## 4. Pull Requests
Before submitting:

- Describe the issue and the logic behind your change.  
- Include testing steps (`/health`, `/metrics`, `/docs`, etc).  
- Update READMEs or CHANGELOGs when applicable.  
- Keep PRs focused, modular, and testable.  

**Quick checklist:**
- Title and context are clear  
- Relevant screenshots/logs attached if useful  
- Tested locally  
- No sensitive or temporary files committed (`.env`, `node_modules`, `.vercel`)  

---

## 5. Code Standards
- Python → follow PEP 8; use type hints and small, testable functions.  
- JavaScript/React → functional components and hooks; avoid side effects.  
- Security → never commit API keys, credentials, or URLs; secrets stay in `.env`; validate inputs and sanitize outputs.

---

## 6. Testing & Validation
Before merging:

- Run tests or validate endpoints manually:  
  - `/health` → `{"status": "ok"}`  
  - `/docs` → reachable  
- Logs must show no runtime or startup errors.

---

## 7. Reporting Issues
Open an issue including:

- Environment details (OS, versions, reproduction steps).  
- Logs or screenshots showing the problem.  
- For security vulnerabilities, use label `security` and report privately.

---

## 8. License
By contributing, you agree your code is licensed under **MIT License — © 2025 Blake Labs**.  
Your work becomes part of the collaborative foundation that defines Blake Labs.

---

# 🇧🇷 **Contribuindo para Projetos Blake Labs**

Obrigado por querer colaborar.  
A Blake Labs se baseia em três pilares: **Tecnologia, Arte e Integridade** — cada commit deve refletir esses valores.  
Valorizamos precisão, transparência e código limpo. Cada contribuição fortalece o ecossistema.

---

## 1. Princípios Fundamentais
- Respeito, colaboração e consciência de segurança.  
- Discussões guiadas por dados e lógica — não por ego.  
- Qualidade > Quantidade: commits pequenos, testados e significativos.  
- Se comprometer segurança ou privacidade, é rejeitado na hora.

---

## 2. Primeiros Passos
Faça um fork e crie um branch descritivo:

- `feat/<descricao>` → nova funcionalidade  
- `fix/<descricao>` → correção (para `staging`)  
- `hotfix/<descricao>` → correção urgente (para `main`)  
- `docs/<descricao>` → documentação  
- `chore/<descricao>` → manutenção  

Configure o ambiente local:

- Backend → `python -m pip install -r backend/requirements.txt`  
- Monitoring → `python -m pip install -r monitoring/requirements.txt`  
- Frontend → `npm install` (Node 18+)  
- Banco de Dados → veja `database/README.md` para configuração e migrações  

Rodando localmente:

- Backend → `python -m uvicorn backend.orchestrator.main:app --port 8000`  
- Monitoring → `python -m uvicorn monitoring.api.main:app --port 9100`  
- Frontend → `npm start`

---

## 3. Estilo de Commit
Siga o padrão **Conventional Commits** — limpo, claro e consistente.

Exemplos:
- `feat(api): adicionar endpoint de inferência`
- `fix(db): corrigir rollback de transação no staging`
- `hotfix(auth): corrigir validação de token no main`
- `docs(readme): ajustar instruções de instalação`

Prefixos válidos → `feat`, `fix`, `hotfix`, `docs`, `chore`, `refactor`, `test`.

---

## 4. Pull Requests
Antes de abrir um PR:

- Descreva o problema e a solução adotada.  
- Inclua passos de validação (`/health`, `/docs`, `/metrics`, etc).  
- Atualize README e CHANGELOG se necessário.  
- Mantenha o PR pequeno, coeso e com commits testados.  

**Checklist rápido:**
- Título e descrição claros  
- Prints/logs relevantes anexados  
- Testado localmente  
- Nenhum arquivo desnecessário (`.env`, `node_modules`, `.vercel`)  

---

## 5. Padrões de Código
- Python → seguir PEP 8; funções pequenas, tipadas e testáveis.  
- JavaScript/React → componentes funcionais e uso de hooks.  
- Segurança → nunca commitar chaves, tokens ou credenciais; `.env` deve conter variáveis sensíveis (fora do Git).

---

## 6. Testes e Validação
Antes do merge:

- Execute testes unitários/integrados.  
- Valide manualmente:  
  - `/health` → `{"status": "ok"}`  
  - `/docs` → acessível  
- Verifique logs sem erros.

---

## 7. Reporte de Problemas
Abra uma issue contendo:

- Detalhes do ambiente (SO, versões, passos de reprodução).  
- Logs e contexto do erro.  
- Para vulnerabilidades, use o rótulo `security` e reporte de forma privada.

---

## 8. Licença
Ao contribuir, você concorda que o código está sob **MIT License — © 2025 Blake Labs**.  
Cada contribuição faz parte da base colaborativa que sustenta a Blake Labs.
