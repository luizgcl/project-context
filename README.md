# project-context

Skill para descobrir, organizar e manter o conhecimento de projetos de software:
produto, contextos de domínio, arquitetura, decisões técnicas e estado da aplicação.
Funciona por entrevistas progressivas e análise do repositório, com instruções
portáteis para Codex e Claude Code.

Em projetos novos, investiga produto, stack e restrições antes de registrar escolhas.
Em projetos existentes, examina código e documentação antes de perguntar sobre
lacunas, regras e definições. Não impõe DDD, microsserviços ou novos módulos.

## Começar sem instalar

Baixe ou clone este repositório, abra a pasta no seu agente e peça:

```text
Leia project-context/SKILL.md e execute /init no projeto indicado.
```

Para um projeto já implementado, use `/discover`. Informe o caminho do projeto
quando ele for diferente do diretório de trabalho. Essa leitura explícita não
instala nem registra a skill no catálogo da ferramenta.

## Instalação

Obtenha o repositório público:

```sh
git clone https://github.com/luizgcl/project-context.git
cd project-context
```

Copie a pasta **project-context inteira**, incluindo templates, referências,
scripts e licença, para um dos destinos abaixo. Não copie somente o SKILL.md.

| Ferramenta | Apenas um projeto | Todos os projetos do usuário |
| --- | --- | --- |
| Codex | `.agents/skills/project-context/` | `~/.agents/skills/project-context/` |
| Claude Code | `.claude/skills/project-context/` | `~/.claude/skills/project-context/` |

Os caminhos de projeto são relativos à raiz do projeto que usará a skill.
`~` representa sua pasta de usuário. Instalar por projeto permite versionar a
skill junto com o código e compartilhá-la com a equipe. Preserve uma instalação
existente e revise diferenças antes de substituir arquivos numa atualização.

