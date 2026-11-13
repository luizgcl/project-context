# Orientações operacionais

{{Preservar instruções existentes; incluir somente links para documentos que existem.}}

- Consulte {{link relativo para produto}} e {{link relativo para mapa}} quando relevantes à tarefa.
- Antes de alterar um contexto, leia seu context.md conforme o roteamento abaixo.
- Consulte {{link relativo para application-state.md}} antes de mudanças. Ao finalizar qualquer alteração no projeto (código, testes, configuração, dependências ou documentação), atualize esse arquivo antes da resposta final, sem esperar pedido do usuário ou `/update`. Registre o que alterou, autoria conhecida, verificações antes/depois e pendências. Diferencie falhas preexistentes, regressões observadas e estado não verificado. Consultas sem mudanças não geram registro; não registre recursivamente a edição do próprio estado. Se não puder atualizar, informe o impedimento.
- Consulte ADRs aceitos aplicáveis e RFCs relevantes; RFCs são propostas e seu status não comprova implementação.
- Atualize documentos cujo significado for alterado pela mudança.
- Siga os comandos e convenções reais registrados em {{guia ou arquivo do repositório}}.
- Apresente conflitos entre instruções, documentos e código com fontes e impacto; não os resolva silenciosamente.

## Roteamento explícito

| Caminho de código | Documentação |
| --- | --- |
| {{caminho existente}} | {{link relativo para context.md}} |

## Compatibilidade de instruções

{{Se houver outro arquivo de instruções: fonte canônica, referência suportada ou estratégia explícita de manutenção. Não presumir descoberta automática de arquivos aninhados.}}
