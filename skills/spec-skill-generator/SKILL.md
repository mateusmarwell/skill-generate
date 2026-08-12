---
name: spec-skill-generator
description: Lê a especificação e os arquivos relevantes do projeto, detecta a stack atual e gera ou atualiza skills de arquiteto, backend, frontend e tester. Use quando requisitos, arquitetura, tecnologias, regras de negócio, critérios de aceite ou configuração do projeto forem alterados.
---

# spec-skill-generator

Esta skill lê a documentação viva e o código do projeto para descobrir dinamicamente a stack de tecnologias, regras de negócio e arquitetura, gerando quatro skills especializadas (architect, backend, frontend, tester) para atuar no projeto.

## Objetivo
Transformar a especificação do projeto em quatro skills vivas, atualizáveis e agnósticas a tecnologias fixas.

## Fluxo de Execução

1. **Ler Especificação:**
   - Procure arquivos relevantes, prioritariamente na pasta `.spec/init/`, como descrições de projeto, requisitos, histórias de usuário, modelo de dados e decisões técnicas.
   - A especificação não tem um formato estrito, analise os arquivos que existirem.

2. **Descoberta Dinâmica de Stack (Evidence-based):**
   - Inspecione arquivos no repositório (ex: `package.json`, `pom.xml`, `go.mod`, `Dockerfile`, `.yml`, etc.) e configurações (testes, builds, db) para inferir tecnologias reais.
   - Diferencie o "estado desejado" (especificação) do "estado atual" (código).
   - **IMPORTANTE:** Não assuma nenhuma linguagem (ex: JS, TS, Python, Go) ou framework antecipadamente. Apenas use o que encontrar com evidências concretas.

3. **Gerar as Quatro Skills:**
   - Com base nos dados encontrados, gere/atualize 4 arquivos de skill em `.agents/skills/`:
     - `<project>-architect/SKILL.md`: Focado na arquitetura geral.
     - `<project>-backend/SKILL.md`: Focado em desenvolvimento backend e banco de dados.
     - `<project>-frontend/SKILL.md`: Focado no desenvolvimento da interface.
     - `<project>-tester/SKILL.md`: Focado em cenários de teste, unitários e E2E.
   - Utilize o nome detectado do projeto para nomear as pastas. Se não encontrar o nome, prefixe com `project-`.
   - Consulte `references/output-contract.md` para o formato esperado.

4. **Regeneração (Regenerate Mode):**
   - Siga as regras em `references/regeneration-rules.md`.
   - Substitua APENAS o conteúdo dos blocos marcados com `SPEC-GENERATED`.
   - PRESERVE integralmente os blocos marcados com `SPEC-CUSTOM`.
   - Se os marcadores não existirem, faça backup antes de atualizar.
   - Atualize apenas as mudanças reais em vez de reescrever todo o arquivo.

5. **Gerenciar Conflitos:**
   - Se houver disparidade entre fontes (ex: Documentação diz X, código usa Y) não adivinhe nem altere arquivos-fonte silenciosamente.
   - Crie/Registre em `SPEC_CONFLICTS.md` no diretório do projeto, informando o conflito, e exiba no final.

6. **Atualizar Manifesto:**
   - Mantenha `.agents/skills/.spec-skill-manifest.json` seguindo o schema em `references/manifest-schema.json`.
   - Atualize fontes usadas, ignoradas, ausentes, stack, e o que mudou.

7. **Validar Arquivos Gerados:**
   - Execute o script `scripts/validate-generated-skills.py` e verifique a integridade (frontmatter YAML, blocos preservados, consistência).
   - Não finalize sem passar por todas as validações com sucesso.

8. **Relatório Final:**
   - Exiba as tecnologias detectadas, arquivos alterados/preservados, conflitos e status do git.
