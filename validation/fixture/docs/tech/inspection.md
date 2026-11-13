# Inspecionar a fixture localmente

## Objetivo e pré-requisitos

Inspecionar os dois arquivos de entrada, sem executar fluxos de negócio.
Requer PowerShell e execução a partir da raiz da fixture.

## Procedimento

```powershell
Get-Content -LiteralPath src/sales/service.py
Get-Content -LiteralPath src/shipping/service.py
```

## Verificação

O primeiro arquivo expõe `can_cancel` e `shipment_payload`; o segundo,
`shipment_request`. Não há produtor de eventos nem deduplicação.

## Troubleshooting

Se o caminho não existir, verifique o diretório de execução. Os arquivos são
entradas sintéticas; este procedimento não executa nem comprova regras de negócio.
