# Uso de IA no código Python - Prioriza

## Ferramentas utilizadas

| Ferramenta | Finalidade |
|---|---|
| Claude (Anthropic) | Tirar duvidas de Python e Git, organizar a estrutura de pastas e os arquivos de documentacao |

**Periodo:** novembro de 2026
**Responsavel pelas conversas:** Nathaly Vieira Barbosa - RM 575407 / Gustavo Moreira Souza - RM 576147

---

## 1. Correcao de erros e organizacao das pastas

**Prompts principais:**
- Print do erro `SyntaxError: invalid syntax` na linha do `match`
- "De acordo com os requisitos que o professor pediu para o projeto, me de como serao as pastas organizadas do projeto"

**O que a IA fez:**
- Explicou que o `match/case` exige Python 3.10 ou mais novo e como trocar o interpretador no VS Code.
- Sugeriu a estrutura de pastas usada no projeto.
- Auxiliou na busca da ODS que o sistema se enquadra. Tal informação foi incluida na criação da Ficha da CitizenTech.

## 2. Duvidas sobre estrutura de repeticao

**Prompts principais:**
- "Como colocar condicao dentro do case"
- "Posso colocar if dentro do case?"
- "Me de alguns exemplos de como seriam"

**O que a IA fez:**
- Explicou duas formas: o *guard* (`case padrao if condicao:`) e o `if` comum dentro do bloco do `case`.
- Mostrou exemplos das duas. No projeto usamos o `if` dentro do `case`, que é o conteudo visto em aula.

## 3. Estrutura do projeto e Git

**Prompts principais:**
- "Commit em ingles para o que fiz hoje"
- Print da pasta `.vscode` com o arquivo `settings.json`: "O que e isso?"

**O que a IA fez:**
- Explicou a pasta `.vscode` e o `settings.json` e orientou o uso do `.gitignore` para nao enviar configurações do VS Code ao repositorio.
- Sugeriu mensagens de commit em ingles.

## 4. README

**Prompts principais:**
- "Veja se o readme bate com o projeto"
- "Adicione uma tabela para os integrantes do grupo, preciso que tenha duas colunas, uma para os nomes e a outra para os RMs"

**O que a IA fez:**
- Redigiu o `readme.md` a partir do escopo e do código do grupo.

## Analise crítica

**Beneficios**
- A IA ajudou a entender erros, explicou os motivos nao apenas deu a correcao.
- Economizou tempo com Git, que era a parte em que o grupo tinha menos experiencia.
- As revisoes finais mostrou algumas falhas que nao tinhamos percebido como aceitar nome vazio e os assentos.

**Limitações**
- Em algumas respostas, a IA sugeriu recursos que ainda nao vimos em aula, como *guards* no `match`, classes e `.isnumeric()`.

**Dificuldades**
- Seguir o conceito por dicas e nos ensinando como fazer exigiu bem mais tempo porem ajudou a entender com deveria ficar.
