# Manutenção e auditoria

## Execuções repetidas

O encerramento de qualquer tarefa que altere o projeto inclui atualizar
application-state.md, mesmo sem solicitação explícita e mesmo em mudança apenas
documental. Mantenha essa obrigação no AGENTS.md, sem duplicar registros quando não
houver novidades nem gerar histórico recursivo da edição do próprio estado.

Leia o conteúdo antes de editar. Localize o equivalente canônico, compare o significado e altere apenas o trecho afetado. Não copie templates por cima de documentos existentes. Preserve notas válidas, instruções locais e histórico. Uma segunda execução sem informação nova deve produzir diff vazio; registre incertezas uma vez, sem replicar seções.

Em mudança de código, inspecione o diff e siga contratos, consumidores e testes para localizar documentos impactados. Atualize mapa, contexto, arquitetura ou guias apenas onde o significado mudou. Proposta discutida não autoriza implementação de funcionalidade. Não altere projetos externos.

## Auditoria semântica pelo agente

Ao inicializar ou atualizar, mantenha [application-state.md](application-state.md)
conforme o procedimento de linha de base e comparação. Na auditoria, confira se a
referência do estado ainda corresponde ao código, se verificações possuem evidência
e se falhas não verificadas foram indevidamente tratadas como resolvidas.

Procure regras sem evidência, ambiguidade de responsabilidade, documentação obsoleta, contradições entre fontes, requisitos confundidos com comportamento atual, aceitações sem evidência e arquitetura proposta apresentada como vigente. Compare o significado local antes de chamar diferenças de vocabulário de conflito.

Para cada achado, relate localização das duas fontes quando aplicável, evidência, impacto e pergunta ou correção sugerida. Corrija links e erros objetivos dentro do escopo; deixe conflitos semânticos relevantes abertos até obter confirmação. Não infira a resolução a partir da passagem de tempo ou de uma perspectiva de especialista.

## Validador somente leitura

Requer Python 3.10+ e somente biblioteca padrão. A partir da pasta que contém a skill:

```sh
python project-context/scripts/audit_docs.py CAMINHO_DO_PROJETO
```

Examina Markdown, ignorando diretórios de ferramentas/build conhecidos, links externos e blocos cercados de código. Verifica links locais inline e referências explícitas, arquivos e âncoras simples de títulos Markdown, numeração duplicada, nomes e estados de RFC/ADR, e campo de implementação em RFC. Use `--rfc-dir` e `--adr-dir` para convenções de diretórios diferentes; cada caminho é relativo à raiz. Não exige documentos opcionais nem pastas vazias. Retorna 0 sem achados, 1 com achados, 2 para erro de execução.

É um verificador leve, não um parser CommonMark completo: não valida disponibilidade de URLs, sintaxes complexas com parênteses aninhados, HTML, referências abreviadas, nem âncoras geradas por extensões. Âncoras seguem títulos simples no estilo GitHub (incluindo sufixo de repetição). Não segue symlinks nem links que saiam da raiz: sinaliza estes últimos para revisão. Não valida semanticamente entrevistas, aprovação, limites, contradições ou conclusão da implementação. Esses pontos dependem de revisão do agente e das fontes.

## Revisão de entrega

Confira referências, ausência de seções vazias/marcadores nos documentos produzidos, consistência dos status, evidências de decisões e diff. Reporte limitações e pendências. Use os templates como esquema adaptável, nunca como exigência de preencher conhecimento inexistente.
