# Validação de project-context

Executada em 2026-11-13. A skill está em [project-context](../project-context/SKILL.md),
sem instalação global ou alterações em projetos externos.

## Como usar

Neste checkout, solicite: “Leia project-context/SKILL.md e use o modo Inicializar
no projeto indicado”. Outros exemplos estão na [referência de uso](../project-context/references/examples.md).
O caminho explícito funciona como instrução de leitura; a skill não foi registrada
no catálogo global, portanto a descoberta automática por `$project-context` não
foi testada neste ambiente. A pasta `project-context` é a unidade portátil completa.

## Entrega

- [SKILL.md](../project-context/SKILL.md): fluxo, oito modos e regras essenciais.
- [Catálogo de templates](../project-context/assets/templates/README.md): dez
  templates para agentes, produto, estado da aplicação, mapa, contexto, índice, RFC, ADR, arquitetura e guia.
- [Referências](../project-context/references/organization.md): organização,
  entrevista, manutenção, ciclo RFC → ADR e exemplos, roteados pelo SKILL.md.
- [Auditor](../project-context/scripts/audit_docs.py): somente leitura, biblioteca
  padrão Python 3.10+, com códigos de saída documentados.
- [Fixture](fixture/product.md), [roteiro fictício](fixture/discovery.md),
  [snapshots da primeira execução](run-1/hashes.json) e
  [testes](test_project_context.py).

## Demonstração em duas execuções

A demonstração foi conduzida pelo agente autor nesta fixture, com respostas
preparadas e explicitamente fictícias. Não foi uma entrevista com pessoas reais
nem um teste autônomo de outro agente. Os testes verificam os artefatos e o auditor;
não geram respostas, decidem limites ou aprovam decisões.

| Capacidade solicitada | Evidência e resultado |
| --- | --- |
| Inicializar documentação | Primeira execução produziu produto, mapa, dois contextos, roteamento, índice e arquitetura observada a partir dos dois arquivos de código e P1/P2 fictícias. Hashes da primeira execução foram capturados antes da segunda. |
| Preservar numa segunda execução | AGENTS.md permaneceu idêntico; o conteúdo inicial de Vendas foi preservado integralmente e ampliado. Produto, mapa, arquitetura vigente e os dois arquivos de código mantiveram seus hashes. |
| Entrevistar sobre novo módulo | P3 investiga rastreio: não há responsabilidade independente, portanto a capacidade é documentada em Expedição sem criar módulo. |
| Consolidar descoberta | P4/P5 resultam em regra, FAQ e antipadrão com motivo, alternativa e força no contexto de Vendas, sem copiar toda a transcrição. |
| Distinguir vocabulários | “Pedido” é compromisso comercial em Vendas e solicitação de envio em Expedição; o mapa explica tradução e cardinalidade. |
| Criar RFC e ADR relacionado | RFC 0001 e ADR 0001 têm links recíprocos, sequências independentes e aceitação sustentada exclusivamente por P6 fictícia. |
| Separar aprovação e implementação | RFC Accepted com Implementação: Não iniciada. Arquitetura vigente permaneceu inalterada e sem eventos. |
| Expor contradição | P4 versus can_cancel em shipped permanece questão aberta em Vendas. Código não foi modificado nem uma das fontes foi declarada verdadeira por conta própria. |
| Detectar links inválidos | Teste injeta arquivo inexistente, âncora inexistente e referência não definida em diretório temporário; o auditor detecta os três e ignora exemplos em blocos de código. A fixture entregue permanece sem links inválidos. |

## Verificações executadas

1. `quick_validate.py project-context`, da skill-creator: **Skill is valid!**
2. `python -X utf8 -m unittest discover -s validation -p 'test_*.py' -v`:
   **7 testes aprovados**.
3. Auditor sobre skill e fixture: **nenhum achado mecânico**. Também exercitados
   erros de status, numeração duplicada, campo de implementação ausente, diretórios
   alternativos, limite da raiz e códigos de saída 0/1/2.
4. Revisão semântica pelo autor: fontes e hipóteses distintas, zero aprovação real
   inventada, nenhum novo módulo, nenhuma implementação de proposta e exemplos
   identificados como fictícios.

O alias `python` do Windows não funcionava nesta sessão; as verificações usaram o
Python 3.12 do runtime empacotado do ambiente. O validador oficial precisava de
PyYAML; a versão 6.0.3 foi instalada **apenas em validation/.deps**, ignorada pelo
Git, após autorização de rede. A skill e seus testes não dependem desse pacote.
Para repetir o validador oficial com esse Python, configure PYTHONPATH para essa
pasta. O próprio validador pertence ao ambiente e não é redistribuído na skill.

## Extensão: estado da aplicação e início de projeto

Incluído [application-state.md na fixture](fixture/application-state.md), com
stack observada, capacidades, código preservado, pendências e limites das
verificações; o roteamento foi acrescentado a AGENTS.md preservando integralmente
as instruções anteriores. O teste de preservação agora permite esse acréscimo,
sem modificar os snapshots históricos da primeira execução.

O [roteiro fictício de projeto novo](new-project-discovery.md) demonstra perguntas
progressivas sobre produto, stack e restrições antes de qualquer implementação.
Projetos existentes começam com inventário e perguntas sobre definições faltantes.
Não foi adicionada automação de monitoramento: o estado é atualizado pela execução
da skill e pelas instruções operacionais produzidas por ela.

## Extensão: atalhos e encerramento obrigatório

Incluído [roteamento de atalhos](../project-context/references/commands.md), com
`/init` para novos projetos, `/discover` para existentes e os demais modos, além
de `/state` e `/help`. São instruções conversacionais quando a skill está carregada;
não foram registrados comandos nativos no menu do aplicativo. A compatibilidade
documenta a colisão com o `/init` nativo do Codex e a invocação explícita alternativa.

O SKILL.md, as referências e o template de AGENTS.md agora exigem atualização do
estado antes de finalizar qualquer alteração, mesmo documental e sem pedido do
usuário. Na fixture, a alteração de AGENTS.md foi registrada em application-state.md
sem exigir `/update`, preservando suas instruções anteriores. Consultas sem mudanças
e a edição do próprio estado não geram entradas recursivas.

Revisão dos casos de roteamento: `/init` diante de código existente preserva o projeto
e segue descoberta; argumento ausente essencial gera pergunta; `/adr` não aprova
sozinho; `/state` não escreve; linguagem natural mantém o mesmo encerramento.
São casos revisados nas instruções, não execuções de um parser ou avaliação autônoma.

## Limitações da validação

O auditor implementa um subconjunto de Markdown, documentado em
[manutenção](../project-context/references/maintenance.md). Não consulta URLs nem
comprova regras, aceitação, implantação ou consistência semântica. Templates
exigem adaptação pelo agente; não há gerador que finja deduzir decisões de negócio.
Não foi executada avaliação independente com outro agente nem instalação para
testar descoberta automática. A preservação demonstrada refere-se aos arquivos
desta fixture; não é garantia de comportamento para todo repositório futuro.
