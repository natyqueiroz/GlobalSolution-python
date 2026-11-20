# PRIORIZA - Mobilidade sem barreiras

## Ficha da CitizenTech

| Campo | Resposta |
|---|---|
| Nome da CitizenTech | PRIORIZA - Mobilidade sem barreiras |
| Cidade e bairro | São Paulo - Sé (Centro) |
| Cidadão beneficiado | Pessoas com direito a atendimento prioritário: deficiência física, visual ou auditiva, idosos, mobilidade reduzida, gestantes e pessoas autistas |
| Problema, em uma frase | O passageiro com prioridade não consegue avisar o motorista antes de o ônibus chegar e costuma encontrar o assento preferencial ocupado |
| Como funciona | O passageiro solicita atendimento informando o tipo, o ponto e a quantidade de assentos, o motorista é avisado e o LED do assento preferencial acende. Antenas nos pontos informam onde o ônibus está |
| O que cada parte faz | `prioriza.py`: menu e lógica do sistema em Python, sem classes. `prompts.md`: registro dos prompts usados com IA. Repositório do site: telas do passageiro e do motorista em HTML, CSS e JavaScript |
| Link do repositório | Python: https://github.com/natyqueiroz/GlobalSolution-python · Site (JS): https://github.com/gustavomsz/GS1semestre |
| Indicador de impacto | Número de passageiros com prioridade que embarcaram com o motorista avisado e o assento preferencial livre, por linha e por mês |
| ODS conectados | ODS 10 (Redução das desigualdades) e ODS 11 (Cidades e comunidades sustentáveis) |

## Estrutura do projeto

```
GlobalSolution-python/
├── prioriza.py
├── readme.md
└── prompts.md
```

- `prioriza.py`: programa principal, com o menu e a simulação.
- `prompts.md`: prompts usados com IA durante o desenvolvimento.

## Como executar

```
python prioriza.py
```

## Sobre o projeto

Pessoas com deficiencia, mobilidade reduzida, idosos, gestantes e outros passageiros prioritarios ainda enfrentam dificuldades na comunicação com os motoristas de onibus.

O **Prioriza** permite que o passageiro solicite atendimento prioritario antes de o onibus chegar ao ponto. Quem solicitado:

- o **motorista recebe um aviso** com antecedencia;
- Um **LED** acende nos assentos preferenciais, indicando aos demais passageiros que o lugar foi requisitado;
- **Antenas nos pontos** informam o status do onibus.

Esta é a adaptação em Python do sistema feito em JavaScript, usando apenas variáveis, listas, funções, condicionais e repetições, sem classes e métodos. A versão com site está em https://github.com/gustavomsz/GS1semestre.

### Menu

| Opção | O que faz |
|---|---|
| 1 - Solicitar atendimento prioritario | Pede nome, tipo de atendimento, ponto de embarque e quantidade de assentos. Se o passageiro tiver direito e houver vaga, reserva os assentos, avisa o motorista e acende o LED. |
| 2 - Cancelar solicitacao | Libera os assentos reservados e avisa o motorista. O LED apaga quando todos os assentos ficam livres. |
| 3 - Ver onibus | Mostra a linha, os assentos livres e o estado do LED. |
| 4 - Simular viagem | Mostra o status das antenas em cada ponto da linha ate o ponto final. |
| 5 - Sair | Encerra o programa. |

## Validações

- Opção do menu que nao for entre 1 e 5 dira "Opcao invalida".
- Se o nome estiver vazio ira pedir novamente.
- Tipo de atendimento, ponto de embarque e solicitacao para cancelar: so aceitam os numeros das listas prontas (por enquanto).
- A quantidade de assentos vai de 1 ate o numero de assentos livres.
- Passageiro do tipo "NENHUM" ou onibus sem assento livre: a solicitação nao e feita.

### Dados da simulação

- **Linha:** 2002-10, com 3 assentos preferenciais
- **Pontos de embarque:** Terminal Pq. D. Pedro II, Lgo. Pateo do Colégio, R. Boa Vista, 364
- **Tipos com direito ao assento preferencial:** física, visual, auditiva, idoso, mobilidade reduzida, gestante e autista
- **Status das antenas:** A CAMINHO → ONIBUS CHEGOU → ONIBUS ACABOU DE SAIR → SEM ONIBUS

## Conceitos de programação utilizados

| Conceito | Onde aparece |
|---|---|
| Menu de opcoes | `while True` com as 5 opcoes |
| Estruturas de decisao | `match/case` no menu; `if/elif/else` no direito ao assento e no LED |
| Estruturas de repeticao | `while` no menu e nas validacoes; `for` para mostrar listas e simular a viagem |
| Listas | listas fixas (pontos, tipos, status) e listas de solicitacoes com `append` e `pop` |
| Entrada e saida | `input()` e `print()` com f-strings |

## Integrantes - Time 404

| Integrante | RM |
|---|---|
| Giovanna Ciola | 575631 |
| Gustavo Moreira Souza | 576147 |
| Jamil de Jesus Chaluppe Filho | 575697 |
| Nathaly Vieira Barbosa | 575407 |
| Marina Lobato Soares | 575475 |