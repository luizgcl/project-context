# Expedição — cenário fictício

## Propósito e limites

Possui separação e despacho de volumes. Não decide preço nem cancelamento
comercial. Fonte: [P2](../../discovery.md).

## Linguagem e integração

“Pedido” significa solicitação de envio de um volume (`shipment_request`), não
o compromisso comercial de [Vendas](../sales/context.md). Evite usar “venda” como
sinônimo dessa solicitação. `sales_order_id` liga cada pedido de envio à origem;
uma origem pode possuir vários volumes. Evidência: [construtor](service.py).

## Escopo refinado

Consultar o rastreio de volumes pertence a este contexto, conforme P3 das
[respostas fictícias](../../discovery.md). Não se criou um contexto separado:
não há responsabilidade nem ciclo de vida independente identificado.

## Contratos propostos

A [RFC de eventos](../../docs/rfcs/0001-eventos-de-expedicao.md) propõe
`ShipmentRequested` com identificação idempotente. Está Accepted na simulação,
mas não implementada; não é um contrato público vigente.
