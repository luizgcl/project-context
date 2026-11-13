---
name: project-context
license: MIT
description: Organiza e mantém documentação de produto, contextos de domínio, arquitetura e tecnologia a partir do repositório e de entrevistas progressivas. Use para iniciar, mapear, criar ou refinar contextos, propor RFCs, registrar ADRs, atualizar ou auditar esse conhecimento em projetos de software.
---

# Project Context

Produza conhecimento objetivo e proporcional à complexidade do projeto. Documente o sistema e suas incertezas sem impor DDD completo, microsserviços ou novos módulos.

## Fluxo principal

1. Identifique a raiz e o escopo solicitado. Leia instruções existentes, documentação pertinente e código representativo (entradas, modelos, contratos e testes). Descubra comandos reais nos arquivos do projeto; não adivinhe comandos. Não carregue toda a documentação por padrão.
2. Distinga projeto novo de existente pela inspeção e pelo objetivo informado; esclareça se houver dúvida. Em projeto novo, entreviste sobre produto e stack antes de registrar escolhas. Em projeto existente, inventarie stack, capacidades e definições antes de perguntar sobre lacunas. Separe fatos confirmados, comportamento observado, hipóteses e perguntas abertas; código não comprova a regra desejada.
3. Escolha o modo abaixo. Nas tarefas de descoberta, apresente o que já sabe e entreviste sobre lacunas essenciais, conforme [entrevista](references/interview.md). Continue tarefas independentes enquanto aguarda respostas.
4. Selecione os documentos conforme [organização](references/organization.md). Adapte somente os [templates necessários](assets/templates/README.md); remova instruções, marcadores e seções sem conteúdo útil. Não crie arquivos vazios. Respeite a localização e as fontes canônicas existentes.
5. Leia ou estabeleça a linha de base em application-state.md antes de mudanças. Depois, registre alterações, autoria conhecida, verificações e comparação com o estado anterior conforme [estado da aplicação](references/application-state.md). Faça alterações pontuais, preserve conteúdo válido e confira links relativos. Siga [manutenção](references/maintenance.md), revise o diff e apresente evidências e pendências.

## Modos e solicitações

Aceite linguagem natural e os atalhos conversacionais abaixo quando esta skill
estiver carregada. São rotas de instrução, não comandos de terminal ou registros
nativos de slash commands. Para sintaxe, argumentos e compatibilidade, leia
[comandos](references/commands.md).

| Atalho | Ação |
| --- | --- |
| `/init` | Inicializar projeto vazio/novo, descobrindo produto, stack e restrições. |
| `/discover` | Entender projeto existente e entrevistar sobre lacunas e definições. |
| `/map` | Mapear contextos e relações. |
| `/context <nome ou problema>` | Investigar e definir um contexto antes de implementar. |
| `/refine <contexto ou tema>` | Refinar regras, linguagem, FAQ e antipadrões. |
| `/rfc <mudança>` | Explorar e documentar uma proposta técnica. |
| `/adr <decisão>` | Registrar decisão com status sustentado por evidência. |
| `/update [escopo]` | Sincronizar documentação e estado com alterações existentes. |
| `/audit [escopo]` | Auditar documentação e reportar achados. |
| `/state` | Consultar estado, verificações e pendências, sem alterar arquivos. |
| `/help` | Exibir atalhos e exemplos de uso. |

| Modo | Pedido de exemplo | Resultado e leitura adicional |
| --- | --- | --- |
| Inicializar | “Inicialize a documentação mínima deste projeto.” | Projeto novo: descoberta de produto e stack. Existente: inventário e entrevista sobre capacidades e definições. Em ambos, documentação mínima e application-state.md. |
| Mapear | “Mapeie responsabilidades e integrações.” | Mapa e linguagem local, com limites incertos explicitados. |
| Criar contexto | “Defina o contexto de devoluções antes de implementar.” | Avalie pertencer a um contexto existente; entreviste e documente escopo sem criar código ou pastas de módulos. |
| Refinar | “Refine regras e FAQ de cobrança.” | Cenários, invariantes, vocabulário, FAQ e antipadrões sustentados. |
| Propor | “Explore alternativas para entrega de eventos.” | RFC quando a discussão justificar; leia [ciclo RFC → ADR](references/decisions.md). |
| Decidir | “Registre a decisão sobre persistência.” | ADR no status sustentado por evidência; leia o ciclo de decisões. |
| Atualizar | “Atualize a documentação afetada por este diff.” | Rastreie impacto, compare verificações antes/depois e atualize documentos afetados e application-state.md. |
| Auditar | “Audite divergências e links da documentação.” | Achados com fontes, impacto e dúvidas; nenhuma resolução semântica inventada. |

## Regras essenciais

- Ao finalizar **qualquer alteração no projeto**, atualize application-state.md
  por iniciativa própria, antes da resposta final, sem exigir `/update` ou pedido
  adicional. Inclua código, testes, configuração, dependências e documentação;
  registre o que mudou, autoria conhecida, verificações e pendências. Propague essa
  obrigação ao AGENTS.md do projeto para próximas tarefas, inclusive pedidos em
  linguagem natural. Consultas sem mudanças não geram entradas; atualizar o próprio
  estado não dispara um novo registro recursivo. Se não puder escrever, informe a
  pendência e o motivo, sem declarar a atualização concluída.

- Não invente regras, entrevistas, responsáveis ou aprovações. Perspectivas de especialistas e diálogos entre agentes geram hipóteses, não validação de negócio.
- Não confunda pasta técnica com contexto de domínio. Não mova código nem crie módulos para acomodar documentos. Não implemente funcionalidades apenas por terem sido discutidas.
- Uma palavra pode ter significados legítimos diferentes em contextos distintos; registre a tradução na integração.
- Apresente conflitos entre código, documentos e respostas com fontes e impacto; confirme apenas ambiguidades relevantes que dependam do usuário.
- RFC Accepted não significa implementação concluída. Não aceite ADR sem evidência ou autorização explícita. Preserve decisões históricas e seus vínculos de substituição.
- Mantenha AGENTS.md curto e operacional; preserve instruções e evite duplicação com CLAUDE.md ou equivalentes. Não dependa de descoberta de instruções aninhadas sem verificar suporte.
- Documentação não substitui testes e verificações arquiteturais. Regras de domínio não justificam padrões técnicos por si só.
- Estado não verificado não significa aplicação saudável. Registre falhas e verificações não executadas; só atribua regressão ou autoria quando houver evidência. A atualização do estado ocorre ao executar esta skill ou seguir suas instruções no projeto, sem monitoramento automático.
- Atue apenas no projeto autorizado. Esta pasta é uma skill portátil; não instale globalmente nem altere projetos externos por conta própria.

## Recursos sob demanda

- [Entrevista](references/interview.md): produto, novo módulo, cenários e consolidação.
- [Comandos](references/commands.md): atalhos conversacionais e tratamento de argumentos.
- [Organização](references/organization.md): responsabilidades de cada documento e roteamento.
- [Decisões](references/decisions.md): estados, numeração e histórico RFC/ADR.
- [Manutenção e auditoria](references/maintenance.md): execução repetida e validador somente leitura.
- [Estado da aplicação](references/application-state.md): linha de base, alterações, autoria e evidências antes/depois.
- [Exemplos](references/examples.md): solicitações e dois significados de “pedido”.
- [Templates](assets/templates/README.md): documentos adaptáveis, sem geração automática indiscriminada.
