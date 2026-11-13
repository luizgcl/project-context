# Instruções do projeto fictício

Preserve os identificadores públicos usados nas integrações.

## Documentação

Consulte [produto](product.md) e [mapa](context-map.md) quando relevantes.
Antes de alterar `src/sales`, leia [Vendas](src/sales/context.md); antes de alterar
`src/shipping`, leia [Expedição](src/shipping/context.md). Este roteamento é explícito;
não depende de descoberta automática de instruções aninhadas.

Consulte decisões aceitas e propostas pertinentes no [índice](docs/README.md),
respeitando os status. Atualize documentação cujo significado mudar e apresente
conflitos com suas fontes. Não há comando de teste configurado neste repositório
sintético; não invente um comando de projeto.

Consulte o [estado da aplicação](application-state.md) antes de mudanças. Depois,
registre alterações atribuíveis à execução, verificações antes/depois e pendências;
não trate estado não verificado como saudável.

A atualização do estado é obrigatória antes da resposta final de qualquer tarefa
que altere código, testes, configuração, dependências ou documentação, sem esperar
pedido do usuário ou `/update`. Consultas sem mudanças não geram registro; a edição
do próprio estado não gera uma nova entrada recursiva. Se a atualização estiver
impedida, informe a pendência e o motivo.
