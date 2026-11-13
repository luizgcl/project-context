# Exemplos curtos de uso

Com a skill disponível no ambiente: “Use $project-context para inicializar a documentação mínima deste repositório.” Sem instalação: “Leia project-context/SKILL.md e aplique o modo Auditar neste repositório.” O caminho explícito carrega instruções; não registra a skill no catálogo do aplicativo.

- “Mapeie os contextos deste monólito sem reorganizar código.”
- “Quero iniciar um projeto novo. Descubra o produto e me pergunte sobre a stack antes de registrar escolhas.”
- “Entenda a stack e as capacidades deste projeto existente; depois entreviste sobre regras e definições que faltam.”
- “Atualize application-state.md com o que você alterou e as verificações antes/depois, indicando o que não foi testado.”
- “Antes de implementar devoluções, investigue se precisamos de um contexto novo.”
- “Refine cancelamento em vendas com cenários e consolide o FAQ.”
- “Proponha alternativas de integração em uma RFC; não implemente.”
- “Registre em ADR esta decisão confirmada e vincule a RFC.”
- “Atualize somente a documentação afetada por este diff.”

## Atalhos e encerramento

Após carregar a skill, `/init` inicia a descoberta em projeto novo; `/discover`
entende um existente; `/refine cancelamento` aprofunda o tema; `/rfc eventos`
explora uma proposta. Veja a [lista completa](commands.md).

“Documente a regra de cancelamento” já implica atualizar application-state.md ao
concluir a alteração, sem que o usuário precise mencioná-lo. O mesmo vale para uma
correção de código autorizada por outra tarefa num projeto cujo AGENTS.md contenha
a obrigação de encerramento. `/state` apenas consulta o estado registrado.

## Exemplo fictício: mesma palavra, conceitos distintos

Todos os nomes, regras e respostas desta seção são fictícios.

| Contexto | Termo local “pedido” | Código | Responsabilidade |
| --- | --- | --- | --- |
| Vendas | Compromisso comercial com itens e preço aceitos | SalesOrder | Negociação e cancelamento comercial |
| Expedição | Solicitação de separação e envio de volumes | ShipmentRequest | Separação e despacho físico |

Um pedido de Vendas pode originar vários pedidos de Expedição. A integração traduz `SalesOrder.id` em `ShipmentRequest.sales_order_id`; os identificadores locais não são intercambiáveis. Não há contradição na palavra compartilhada.

Pergunta fictícia: “Cancelar em Vendas pode apagar um despacho já realizado?” Resposta simulada: “Não. Depois do despacho, é necessário um processo de devolução.” Consolidação: regra de não apagar despacho, FAQ explicando a necessidade de devolução, antipadrão de remover histórico com alternativa de registrar compensação. Se o código permitir apagar, registre divergência; não invente se a resposta ou o código deve prevalecer.

Para testar num projeto isolado, use dados sintéticos e registre claramente o que é simulação. Verificação mecânica de arquivos não equivale a validação de negócio ou avaliação autônoma do comportamento de um agente.
