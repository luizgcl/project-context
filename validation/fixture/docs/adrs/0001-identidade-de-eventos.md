# ADR 0001 — Identidade de eventos (fictício)

Status: Accepted

## Contexto e problema

A [RFC 0001](../rfcs/0001-eventos-de-expedicao.md) propõe entrega de solicitações
que pode sofrer repetição. Uma venda pode originar vários envios.

## Decisão

Adotar `event_id` como identidade da solicitação para deduplicação. Aceitação
sustentada apenas por P6 das [respostas fictícias](../../discovery.md).
Implementação não iniciada; isto não descreve o código atual.

## Alternativas e motivos

Deduplicar por venda impediria volumes independentes. Não deduplicar permitiria
duplicar a solicitação em reentregas. O evento distingue repetição de nova intenção.

## Consequências e trade-offs

Permite repetição segura, mas exige armazenar identidades processadas e definir
retenção. O custo operacional ainda precisa ser validado.

## Contextos afetados

[Vendas](../../src/sales/context.md) gera a identidade;
[Expedição](../../src/shipping/context.md) a usa para deduplicar.

## Links relacionados

[Código atual de Expedição](../../src/shipping/service.py) não implementa a decisão.
