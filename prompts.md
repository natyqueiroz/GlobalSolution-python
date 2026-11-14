# Uso de IA no código Python - Prioriza

**Ferramenta:** Claude (Anthropic)
**Período:** novembro de 2026
**Responsável pelas conversas:** Nathaly Vieira Barbosa - RM 575407

Este arquivo resume como a IA foi usada no desenvolvimento do código Python (`prioriza.py`).

---

## 1. Correção de erros e organizacao das pastas

Solicitei como seria a organizacao final das pastas de acordo com os requisitos que o professor solicitou, e exclarecimento de alguns erros que nao sabia o que eram.

**Prompts principais:**
- Print do erro `SyntaxError: invalid syntax` na linha do `match`
- "de acordo com os requisitos que o professor pediu para o projeto, me de como seram as pastas organizadas do projeto"

**O que a IA fez:**
- Explicou que o `match/case` exige Python 3.10 ou mais novo e como trocar o interpretador no VS Code
- Entregou como seria as pastas estruturadas (como estao atualmente)

## 2. Duvidas sobre estrutura de repeticao

**Prompts principais:**
- "como colocar condicao dentro do case"
- "posso colocar if dentro do case?"
- "me de alguns exemplo de como seriam"

**O que a IA fez:**
- Expliquei o uso de **Guards** (Guardas), que consiste em colocar um `if` na mesma linha logo após o padrão (`case padrao if condicao:`). Se o `if` for falso, o Python ignora o bloco e testa o próximo `case`. Também mencionei que é possível usar variáveis externas na condição.
* **Exemplo fornecido:** Um loop `while True:` que recebia um número do usuário (`input()`), validava se era dígito (`isdigit()`), convertia para inteiro e usava `match numero:` para testar três casos: `case n if n > 0:` (positivo), `case n if n < 0:` (negativo) e `case 0:` (zero).

- Podemos colocar um if dentro do case. Diferenciei as duas abordagens: o **Guard** (que avalia antes de entrar e pula para o próximo `case` se for falso) versus o `if` tradicional dentro do bloco indentado (que roda quando o padrão já foi aceito e serve para sub-validações internas sem pular de `case`).
* **Exemplo fornecido:** Um `match comando:` com o `case "configuracao":`. Dentro dele, a variável `usuario_eh_admin` recebia o retorno de `checar_permissao()`, seguida de um bloco `if usuario_eh_admin:` / `else:` para liberar ou negar o acesso ao painel de controle.


## 3. Estrutura do projeto e Git
**Prompts principais:**

- "Commit em inglês para o que fiz hoje"
- Print da pasta .vscode com o arquivo settings.json: "O que é isso?"

**O que a IA fez:**
- explicar a pasta .vscode e o settings.json, orientar o uso do .gitignore para não enviar configurações do VS Code ao repositório, e sugerir mensagens de commit em inglês.

## 4. README
**Prompts principais:**

- "Veja se o readme bate com o projeto"
- "Adicione uma tabela para os integrantes do grupo, preciso q tenha duas colunas uma para os nomes e a outra para os rm"

**O que a IA fez:**
- Edigir o readme.md a partir do escopo e do código do grupo
