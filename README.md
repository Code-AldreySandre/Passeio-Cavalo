# Passeio do Cavalo

## Introdução
O problema do Passeio do Cavalo é um desafio matemático que envolve o movimento da peça do cavalo em um tabuleiro de xadrez. O objetivo é que o cavalo percorra todas as 64 casas do tabuleiro exatamente uma vez, seguindo as regras de movimento da peça.

Este programa resolve o problema usando um algoritmo recursivo baseado em backtracking.

---

## Funcionalidades

- **Entrada do Usuário:** O programa aceita a posição inicial do cavalo em notação algébrica de xadrez (ex.: `a1`).
- **Validação:** Garante que a entrada do usuário esteja no formato correto.
- **Solução do Problema:** Encontra uma sequência de movimentos válida ou informa que não há solução.
- **Saída Formatada:** Retorna a sequência de movimentos em notação algébrica, um por linha.

---

## Como Usar

1. Certifique-se de que tem o Python 3 instalado em sua máquina.
2. Salve o código em um arquivo, por exemplo, `passeio_cavalo.py`.
3. Execute o programa no terminal, fornecendo a posição inicial:

   ```bash
   python passeio_cavalo.py a1
   ```

4. Alternativamente, inicie o programa e digite a posição inicial quando solicitado:

   ```bash
   python passeio_cavalo.py
   Digite a posição inicial do cavalo (notação algébrica, ex.: a1):
   ```

---

## Exemplo de Execução

Entrada:
```bash
python passeio_cavalo.py b1
```

Saída:
```bash
./cavalo b1
b1
c3
a2
...
```
---

## Estrutura do Código

### Funções Principais

1. **`pos_para_coordenadas(pos)`**
   - Converte a notação algébrica (ex.: `a1`) para índices do tabuleiro.

2. **`coordenadas_para_pos(row, col)`**
   - Converte índices do tabuleiro para notação algébrica.

3. **`movimento_valido(x, y, tabuleiro)`**
   - Verifica se o movimento é válido e se a casa ainda não foi visitada.

4. **`passeio_do_cavalo(x, y, contador, tabuleiro, movimentos)`**
   - Resolve o problema do Passeio do Cavalo usando backtracking.

5. **`validar_entrada(pos)`**
   - Valida a entrada do usuário para garantir conformidade com a notação algébrica.

6. **`principal()`**
   - Função principal que gerencia o fluxo do programa.

---

## Algoritmo

1. Receber a entrada inicial do cavalo.
2. Validar a entrada.
3. Inicializar o tabuleiro e possíveis movimentos do cavalo.
4. Aplicar backtracking para encontrar a solução:
   - Marcar a casa atual como visitada.
   - Testar movimentos possíveis recursivamente.
   - Recuar se nenhum movimento levar a uma solução.
5. Exibir a sequência de movimentos ou informar que não há solução.

---

## Limitações

- O programa assume que o tabuleiro tem dimensões de 8x8.
- Pode ser lento para determinadas entradas devido à natureza do algoritmo de backtracking.

---

## Melhorias Futuras

- Implementar heurísticas como a Regra do Warnsdorff para otimizar a solução.
- Adicionar suporte a tabuleiros de tamanhos personalizados.
- Melhorar a interface com o usuário para experiência mais intuitiva.

---

## Créditos

Este desafio foi idealizado por:
- [Renata Nésio](https://github.com/renatanesio)
- [Carvalhais](https://github.com/carvalhais)

Desafio disponível em: [Desafio 13 - Os Programadores](https://osprogramadores.com/desafios/d13/)

## Licença

Este código está disponível sob a licença MIT. Você é livre para usar, modificar e distribuir conforme desejar.




