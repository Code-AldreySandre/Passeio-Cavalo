def pos_para_coordenadas(pos):
    #Converte a notação de xadrez para índices do tabuleiro.#
    col = ord(pos[0].lower()) - 97
    row = int(pos[1]) - 1
    return row, col

def coordenadas_para_pos(row, col):
    
    return f"{chr(col + 97)}{row + 1}"

def movimento_valido(x, y, tabuleiro):
   
    return 0 <= x < 8 and 0 <= y < 8 and tabuleiro[x][y] == -1

def passeio_do_cavalo(x, y, contador, tabuleiro, movimentos):
    """Aplica o algoritmo para resolver o passeio do cavalo."""
    tabuleiro[x][y] = contador

    if contador == 63:
        return True

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if movimento_valido(nx, ny, tabuleiro):
            if passeio_do_cavalo(nx, ny, contador + 1, tabuleiro, movimentos):
                return True

    tabuleiro[x][y] = -1
    return False

def validar_entrada(pos):
    
    if len(pos) != 2:
        return False
    if not ("a" <= pos[0].lower() <= "h"):
        return False
    if not ("1" <= pos[1] <= "8"):
        return False
    return True

def principal():
    import sys
    if len(sys.argv) == 2:
        inicio = sys.argv[1]
    else:
        inicio = input("Digite a posição inicial do cavalo (notação algébrica, ex.: a1): ").strip()

    if not validar_entrada(inicio):
        print("Entrada inválida. Certifique-se de usar a notação algébrica, como 'a1'.")
        return

    x, y = pos_para_coordenadas(inicio)

    tabuleiro = [[-1] * 8 for _ in range(8)]
    movimentos_do_cavalo = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    if passeio_do_cavalo(x, y, 0, tabuleiro, movimentos_do_cavalo):
        caminho = [coordenadas_para_pos(r, c) for r in range(8) for c in range(8) if tabuleiro[r][c] != -1]
        caminho.sort(key=lambda p: tabuleiro[pos_para_coordenadas(p)[0]][pos_para_coordenadas(p)[1]])
        print(f"./cavalo {inicio}")
        print("\n".join(caminho))
    else:
        print("Sem solução possível.")

if __name__ == "__main__":
    principal()
