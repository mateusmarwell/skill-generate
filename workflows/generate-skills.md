# Generate Skills Workflow

Este arquivo dita as regras e comandos para o bot executar o plugin `spec-skill-generator`.

## Comandos Disponíveis

- `/generate-skills`
  - **Comportamento Padrão**: Se o manifesto `.agents/skills/.spec-skill-manifest.json` não existir, executa o modo `generate`. Se o manifesto existir, executa o modo `regenerate`.
- `/generate-skills generate`
  - Cria as 4 skills (`architect`, `backend`, `frontend`, `tester`) pela primeira vez, lendo a documentação e detectando a stack.
- `/generate-skills regenerate`
  - Lê a documentação atualizada e código fonte e atualiza apenas os blocos `SPEC-GENERATED` dentro das 4 skills, preservando qualquer conteúdo em `SPEC-CUSTOM`.
- `/generate-skills check`
  - Apenas analisa a stack e as mudanças entre fontes e manifesto, informando (dry-run) quais alterações aconteceriam sem modificar nenhum arquivo.
- `/generate-skills force`
  - Força a regeneração de todas as skills, ignorando o estado atual do hash no manifesto.

## Ações Exigidas ao Executar Comandos
O agente deve:
1. Invocar internamente a skill `spec-skill-generator`.
2. Seguir as regras de preservação de blocos descritas em `regeneration-rules.md`.
3. Informar ao usuário os arquivos criados/modificados/preservados e qualquer conflito encontrado.
4. Passar pela validação obrigatória usando `validate-generated-skills.py`.
