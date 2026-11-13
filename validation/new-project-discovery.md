# Exemplo de inicialização — inteiramente fictício

Este roteiro demonstra o novo fluxo, não uma entrevista real nem teste autônomo.

Inspeção simulada: diretório sem código ou manifests, e pedido explícito de criar
um produto novo. Nenhuma stack pode ser deduzida.

1. Agente: “Qual problema resolve, para quem e qual é o escopo inicial?”
   Resposta fictícia: “Um catálogo web interno, somente consulta; equipe conhece Python.”
2. Agente: “Há stack definida ou restrições de implantação e persistência?”
   Resposta fictícia: “Django e PostgreSQL por padrão interno; implantação ainda indefinida.”
3. Agente: “O catálogo exige API para outro cliente ou páginas renderizadas atendem?”
   Resposta fictícia: “Páginas renderizadas atendem. Não precisamos de frontend separado.”

Consolidação: produto com escopo de consulta; Django/PostgreSQL **planejados e
confirmados apenas no exemplo**; versões, hospedagem e testes ainda pendentes.
application-state.md deve registrar “sem implementação; execução não verificada”,
sem inventar build, dependências instaladas ou testes aprovados. Não gerar scaffold
enquanto a tarefa for apenas descoberta/documentação.

Contraste com a [fixture existente](fixture/application-state.md): primeiro se
identificam código Python, capacidades e divergência de cancelamento; o roteiro
de [descoberta](fixture/discovery.md) aprofunda responsabilidades e regras. Não é
necessário perguntar qual linguagem já está nos arquivos nem exigir trocar a stack.

## Exercício de interpretação do estado — resultados fictícios

Se um teste passava na referência A e falha em B no mesmo ambiente, registrar
regressão observada nessa verificação e investigar o diff. Se falhava em A e B,
registrar falha preexistente. Se A não foi testada, registrar falha atual com origem
indeterminada. Esses casos são exemplos conceituais, não execuções de testes reais.
