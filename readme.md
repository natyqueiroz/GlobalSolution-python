# PRIORIZA


## Estrutura do preojeto

```
GlobalSolution-python/
├── prioriza.py
├── readme.md
└── prompts.md
```

## Sobre o projeto

Pessoas com deficiência, mobilidade reduzida, idosos, gestantes e outros passageiros prioritários ainda enfrentam dificuldades na comunicação com os motoristas de ônibus.

O **Prioriza** permite que o passageiro solicite atendimento prioritário antes de o ônibus chegar ao ponto. Ao solicitar:

- o **motorista recebe um aviso** com antecedência;
- um **LED** acende nos assentos preferenciais, indicando aos demais passageiros que o lugar foi requisitado;
- **antenas nos pontos** informam o status do ônibus.

### Menu

| Opção | O que faz |
|---|---|
| 1 - Solicitar atendimento prioritário | Pede nome, tipo de atendimento, ponto de embarque e quantidade de assentos. Se o passageiro tiver direito e houver vaga, reserva os assentos, avisa o motorista e acende o LED. |
| 2 - Cancelar solicitação | Libera os assentos reservados e avisa o motorista. O LED apaga quando todos os assentos ficam livres. |
| 3 - Ver ônibus | Mostra a linha, os assentos livres e o estado do LED. |
| 4 - Simular viagem | Mostra o status das antenas em cada ponto da linha até o ponto final. |
| 5 - Sair | Encerra o programa. |

### Dados da simulação

- **Linha:** 2002-10, com 3 assentos preferenciais
- **Pontos de embarque:** Terminal Pq. D. Pedro II, Lgo. Pateo do Colégio, R. Boa Vista, 364
- **Tipos com direito ao assento preferencial:** física, visual, auditiva, idoso, mobilidade reduzida, gestante e autista
- **Status das antenas:** A CAMINHO → ONIBUS CHEGOU → ONIBUS ACABOU DE SAIR → SEM ONIBUS

## Integrantes

| Integrantes | RM |
|---|---|
| Giovanna Ciola | 575631 |
| Gustavo Moreira Souza | 576147 |
| Jamil de Jesus Chaluppe Filho | 575697 |
| Nathaly Vieira Barbosa | 575407 |
| Marina Lobato Soares | 575475 |
