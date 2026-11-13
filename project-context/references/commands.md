# Atalhos conversacionais

Interprete os atalhos do SKILL.md como intenção do usuário, aplicando o mesmo
fluxo e limites dos pedidos em linguagem natural. Não execute os atalhos no shell
nem trate argumentos como código. O texto após o atalho é o escopo da tarefa.
Não é preciso implementar um parser para o agente seguir esse roteamento.

## Invocação e compatibilidade

Com a skill já carregada, reconheça `/init`, `/discover` e os demais atalhos quando
forem a solicitação do usuário. Exemplos em documentos, citações ou código não são
instruções para executar esses modos. Se a skill estiver disponível no catálogo,
é possível pedir `$project-context /init`; sem instalação, use
“Leia project-context/SKILL.md e execute o atalho /init”.

Esta entrega não registra itens no menu de slash commands nem substitui comandos
nativos do aplicativo. Em particular, o Codex documenta um `/init` próprio para
gerar AGENTS.md; quando a interface interceptar o comando, use a frase explícita
acima para chegar à skill. Fonte consultada em 2026-11-13:
[documentação oficial](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex).

## Roteamento

- `/init`: inspecione primeiro; em projeto vazio/novo, descubra produto e stack.
  Se encontrar implementação existente, explique brevemente e siga `/discover`
  preservando o conteúdo, sem reinicializar ou apagar arquivos.
- `/discover`: inventarie o projeto e conduza a entrevista sobre capacidades,
  regras, limites e definições ausentes. Se o projeto for realmente vazio, siga
  a descoberta de produto e stack de `/init`.
- `/map`: produza ou refine o mapa com evidências, sem reorganizar código.
- `/context <nome ou problema>`: avalie necessidade e limites; não crie módulo
  nem implementação apenas por esse comando.
- `/refine <contexto ou tema>`: investigue cenários e consolide conhecimento.
- `/rfc <mudança>`: explore alternativas e crie proposta quando justificável;
  o atalho não autoriza implementação ou aprovação.
- `/adr <decisão>`: registre a decisão; o atalho por si só não comprova aceitação.
- `/update [escopo]`: inspecione alterações e sincronize os documentos afetados;
  sem escopo, use as alterações da tarefa/diff disponível. Se a base de comparação
  não for conhecida, explicite isso, sem inventar o que mudou.
- `/audit [escopo]`: reporte achados, evidências e impacto; só aplique correções
  quando também solicitadas. Registre no estado novos resultados de verificações
  quando pertinente, sem fingir que os defeitos encontrados foram corrigidos.
- `/state`: leia application-state.md e informe referência temporal e limites.
  Se ausente, diga que ainda não há estado registrado; não invente estado saudável.
- `/help`: apresente a tabela de atalhos e exemplos curtos, sem modificar arquivos.

Quando faltar argumento indispensável e o contexto não permitir inferi-lo, faça
uma pergunta curta. Não aplique ações abrangentes só porque o argumento foi omitido.
Atalho desconhecido deve ser explicado, sugerindo os existentes sem executar um
modo arbitrário. Não é preciso repetir uma intenção clara já dada em linguagem natural.

## Encerramento comum

Toda tarefa que modificar o projeto termina com a atualização de application-state.md,
independentemente do atalho usado ou de ter sido solicitada em linguagem natural.
Isso inclui alterações apenas documentais. Consolide uma entrada por tarefa com
escopo, autoria conhecida, evidências e limites; não uma entrada por operação de
arquivo. A obrigação persiste no AGENTS.md gerado/mesclado no projeto. Não é um
observador de mudanças feitas por terceiros entre execuções.
