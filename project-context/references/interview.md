# Descoberta e refinamento

## Preparação

Antes de perguntar, leia os documentos relevantes, modelos, fluxos, contratos e testes. Apresente brevemente os achados com fontes: “O endpoint aceita cancelamento após pagamento; a documentação restringe esse caso. Qual comportamento é desejado?”. Não pergunte o que já está documentado de forma consistente. Diferencie evidência do sistema atual de intenção de produto.

Pergunte preferencialmente uma coisa por vez. Agrupe poucas perguntas relacionadas para assuntos simples; adapte a próxima à resposta. Ofereça alternativas só quando fundamentadas, incluindo a possibilidade de outra resposta. As listas abaixo são repertório de descoberta, não um questionário obrigatório.

## Projeto novo ou existente

Inspecione antes de classificar: arquivos de dependências, lockfiles, configuração,
código, testes e documentação. Uma pasta vazia não prova que o produto não existe
em outro lugar; se o pedido e as fontes não esclarecem isso, pergunte. Um scaffold
pode já conter escolhas de stack: trate-as como observadas e confirme sua intenção.

### Projeto novo

Comece pelo problema, público e escopo mínimo. Pergunte se já existe stack definida
ou alguma restrição técnica. Progrida pelas escolhas pertinentes: plataforma
(web, mobile, serviço etc.), linguagens/runtimes, frontend/backend quando houver,
persistência, integrações, implantação, testes e ferramentas de desenvolvimento.
Considere experiência da equipe, operação, prazo e restrições antes de sugerir
alternativas. Não exija componentes que o produto não precisa.

Se o usuário não souber, apresente poucas opções fundamentadas nas necessidades
já descobertas e peça a decisão que faltar. Não escolha uma stack silenciosamente.
Registre escolhas confirmadas e suas razões; opções ainda em discussão ficam
como hipóteses ou RFC, e decisões duradouras podem justificar ADR. Em
application-state.md, marque “planejado / sem implementação”, sem apresentar a
stack escolhida como instalada. Não gere scaffold ou instale dependências sem
que implementação esteja no escopo solicitado.

### Projeto existente

Apresente um inventário curto do que encontrou: stack e versões declaradas,
capacidades, contextos candidatos, contratos, testes, execução e decisões já
documentadas, com fontes. Distinga versão declarada de versão executada e
funcionalidade aparente de comportamento verificado.

Conduza a entrevista progressivamente sobre o que já existe: propósito e uso das
capacidades, limites, regras, exceções, termos e motivos das escolhas. Confirme
inferências que afetam decisões e explore definições ausentes, ambíguas ou
contraditórias. Não peça novamente fatos claros e consistentes nas fontes nem
reabra a escolha da stack sem motivo. Registre o estado inicial e as lacunas em
application-state.md; refinamentos alimentam os documentos canônicos correspondentes.

## Produto

Descubra problema, público e demais atores; resultados esperados; capacidades essenciais; escopo e não objetivos; restrições e critérios de sucesso. Se há descrição de público mas não objetivo, pergunte pelo resultado desejado, sem reiniciar toda a descoberta. Não converta product.md em backlog.

## Novo módulo ou contexto

Comece pelo problema de negócio, razão de existir e usuários. Investigue se a capacidade cabe em um contexto existente: há linguagem, invariantes, responsabilidade por dados ou ciclos de vida distintos? Uma funcionalidade ou diretório novo não é evidência suficiente de um contexto novo.

Depois esclareça responsabilidades, conceitos e dados próprios; exclusões e quem as assume; invariantes e exceções; termos locais; integrações; exemplos concretos e resultados que demonstram escopo atendido. Limites ainda não confirmados ficam como hipótese. Se não houver pasta de código adequada, descreva o contexto candidato no mapa ou na RFC e adie context.md; não crie um módulo para armazená-lo.

## Cenários e exceções

Use um caso comum, um contraexemplo e um caso de borda quando relevantes. Investigue por que existe uma restrição e o que deve ocorrer quando ela falha. Exemplos de perguntas adaptáveis:

- “Se o pagamento confirmar depois do cancelamento, quem decide o próximo estado?”
- “Essa proibição protege qual regra? Existe uma exceção autorizada?”
- “Neste contexto, ‘cliente’ é a pessoa, a conta contratante ou outro conceito?”

Se duas fontes divergirem, mostre ambas e o impacto. Não escolha silenciosamente a mais recente, o código ou a opinião do agente como verdade de negócio. Significados locais diferentes não são, por si, contradições.

## Consolidar sem transcrever

| Conteúdo da resposta | Destino |
| --- | --- |
| Definição local e nome no código | Vocabulário no context.md |
| Condição, invariante, exceção e motivo | Regras, com evidência ou confirmação |
| Quem faz o quê e troca entre contextos | Limites, contratos e context-map.md |
| Dúvida recorrente e explicação duradoura | FAQ conciso, coerente com a regra |
| Prática problemática e motivo local | Antipadrão com alternativa, força e exceções |
| Alternativas técnicas ainda em discussão | RFC, quando o impacto justificar |
| Escolha duradoura comprovada | ADR no status sustentado |
| Incerteza, sugestão do agente ou conflito | Hipóteses ou questões abertas |

Não registre toda a conversa em context.md. Para confirmar algo, referencie a resposta real ou fonte rastreável, com data/pessoa apenas se conhecidas. Não invente nomes nem atas. Em exemplos e testes, marque explicitamente todas as respostas simuladas como fictícias.

## Encerrar

Pare quando houver informação suficiente para a tarefa. Apresente síntese de escopo, responsabilidades e limites, regras e decisões, hipóteses e pendências. Permita correções. Peça confirmação apenas de ambiguidades relevantes ou decisões que dependam do usuário; não exija assinatura de cada fato nem modelagem completa do domínio. Registre o confirmado e continue trabalho independente. Nunca promova uma hipótese a regra para preencher uma seção.
