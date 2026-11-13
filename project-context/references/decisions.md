# Ciclo RFC → ADR

## Quando registrar

Use RFC para alternativas relevantes, impacto entre contextos, incerteza ou alinhamento necessário. Mudanças pequenas não precisam de RFC. Use ADR para uma decisão duradoura e seus motivos; pode existir sem RFC prévia. Uma RFC pode resultar em vários ADRs. Resuma a decisão no ADR e referencie a discussão, sem duplicá-la.

## Identificadores

Use `docs/rfcs/NNNN-titulo.md` e `docs/adrs/NNNN-titulo.md`, salvo convenção existente. As sequências são independentes: obtenha o maior número existente em cada diretório e avance um, sem renumerar registros históricos ou preencher lacunas. Confira colisões imediatamente antes de criar; se houver concorrência, escolha outro número e ajuste links. O validador detecta duplicatas, mas não reserva números.

## Estados

| Tipo | Estados permitidos e significado |
| --- | --- |
| RFC | Draft (elaboração), In Review (discussão), Accepted (proposta aprovada), Rejected (não aprovada), Withdrawn (retirada), Superseded (substituída). |
| ADR | Proposed (decisão sugerida), Accepted (decisão aceita), Deprecated (não mais recomendada/vigente, com motivo), Superseded (substituída por outra decisão). |

Use `Status: ...` nos documentos para permitir auditoria mecânica. Datas e responsáveis só quando conhecidos. Registre evidência da aceitação, rejeição, retirada ou substituição e o resultado da discussão; o agente não pode aprovar por conta própria. Na ausência de aceitação comprovada, use Draft/In Review ou Proposed conforme o caso.

## Aprovação, implementação e histórico

Em RFC, mantenha `Implementação: ...` separada de Status, por exemplo “Não iniciada”, “Parcial”, “Concluída” ou “Desconhecida”, com evidências disponíveis. Accepted só comprova aprovação. Mesmo código implementado não comprova implantação. A arquitetura vigente só muda quando houver evidência da mudança efetiva; atualize guias e contextos conforme o impacto comprovado.

Não reescreva a decisão de um ADR aceito para esconder nova direção. Crie outro registro, preserve o texto original e atualize o status/metadados históricos com motivo e links recíprocos de substituição. RFC Superseded também deve apontar a sucessora. Deprecated pode não ter sucessor, mas precisa de razão. Aceitação histórica sem fonte conhecida deve ser assinalada como lacuna, sem inventar aprovadores nem apagar o histórico.

Rastreie o ciclo nos dois sentidos: RFC → ADR(s), ADR → RFC quando houver, decisões substituídas ↔ sucessoras, documentos de estado atual → decisões aplicáveis. Links são relativos ao arquivo de origem.
