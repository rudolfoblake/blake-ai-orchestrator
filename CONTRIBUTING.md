# Contribuindo para o projeto

Obrigado por querer contribuir! Este projeto é licenciado sob MIT e mantido por Rudolfo Blake. Abaixo estão as diretrizes para colaborar de forma eficiente e respeitosa.

## Princípios

- Respeito, colaboração e transparência.
- Discussões técnicas baseadas em fatos; feedback claro e educado.
- Qualidade > quantidade: mudanças pequenas e bem testadas.

## Como começar

1. Faça um fork e crie um branch descritivo:
   - `feat/<breve-descricao>` para novas funcionalidades
   - `fix/<breve-descricao>` para correções
   - `docs/<breve-descricao>` para documentação
   - `chore/<breve-descricao>` para tarefas operacionais
2. Configure o ambiente local:
   - Backend: `python -m pip install -r backend/requirements.txt`
   - Monitoring: `python -m pip install -r monitoring/requirements.txt`
   - Frontend: `npm install` (Node 18+)
3. Rodando localmente:
   - Backend: `python -m uvicorn backend.orchestrator.main:app --port 8000`
   - Monitoring: `python -m uvicorn monitoring.api.main:app --port 9100`
   - Frontend (opcional): `npm start`

## Commits e mensagens

Use um estilo inspirado em Conventional Commits:

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` documentação
- `chore:` manutenção
- `refactor:` mudança interna sem alterar comportamento

Exemplo: `feat(orchestrator): adicionar endpoint de inferência assíncrona`

## Pull Requests (PR)

Antes de abrir um PR:

- Descreva claramente o problema e a solução.
- Inclua passos de teste/validação (ex.: `/health`, `/docs`).
- Atualize a documentação quando aplicável (ex.: README, comentários).
- Mantenha o PR focado e pequeno quando possível.

Checklist rápida:

- [ ] Título claro e conciso
- [ ] Descrição com contexto e screenshots/logs quando relevante
- [ ] Validação local realizada (backend/monitoring/front)
- [ ] Sem arquivos gerados (ex.: `node_modules`, `.env`)

## Padrões de código

- Python: siga PEP 8 quando possível; nomes claros; funções pequenas.
- JavaScript/React: componentes funcionais, hooks, evitar efeitos colaterais.
- Evite mudanças não relacionadas no mesmo PR.

## Testes e validação

- Se houver testes, rode antes do PR. Se não houver, valide manualmente endpoints:
  - Backend: `GET /health` deve retornar `{"status":"ok"}`; `GET /docs` acessível.
  - Monitoring: `GET /health` e `GET /metrics` acessíveis.
- Verifique logs de inicialização sem erros.

## Reportar problemas

Abra uma issue com:

- Detalhes do ambiente (SO, versões, passos para reproduzir).
- Logs relevantes e contexto do erro.

## Segurança

Para vulnerabilidades, abra uma issue usando o rótulo `security`. Descreva de forma responsável e evite divulgar dados sensíveis.

## Licença

Ao contribuir, você concorda que suas contribuições são licenciadas sob a **MIT License**. Copyright (c) 2025 **Rudolfo Blake**.