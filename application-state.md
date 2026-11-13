# Estado de manutenção de project-context

## Referência e escopo

Registro iniciado em 2026-11-13 para este repositório de uma skill, não para uma
aplicação implantada. As fixtures em validation são exemplos fictícios separados.
Repositório público criado em https://github.com/luizgcl/project-context.
Não houve instalação global. Consulte o histórico remoto para as revisões publicadas.

## Estado observado

A [skill](project-context/SKILL.md) contém instruções, referências, templates e um
auditor Python. O [README](README.md) documenta instalação e uso em Codex e Claude
Code. A [licença MIT](LICENSE), escolhida pelo usuário nesta conversa, identifica
luizgcl como titular em 2026 e também acompanha a pasta instalável.

Stack: Markdown para instruções e templates; Python 3.10+ para o auditor e testes,
sem dependências externas de execução da skill. O validador oficial de formato usa
PyYAML, disponível apenas na pasta local ignorada validation/.deps nesta sessão.

## Alterações desta tarefa

| Data | Autoria/evidência | Alteração |
| --- | --- | --- |
| 2026-11-13 | Agente nesta conversa, após escolha MIT e titular luizgcl pelo usuário | Criou README.md, LICENSE e cópia em project-context/LICENSE; declarou license: MIT no frontmatter e iniciou este registro de estado. |
| 2026-11-13 | Agente nesta conversa, com publicação pública autorizada pelo usuário | Criou luizgcl/project-context pelo GitHub CLI, adicionou instrução de clone ao README e padronizou finais de linha LF em .gitattributes para preservar hashes das fixtures entre plataformas. |

Os demais materiais da skill e as fixtures já existiam antes desta tarefa;
seu histórico de desenvolvimento e validação está em [RESULTS](validation/RESULTS.md).

## Verificações

Verificações executadas em 2026-11-13, a partir da raiz, com Python 3.12 do runtime
local; o alias python do Windows não foi utilizado:

| Verificação | Antes desta tarefa | Resultado após a alteração |
| --- | --- | --- |
| quick_validate.py project-context, da skill-creator | Aprovação registrada na tarefa anterior | Skill is valid! |
| python -X utf8 -m unittest discover -s validation -p 'test_*.py' -v | Sete testes aprovados na tarefa anterior | Sete testes aprovados. |
| python -X utf8 project-context/scripts/audit_docs.py . | Nenhum achado na tarefa anterior | Nenhum achado mecânico, incluindo links do README. |
| Comparação SHA-256 de LICENSE e project-context/LICENSE | Arquivos ainda não existiam | Conteúdos idênticos. |

A referência anterior vem dos resultados registrados nesta conversa, não de uma
nova execução prévia à edição. Não houve mudança de lógica do auditor ou da
aplicação fictícia. Os resultados não comprovam instalação nas ferramentas.

## Pendências e limites

- Repositório remoto público criado; nenhuma tag ou release criada nesta tarefa.
- Instalação e execução interativa no Claude Code não foram testadas aqui.
- A documentação de instalação referencia fontes oficiais; descoberta da skill
  depende do ambiente e da instalação no destino correto.
- Atualizações futuras da licença devem manter as duas cópias idênticas.
