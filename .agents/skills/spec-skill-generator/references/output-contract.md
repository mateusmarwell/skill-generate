# Contrato de Saída das Skills Geradas

As quatro skills geradas (`architect`, `backend`, `frontend`, `tester`) devem obedecer rigorosamente a esta estrutura de blocos e convenções de preenchimento.

## Estrutura Obrigatória de SKILL.md

```markdown
---
name: [Nome da Skill, ex: myproject-backend]
description: [Descrição focada nas responsabilidades da skill detectada]
---

# Objetivo
[Descrição curta da skill no contexto do projeto]

## Tecnologias e Stack (Evidence-based)
<!-- BEGIN SPEC-GENERATED: detected-stack -->
- Linguagem: [Detectada]
- Framework: [Detectado]
<!-- END SPEC-GENERATED: detected-stack -->

## Regras de Negócio
<!-- BEGIN SPEC-GENERATED: business-rules -->
- Regra 1...
<!-- END SPEC-GENERATED: business-rules -->

## Comandos Reais (Detectados)
<!-- BEGIN SPEC-GENERATED: commands -->
- Testes: `[comando detectado]`
<!-- END SPEC-GENERATED: commands -->

## Regras Customizadas Manuais (Não apague)
<!-- BEGIN SPEC-CUSTOM: project-rules -->
[Espaço reservado para o desenvolvedor colocar regras manuais persistentes]
<!-- END SPEC-CUSTOM: project-rules -->

## Decisões Técnicas de Engenharia
<!-- BEGIN SPEC-CUSTOM: engineering-decisions -->
[Espaço para registrar logs de decisões feitas que não devem ser perdidas na regeneração]
<!-- END SPEC-CUSTOM: engineering-decisions -->
```

## Regras por Skill

1. **Architect:** Focar em separar módulos, dependências permitidas, arquitetura documentada e conflitos potenciais de integração.
2. **Backend:** Focar em controllers, validações, persistência, banco de dados (se detectado) e integrações do lado do servidor.
3. **Frontend:** Focar em frameworks (se detectado), componentes, chamadas e contratos de rotas, estados e UI/UX/Acessibilidade.
4. **Tester:** Transformar cenários da especificação em uma matriz clara de pré-condições, entradas e saídas e relacionar com o framework de testes (se detectado). Se não detectar ferramentas, recomendar criação manual de scripts.
