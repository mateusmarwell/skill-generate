# Regras de Regeneração (Regenerate Mode)

Quando executado o comando `/generate-skills regenerate`, a skill principal `spec-skill-generator` deverá processar a documentação novamente e aplicar as modificações estritamente dentro destas regras:

## 1. Tratamento de Blocos
- **Blocos Gerados (`SPEC-GENERATED`)**: Podem ser sobrescritos integralmente pelos novos dados lidos do `.spec/init` ou do projeto.
- **Blocos Customizados (`SPEC-CUSTOM`)**: Nunca devem ser sobrescritos, excluídos, nem alterados pela automação. Eles pertencem ao desenvolvedor humano.

## 2. Tecnologias Substituídas ou Obsoletas
- Se uma tecnologia for detectada como substituída (ex: O código parou de usar MySQL e agora usa PostgreSQL), não apague silenciosamente as regras anteriores se houver conteúdo manual associado.
- Adicione uma nota de que a tecnologia foi descontinuada para a skill que a consumia e anote no manifesto a obsolescência.

## 3. Ausência de Marcadores
- Se o arquivo existir e não contiver nenhum bloco `SPEC-*`, **crie um backup** (ex: `SKILL.md.bak`) do conteúdo e não aplique as substituições até que o desenvolvedor organize os blocos.
- Informe ao desenvolvedor que os arquivos estão fora do padrão.

## 4. Diferencial de Conteúdo
- Não escreva o arquivo inteiro a menos que haja mudanças. Compare as informações novas com o arquivo atual ou com a hash das fontes guardada no manifesto.
