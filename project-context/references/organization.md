# Organização e fontes canônicas

Adote a convenção abaixo quando não houver equivalente. Preserve nomes e caminhos existentes; indique equivalências no índice e no roteamento. Use links relativos à localização de cada arquivo, inclusive para código. Crie apenas documentos com informação útil; seções dos templates são opcionais conforme evidência disponível.

| Documento | Conteúdo e fronteira |
| --- | --- |
| AGENTS.md | Instruções operacionais e roteamento; não reproduz regras detalhadas do domínio. |
| product.md | Problema, público, atores, objetivos, capacidades, escopo, não objetivos, restrições e critérios de sucesso. Separe confirmado, hipótese e questão aberta. |
| application-state.md | Estado observado e sua referência temporal/revisão, stack observada ou planejada, capacidades, verificações, falhas e histórico conciso das alterações com autoria conhecida. Não substitui produto, arquitetura, Git ou relatórios completos de testes. |
| context-map.md | Nome, responsabilidade, caminhos do código/context.md, conceitos e dados próprios, relações, contratos/eventos/APIs, traduções e direção conhecida das dependências. |
| pasta existente/context.md | Propósito, limites, responsabilidades e exclusões, linguagem, regras, fluxos, FAQ, antipadrões, contratos, referências e questões abertas. |
| docs/README.md | Índice da arquitetura, decisões, propostas e guias existentes. |
| docs/adrs/ | Decisões duradouras e razões; não uma descrição completa do estado implantado. |
| docs/rfcs/ | Propostas, discussão, alternativas e estado de implementação separado. |
| docs/architecture/ | Estado vigente: componentes, dependências, fluxos, integrações e implantação, com fontes. |
| docs/tech/ | Guias reproduzíveis de desenvolvimento, testes, operação e troubleshooting. |

## AGENTS.md e equivalentes

Inclua roteamento para application-state.md: leitura antes de mudanças, atualização
obrigatória antes de encerrar qualquer alteração, sem pedido adicional, com mudanças
atribuíveis ao agente, verificações e falhas pendentes. Ligue
o estado também no índice docs/README.md, quando existente.

Preserve instruções anteriores. Acrescente links para produto/mapa quando pertinentes, leitura prévia do context.md envolvido, consulta a ADRs aceitos aplicáveis e RFCs relevantes como propostas. Oriente atualizar documentos quando o significado mudar, seguir comandos reais e expor conflitos entre instruções e fontes.

Verifique o suporte do agente a arquivos aninhados nas instruções disponíveis ou documentação da ferramenta antes de depender dele. Se desconhecido, mantenha roteamento explícito na raiz (caminho do código → context.md), sem prometer descoberta automática. Não altere escopo de instruções aninhadas existentes.

Se houver CLAUDE.md ou equivalente, escolha uma fonte operacional canônica conforme o repositório. Use referência/importação apenas se suportada pela ferramenta. Sem suporte verificado, documente explicitamente quais arquivos têm instruções específicas e como manter o trecho comum sincronizado; não crie duas cópias integrais concorrentes.

## Contextos e linguagem

Uma pasta de infraestrutura, controller ou biblioteca não implica bounded context. Contextos podem compartilhar um monólito ou várias pastas. Para múltiplos contextos na mesma pasta, preserve um context.md canônico com seções identificadas ou a estrutura documental já adotada e aponte cada contexto no mapa. Não reorganize código.

Em cada termo relevante, registre significado local, sinônimos evitados, diferenças entre contextos e nome no código quando útil. Não imponha linguagem única. Nas integrações, explicite a tradução e a propriedade dos dados. Mermaid é opcional e só deve ser usado se acrescentar informação.

Antipadrões precisam de prática a evitar, problema específico, alternativa e exceções conhecidas. Diferencie regra obrigatória de recomendação. Uma restrição escrita não garante que código ou testes a imponham.

Arquitetura vigente depende de evidência de implementação; implantação exige evidência adicional. Se apenas o código foi observado, declare o limite. Detalhes técnicos compartilhados ficam em um guia referenciado, não copiados para cada contexto.
