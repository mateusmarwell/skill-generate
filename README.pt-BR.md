# Spec Skill Generator Plugin

Este repositório contém o plugin `spec-skill-generator` para o Google Antigravity. Este plugin foi desenvolvido para ser estritamente **agnóstico de stack e de linguagem**.

## Objetivo

Transformar a especificação viva do projeto (normalmente localizada em `.spec/init/`) em skills ativas e atualizáveis que orientarão os agentes da IA:

1. **Architect**: Decisões técnicas e organização de módulos.
2. **Backend**: Persistência, validações e controllers (se aplicável).
3. **Frontend**: Componentes, UI/UX e consumo de rotas (se aplicável).
4. **Tester**: Transformação de critérios de aceite e histórias em cenários de testes.

## Estrutura do Plugin

- `skills/generate-skills/SKILL.md`: A skill principal que aciona a geração.
- `skills/generate-skills/references/`: Regras de preservação (`regeneration-rules.md`), contrato de saída (`output-contract.md`) e schema de manifesto (`manifest-schema.json`).
- `skills/generate-skills/scripts/validate-generated-skills.py`: Script Python usado para garantir a integridade das skills geradas.

## Como Usar (Skills)

No chat do Antigravity, basta digitar `/` para ver as skills nativas no autocompletar:

- `/generate-skills` - Identifica automaticamente se deve gerar (novo projeto) ou regenerar (projeto existente).
- `/check-skills` - Realiza um "dry-run" (teste) sem modificar arquivos.
- `/force-generate-skills` - Força a recriação ignorando o hash no manifesto.
- `/generate-skill-suggest` - Cria skills extras especializadas sugeridas pela IA com base na infraestrutura do projeto.

## Customização e Segurança

Todas as skills geradas utilizam blocos marcados com `<!-- BEGIN SPEC-GENERATED: ... -->` e `<!-- BEGIN SPEC-CUSTOM: ... -->`.
Durante uma regeneração, **apenas o conteúdo gerado** é substituído, garantindo que as regras e notas de engenharia manuais do desenvolvedor nunca sejam perdidas.
