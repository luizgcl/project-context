# Estado da aplicação

Mantenha `application-state.md` na raiz, ou o equivalente canônico já existente.
Use o [template](../assets/templates/application-state.md). O documento responde:
o que existe, o que mudou, quem alterou quando conhecido, o que foi verificado e
o que continua com falha ou desconhecido. Referencie regras, arquitetura e decisões
em vez de copiá-las. Não registre segredos, dumps de logs ou uma cópia completa do diff.

## Linha de base antes da mudança

Leia o estado anterior e compare sua revisão/data com o checkout atual. Inspecione
status e diff do Git quando disponível: diferencie alterações já presentes das
que o agente fará. Não atribua ao agente mudanças preexistentes ou de origem
desconhecida. Sem Git, use caminhos, observações e identificador da execução; não
invente commits, autores ou datas anteriores.

Registre stack e versões com sua fonte (planejada, declarada ou executada),
capacidades implementadas/parciais/planejadas e limites observados. Em projeto
novo sem implementação, diga isso explicitamente; testes e execução ainda não
se aplicam. Stack decidida não comprova dependências instaladas.

Identifique verificações pertinentes à alteração: testes, build, lint, smoke ou
fluxos manuais, conforme existirem e forem viáveis. Capture a linha de base antes
de alterar quando possível. Não execute procedimentos destrutivos ou contra
produção só para preencher a tabela. Se não puder verificar, registre o motivo.

## Depois de qualquer mudança — obrigação do agente

Atualize este documento antes de encerrar toda tarefa que alterar o projeto,
inclusive somente documentação, configuração, dependências ou testes. Não espere
que o usuário peça isso ou use `/update`: é parte do encerramento, também para
pedidos em linguagem natural. Consolide as alterações da tarefa em um registro
proporcional, sem recursão ao editar o próprio estado. Se o arquivo não existir,
crie uma linha de base honesta; sem evidência anterior, marque-a como desconhecida.
Consultas sem mudanças não exigem registro. Se a escrita estiver impedida, exponha
a pendência e o motivo na resposta final.

Compare o diff final com a linha de base e execute verificações proporcionais ao
impacto, usando comandos reais. Registre comando/procedimento, diretório, ambiente,
revisão e resultado observado, incluindo falhas e verificações não executadas.
Relacione cada mudança aos caminhos/capacidades afetados e aos resultados.

| Evidência | Conclusão permitida |
| --- | --- |
| Mesmo teste passa antes e falha depois, em condições comparáveis | Regressão observada nessa verificação; investigar causa no diff, sem atribuição automática. |
| Falha antes e depois | Falha preexistente que permanece. |
| Não há execução anterior comparável | Falha atual, origem indeterminada. |
| Verificações pertinentes passam | Sem falhas detectadas no escopo verificado; não garante ausência de bugs. |
| Verificação não executada ou bloqueada | Estado não verificado, com motivo; nunca “aprovado”. |

Registre separadamente uma divergência de regra encontrada por leitura e uma
falha reproduzida. Não invente uma execução para provar que algo quebrou.

## Estrutura e manutenção

Mantenha um resumo atual e um histórico conciso de mudanças significativas:
referência/data conhecida, autoria comprovada (inclusive agente na execução
atual), o que mudou, por quê, caminhos e verificações/pendências. Use links para
commits, PRs ou relatórios existentes quando disponíveis. Atribuição sem fonte
fica como desconhecida. Não crie registros duplicados em execução sem novidades.

Preserve falhas abertas até evidência de resolução e mantenha histórico de sua
correção. Uma nova verificação não deve apagar a evidência anterior necessária à
comparação. Para históricos extensos, preserve os detalhes em registros existentes
ou arquivo histórico vinculado, mantendo o resumo atual legível.

Inclua em AGENTS.md o roteamento: consultar estado antes de alterações e atualizá-lo
após qualquer alteração, sem pedido adicional, com evidências e limitações. Isso orienta as próximas
execuções; não instala observador, CI ou atualização automática em background.
