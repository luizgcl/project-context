# Vendas — cenário fictício

## Propósito e limites

Possui compromisso comercial, itens e preço. Não possui despacho físico, que cabe
à [Expedição](../shipping/context.md). Fonte: [P2](../../discovery.md).

## Linguagem

| Termo | Significado local | Sinônimo evitado | Outro contexto | Código |
| --- | --- | --- | --- | --- |
| Pedido | Compromisso comercial | Pedido de envio | Em Expedição é solicitação de envio | `order` |

## Nota existente a preservar

O identificador comercial continua estável durante todo o atendimento.

## Comportamento observado

[can_cancel](service.py) aceita estados `paid` e `shipped`. Isso descreve a
implementação observada; a política desejada será refinada com cenários.

## Regras declaradas na simulação

P4 e P5 das [respostas fictícias](../../discovery.md) estabelecem que o despacho
deve permanecer registrado. Antes dele, cancelamento é permitido; depois,
deve haver devolução. O motivo é preservar rastreabilidade física. Nenhuma
exceção foi informada. Trata-se de regra declarada no cenário, não de garantia
implementada ou regra de um negócio real.

## FAQ

### Por que não apagar o envio quando o comprador desiste?

Apagar o envio eliminaria o histórico do que saiu fisicamente. A resposta
fictícia P5 indica registrar devolução, cujo procedimento ainda está pendente.

## Antipadrões

| Evitar | Motivo local | Alternativa | Força | Exceções |
| --- | --- | --- | --- | --- |
| Remover registro de despacho para cancelar venda | Perde rastreabilidade física | Manter despacho e registrar devolução | Obrigatório apenas na regra fictícia P4/P5 | Nenhuma informada |

## Divergência aberta

P4 proíbe cancelamento após despacho, mas [can_cancel](service.py) aceita `shipped`.
Isso pode permitir um estado comercial incompatível com o histórico físico.
É necessário confirmar o comportamento desejado e o impacto em clientes existentes;
não escolhemos uma fonte como correta nem alteramos código.

## Decisões e propostas

[RFC de eventos](../../docs/rfcs/0001-eventos-de-expedicao.md) e
[ADR de identificação](../../docs/adrs/0001-identidade-de-eventos.md) estão aceitos
somente na simulação; a implementação não foi iniciada.
