# RFC 0001 — Eventos de expedição (fictícia)

Status: Accepted
Implementação: Não iniciada

## Problema e motivação

Explorar envio desacoplado e proteção contra duplicação de solicitações.
O transporte atual não está demonstrado; esta RFC não afirma que ele falhou.

## Objetivos e não objetivos

Entregar solicitações rastreáveis e tolerar reentrega. Não redesenhar preço,
cancelamento ou implantar microsserviços.

## Contextos afetados

[Vendas](../../src/sales/context.md) produz a solicitação;
[Expedição](../../src/shipping/context.md) a interpreta como pedido de envio.

## Proposta

Publicar `ShipmentRequested` com `event_id`, `sales_order_id` e volume.
Deduplicar pelo identificador do evento, mantendo a relação com a venda.

## Alternativas consideradas

Chamada síncrona simplifica rastreio imediato, mas acopla disponibilidade.
Processamento por lote reduz infraestrutura de mensagens, com maior latência.
Manter o estado atual adia investimento, mas não define o transporte pretendido.

## Impactos e compatibilidade

Manter identificadores comerciais. A palavra “pedido” continua local a cada
contexto. Versionar o novo contrato antes de disponibilizá-lo a consumidores.

## Riscos

Reentrega pode duplicar envios; deduplicação e testes de repetição são necessários.

## Migração e reversão

Validar em ambiente isolado antes de ativação. Antes de tráfego real, a reversão
consiste em desativar o fluxo experimental. Reversão após despachos exige
reconciliação; seu procedimento ainda não foi definido.

## Estratégia de validação

Reentregar o mesmo evento e verificar apenas uma solicitação por `event_id`;
enviar eventos distintos da mesma venda e verificar volumes independentes.

## Questões abertas

Escolha de transporte, retenção de deduplicação e reconciliação após ativação.

## Resultado da discussão

A resposta inteiramente fictícia P6 em [discovery](../../discovery.md) aprova a
direção no cenário de teste. Não existe aprovação real nem implementação.

## Links relacionados

[ADR 0001](../adrs/0001-identidade-de-eventos.md) registra a decisão duradoura.
[Arquitetura vigente](../architecture/current.md) continua sem fluxo de eventos.
