# Estágio em Desenvolvimento - Target Sistemas

### Q1

**Inicialização:** A função começa com uma lista fib_seq contendo os primeiros dois números da sequência: 0 e 1.

**Geração da Sequência:** Um laço while é utilizado para calcular novos números da sequência até que o último número seja maior ou igual ao número n.

**Verificação:** Após gerar a sequência, o código verifica se n está presente na lista. Se estiver, retorna uma mensagem afirmando que o número pertence à sequência; caso contrário, informa que não pertence.

**Entrada e Saída:** O programa solicita ao usuário um número, chama a função e imprime o resultado da verificação.

#### [Código](Q1.py) 

---

### Q2

**Importação de Módulo:** O módulo unicodedata é importado para permitir a normalização de caracteres.

**Remoção de Acentos:** A função remove_accents normaliza a string de entrada, separando os caracteres acentuados de seus acentos, e retorna a versão sem acentos.

**Contagem de Letras:** A função count_letter_a_with_accents transforma a string em minúsculas, remove os acentos e conta quantas vezes a letra "a" aparece na string normalizada.

**Verificação e Retorno:** Se a letra "a" for encontrada, retorna uma mensagem com o número de ocorrências; caso contrário, informa que não foi encontrada.

**Entrada e Saída:** O programa solicita ao usuário que informe uma string e imprime o resultado da contagem.

#### [Código](Q2.py) 

---

### Q3

```
INDICE = 12
SOMA = 0
K = 1

while (K < INDICE):
    K = K + 1
    SOMA = SOMA + K 

print(SOMA)
```

**SOMA** = 77

---

### Q4

a) 1, 3, 5, 7, ___ **Próximo elemento: 9**

Esta é uma sequência de números ímpares. Cada número é incrementado em 2 a partir do anterior: 1, 3 (1 + 2), 5 (3 + 2), 7 (5 + 2), e assim, o próximo número é 7 + 2 = 9.

b) 2, 4, 8, 16, 32, 64, ____ **Próximo elemento: 128**

Esta sequência representa potências de 2. Cada número é o dobro do anterior: 2 (2^1), 4 (2^2), 8 (2^3), 16 (2^4), 32 (2^5), 64 (2^6), então o próximo número é 64 × 2 = 128 (ou 2^7).

c) 0, 1, 4, 9, 16, 25, 36, ____ **Próximo elemento: 49**

Esta é uma sequência de quadrados perfeitos. Cada número é o quadrado de um número inteiro: 0 (0²), 1 (1²), 4 (2²), 9 (3²), 16 (4²), 25 (5²), 36 (6²), e o próximo número é 7² = 49.

d) 4, 16, 36, 64, ____ **Próximo elemento: 100**

Esta sequência também representa quadrados perfeitos, mas começando a partir de 2: 4 (2²), 16 (4²), 36 (6²), 64 (8²), e seguindo a lógica, o próximo número é 10² = 100.

e) 1, 1, 2, 3, 5, 8, ____ **Próximo elemento: 13**

Esta é a sequência de Fibonacci, onde cada número é a soma dos dois anteriores: 1, 1 (0 + 1), 2 (1 + 1), 3 (1 + 2), 5 (2 + 3), 8 (3 + 5), e o próximo número é 5 + 8 = 13.

f) 2, 10, 12, 16, 17, 18, 19, ____ **Próximo elemento: 20**

Esta sequência alterna entre adicionar um número e um incremento.
- Começando com 2, adiciona 8 (2 + 8 = 10)
- Adiciona 2 (10 + 2 = 12)
- Adiciona 4 (12 + 4 = 16)
- Adiciona 1 (16 + 1 = 17)
- Adiciona 1 (17 + 1 = 18)
- Adiciona 1 (18 + 1 = 19)  

Portanto, seguindo essa lógica, o próximo número é 19 + 1 = 20.

---

### Q5

Primeiro, eu ligaria o primeiro interruptor, que chamarei de Interruptor A, e deixaria ligado por cerca de 5 a 10 minutos. Isso permitiria que a lâmpada aquecesse. Depois desse tempo, desligaria o Interruptor A.

Em seguida, ligaria o segundo interruptor, que chamarei de Interruptor B, imediatamente antes de ir até a sala onde as lâmpadas estão.

Ao entrar na sala, eu faria a seguinte análise:

- Se uma lâmpada estiver desligada, mas quente ao toque, saberei que ela é controlada pelo Interruptor A.
- Se eu encontrar uma lâmpada ligada, isso significaria que ela é controlada pelo Interruptor B.
- Se a lâmpada estiver desligada e fria, eu deduziria que ela é controlada pelo Interruptor C.

Dessa forma, utilizando tanto o estado (ligado ou desligado) quanto a temperatura (quente ou fria) das lâmpadas, consigo identificar claramente qual interruptor controla cada lâmpada em apenas duas idas à sala.