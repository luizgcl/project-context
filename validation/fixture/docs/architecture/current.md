# Arquitetura observada — fixture fictícia

O código contém funções de Vendas e Expedição no mesmo repositório.
[Vendas](../../src/sales/service.py) produz um payload com identificador comercial;
[Expedição](../../src/shipping/service.py) constrói solicitações de envio.
O mecanismo de transporte e a implantação não estão demonstrados.

Não há produtor/consumidor de eventos nem persistência de deduplicação neste código.
