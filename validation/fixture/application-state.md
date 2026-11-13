# Estado da aplicação — fixture fictícia

## Referência e resumo

Observação por leitura em 2026-11-13, após refinamento documental. Há duas funções
de Vendas e um construtor de Expedição. Não há aplicação executável completa nem
implantação demonstrada. A saúde funcional não foi verificada.

## Stack e capacidades observadas

- Python observado nos arquivos [Vendas](src/sales/service.py) e
  [Expedição](src/shipping/service.py); não há versão declarada pelo projeto.
- Cancelamento e construção de payload estão presentes no código; não executados
  como testes de negócio nesta demonstração.
- Eventos e deduplicação permanecem planejados na [RFC](docs/rfcs/0001-eventos-de-expedicao.md),
  Accepted apenas no cenário fictício, com implementação não iniciada.

## Verificações e comparação

| Verificação | Antes | Depois | Conclusão |
| --- | --- | --- | --- |
| Comparação SHA-256 dos dois arquivos de código, executada pelos testes de preservação em validation | Hashes capturados na primeira execução | Idênticos após refinamento documental | Código de entrada preservado; não comprova comportamento correto. |
| Testes funcionais da aplicação | Não executados; não há suíte configurada | Não executados pelo mesmo motivo | Estado funcional não verificado; não é possível afirmar ausência de regressões. |

## Pendências

A regra fictícia P4 proíbe cancelamento após despacho, mas `can_cancel` aceita
`shipped`. É uma divergência constatada por leitura, já presente na entrada;
não uma regressão produzida pelo agente nem uma falha reproduzida em runtime.
Veja [Vendas](src/sales/context.md) e [descoberta](discovery.md).

## Alterações e autoria

| Execução | Autoria conhecida | Alteração | Evidência e limite |
| --- | --- | --- | --- |
| Inicialização e refinamento da fixture | Agente autor desta demonstração | Criou e refinou documentação de produto, mapa, contextos, RFC e ADR | [Índice](docs/README.md); dados e aprovações são fictícios. |
| Extensão de estado em 2026-11-13 | Agente nesta execução | Adicionou este estado e seu roteamento | [AGENTS.md](AGENTS.md) e [índice](docs/README.md); nenhum código de negócio alterado. |
| Encerramento obrigatório em 2026-11-13 | Agente nesta execução | Ampliou AGENTS.md para exigir atualização de estado após qualquer alteração, sem pedido adicional | [AGENTS.md](AGENTS.md); mudança apenas documental. Verificação funcional da aplicação continua não executada. |
