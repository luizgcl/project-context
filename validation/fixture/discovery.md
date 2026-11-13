# Roteiro e respostas inteiramente fictícias

Este arquivo é material de teste, não uma entrevista real ou validação de negócio.
As referências P1–P6 identificam respostas simuladas, sem atribuição a pessoas reais.

## Primeira execução — inicializar

Inspeção: duas pastas com funções de venda e expedição. O código permite cancelar
em `paid` e `shipped`. As pastas são indícios; a separação de responsabilidade foi
estabelecida pela simulação abaixo, não inferida só de seus nomes.

P1 — Pergunta: qual resultado o produto deve entregar e para quem?
Resposta fictícia: compradores compram; operadores acompanham venda e entrega,
com rastreio de volumes até a venda. Não fazemos otimização de rotas.

P2 — Pergunta adaptada: quem possui o compromisso comercial e quem possui o envio?
Resposta fictícia: Vendas possui itens e preço; Expedição possui volumes e despacho.
Ambos usam “pedido”, com os significados distintos descritos no mapa.

Síntese simulada: dois contextos num repositório, sem assumir microsserviços;
escopo comercial e envio, política de devolução pendente. Documentação mínima
criada sem criar novos módulos nem mover código.

## Segunda execução — refinar e investigar novo módulo

P3 — Pergunta: precisamos de um novo contexto para rastreio, ou isso pertence a
Expedição, que já possui o envio?
Resposta fictícia: queremos apenas consultar os volumes existentes; Expedição
já tem a responsabilidade. Não há novo ciclo de vida nem dados próprios.
Conclusão simulada: documentar essa capacidade em Expedição, sem novo módulo.

P4 — Pergunta: se o volume já foi despachado, o cancelamento pode apagar o envio?
Resposta fictícia: não; o despacho deve continuar registrado e o caso segue para
devolução. Antes do despacho, cancelamento é permitido. Nenhuma exceção é conhecida.

P5 — Pergunta adaptada: qual problema a remoção do despacho causaria?
Resposta fictícia: perderíamos o rastreio do que saiu fisicamente. Registrar uma
devolução preserva o histórico. Seu procedimento detalhado ainda será definido.

Divergência a devolver ao usuário: a resposta P4 proíbe cancelamento após despacho,
mas `can_cancel` aceita `shipped`. Qual fonte representa a regra desejada e como
compatibilizar clientes existentes? A simulação não responde; a questão permanece
aberta e nenhuma implementação será alterada.

P6 — Pergunta: a entrega idempotente por evento pode ser aceita como direção,
mantendo a implementação para outra tarefa?
Resposta fictícia: no cenário de teste, aprovamos essa proposta e a decisão de
identificar eventos; não iniciamos implementação. Isso sustenta Accepted somente
dentro desta fixture fictícia.

Síntese simulada: manter dois contextos, rastreio em Expedição; preservar despacho;
proposta de eventos aceita ficticiamente, ainda não implementada; divergência de
cancelamento e procedimento de devolução pendentes. Esta síntese permitiria
correções numa entrevista real; não existe aprovação real atribuída a alguém.
