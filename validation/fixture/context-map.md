# Mapa — cenário fictício

| Contexto | Responsabilidade | Código | Conhecimento | Conceitos e dados |
| --- | --- | --- | --- | --- |
| Vendas | Compromisso comercial | [sales](src/sales/service.py) | [contexto](src/sales/context.md) | Pedido comercial, itens, preço |
| Expedição | Separação e envio | [shipping](src/shipping/service.py) | [contexto](src/shipping/context.md) | Pedido de envio, volume, despacho |

## Integração e linguagem

Vendas → Expedição: `shipment_payload` expõe `sales_order_id` e itens. Expedição
depende desse identificador comercial para rastreio. O transporte efetivo não
está demonstrado pelo código disponível.

“Pedido” em Vendas é um compromisso comercial; em Expedição, uma solicitação de
envio de um volume. A tradução associa `order.id` a `sales_order_id`; não iguala
os identificadores locais. Uma venda pode originar vários pedidos de envio.
Esta diferença é legítima e não exige renomear o domínio de um dos contextos.
