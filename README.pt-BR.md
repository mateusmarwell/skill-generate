# Skill Generation Plugin

Este repositório contém o plugin `skill-generation` para o Google Antigravity. Este plugin foi desenvolvido para ser estritamente **agnóstico de stack e de linguagem**.

## Objetivo

Transformar o projeto em skills ativas e atualizáveis que orientam os agentes de IA, com guardrails não-destrutivos integrados para proteger sistemas legados e em produção:

1. **Arquiteto**: Decisões técnicas, organização de módulos, continuidade estrutural, preservação de lockfiles e portabilidade de caminhos. (Sempre gerado)
2. **Tester**: Transformar critérios de aceite em cenários de teste com paridade do runner detectado e compatibilidade com CI/CD. (Sempre gerado)
3. **Segurança**: Postura de segurança, prevenção ao OWASP Top 10, gestão de segredos, sanitização de inputs e proteção/redação de PII em logs. (Sempre gerado)
4. **Backend**: Persistência, validações, controllers, imutabilidade de contratos de API, migrations não-destrutivas e queries limitadas (sem N+1). (Gerado APENAS se evidências de backend forem encontradas)
5. **Frontend**: Componentes, UI/UX, consistência de estilos, continuidade de padrões de componentes e preservação do layout global. (Gerado APENAS se evidências de UI/Frontend forem encontradas)

### Modos de Operação
- **Spec-Driven**: Se o projeto possuir o diretório `.spec/init/` (especificação viva), o plugin consumirá esses contratos formais para gerar as skills.
- **Code-Driven (Legacy/Fallback)**: Se não houver especificação, o plugin entrará automaticamente no modo de engenharia reversa, analisando profundamente o código fonte, configurações de pacotes e estrutura de pastas para inferir a arquitetura e as regras de negócio.

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