Abra uma nova sessão no projeto após instalar. Confira as instruções atuais de
[skills no Codex](https://learn.chatgpt.com/docs/build-skills) e
[skills no Claude Code](https://code.claude.com/docs/en/skills).
Esta instalação não exige serviço, API key ou dependência Python; o auditor
opcional requer Python 3.10+.

## Uso no Codex

```text
$project-context /init
$project-context /discover
$project-context /refine pagamentos
```

## Uso no Claude Code

```text
/project-context /init
/project-context /discover
/project-context /refine pagamentos
```

Claude Code encaminha o texto após o nome da skill como argumentos. Estes exemplos
se referem ao Claude Code local; não são instruções de instalação no chat do Claude
ou no Cowork. Veja a [documentação de argumentos](https://code.claude.com/docs/en/skills#pass-arguments-to-skills).

## Comandos da skill

| Atalho | O que faz |
| --- | --- |
| `/init` | Descobre produto, stack e restrições de um projeto novo/vazio. |
| `/discover` | Entende um projeto existente e entrevista sobre definições ausentes. |
| `/map` | Mapeia contextos, responsabilidades, linguagem e integrações. |
| `/context <tema>` | Investiga se um novo contexto é necessário e define seus limites. |
| `/refine <tema>` | Aprofunda regras, exceções, vocabulário, FAQ e antipadrões. |
| `/rfc <mudança>` | Explora alternativas e documenta uma proposta técnica. |
| `/adr <decisão>` | Registra uma decisão no status sustentado por evidência. |
| `/update [escopo]` | Sincroniza os documentos com mudanças no código ou entendimento. |
| `/audit [escopo]` | Identifica inconsistências, informações desatualizadas e links inválidos. |
| `/state` | Consulta estado, verificações e pendências sem alterar arquivos. |
| `/help` | Mostra os atalhos e exemplos. |

São atalhos interpretados **dentro da skill**, não comandos independentes de
terminal ou itens registrados individualmente no menu do aplicativo. Use a
invocação completa acima para evitar colisões com comandos nativos como `/init`.
Detalhes de argumentos e comportamento: [referência de comandos](project-context/references/commands.md).

Pedidos em linguagem natural também funcionam:

```text
Use project-context para documentar este projeto e esclarecer as definições que faltam.
Refine as regras de cancelamento com cenários e exceções.
Explore uma integração por eventos e registre a proposta, sem implementar.
```

## Documentação mantida

| Documento | Responsabilidade |
| --- | --- |
| `AGENTS.md` | Instruções operacionais e roteamento para o conhecimento. |
| `product.md` | Problema, público, capacidades, objetivos e escopo. |
| `application-state.md` | Estado observado, alterações, verificações e pendências. |
| `context-map.md` | Contextos, responsabilidades e relações. |
| `<pasta-existente>/context.md` | Linguagem, regras, FAQ, limites e contratos locais. |
| `docs/README.md` | Índice da documentação técnica e arquitetural. |
| `docs/rfcs/` | Propostas em discussão e seu estado de implementação. |
| `docs/adrs/` | Decisões arquiteturais, motivos e histórico. |
| `docs/architecture/` | Arquitetura efetivamente observada. |
| `docs/tech/` | Guias técnicos e operacionais reproduzíveis. |

As estruturas existentes são preservadas. A skill cria apenas documentos úteis;
não cria módulos ou move código para acomodar documentação.

## Estado atualizado sem pedido adicional

Ao concluir qualquer alteração no projeto, o agente deve atualizar
`application-state.md` antes da resposta final, mesmo sem `/update` ou pedido
explícito. Isso inclui código, testes, configuração, dependências e documentação.
A atualização registra mudanças atribuíveis à tarefa, evidências e limitações.

Essa obrigação é incorporada às instruções do projeto em `AGENTS.md`. Para
compartilhá-las com Claude Code quando ele usar `CLAUDE.md`, acrescente a importação
abaixo ao arquivo da raiz, preservando as instruções existentes:

```markdown
@AGENTS.md
```

Veja [compartilhamento de instruções no Claude Code](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools).
Não há monitoramento em background: a manutenção depende de o agente carregar e
seguir as instruções. Consultas sem mudanças não geram histórico e a edição do
próprio estado não dispara entradas recursivas.

## Evidências e limites

- Comportamento observado, regra confirmada e hipótese são tratados separadamente.
- Uma RFC aceita não comprova implementação ou implantação.
- Falha preexistente, regressão observada e estado não verificado não são equivalentes.
- Testes aprovados sustentam apenas o escopo verificado; documentação não garante ausência de bugs.
- Entrevistas não autorizam implementar funcionalidades ou aprovar decisões automaticamente.

## Verificação local

Com Python 3.10+, a partir da raiz deste repositório:

```sh
python -X utf8 -m unittest discover -s validation -p 'test_*.py' -v
python -X utf8 project-context/scripts/audit_docs.py .
```

Para auditar a documentação de outro projeto, substitua `.` pelo caminho dele.
O auditor é somente leitura e usa a biblioteca padrão. Ele verifica um subconjunto
de links Markdown, numeração e status de RFCs/ADRs; não valida decisões de negócio.
Veja [limitações do auditor](project-context/references/maintenance.md).

Os [resultados de validação](validation/RESULTS.md) descrevem os testes e a
[fixture fictícia](validation/fixture/product.md). Respostas simuladas não
representam validação de negócio real nem avaliação independente por outro agente.

## Estrutura e distribuição

```text
project-context/       Skill portátil: SKILL.md, LICENSE, referências, templates e auditor
validation/            Testes, exemplos fictícios e resultados
README.md              Guia público
LICENSE                Licença do repositório
application-state.md   Estado de manutenção deste repositório
```

Para distribuir uma versão, publique este repositório e crie uma release com a
pasta `project-context/` completa. Os testes ficam no repositório e não são
necessários para usar a skill. Exclua caches, `validation/.deps` e dados de projetos
reais do pacote. Este repositório não registra automaticamente um plugin em marketplace.

## Licença

[MIT](LICENSE) — Copyright (c) 2026 luizgcl.
Uma cópia acompanha a [pasta instalável](project-context/LICENSE).
