import os
import time
import random
import copy
from Bot import resolver, mostrar, resolvido

def gerar_sudoku():
    """
    Gera um quebra-cabeça de Sudoku aleatório removendo alguns números de uma grade resolvida.
    
    Returns:
        list: Grade de Sudoku gerada.
    """
    # Inicializa um Sudoku resolvido
    solved_sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    # Cria uma cópia da grade resolvida do Sudoku
    sudoku_puzzle = [row[:] for row in solved_sudoku]

    # Define o número de células a serem removidas para um quebra-cabeça de dificuldade média
    cells_to_remove = random.randint(30, 60)

    # Remove números para criar o quebra-cabeça
    for _ in range(cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        sudoku_puzzle[row][col] = 0

    return sudoku_puzzle
input('pressione enter para começar...')
tabuleiro = [[8,9,4,0,0,0,0,5,1],
             [0,0,7,0,0,3,0,6,9],
             [0,6,0,5,0,4,0,0,0],
             [0,3,8,4,5,1,0,0,0],
             [2,0,0,0,0,6,8,0,5],
             [6,0,0,0,0,2,7,0,0],
             [3,8,0,1,7,5,0,0,0],
             [4,0,0,3,6,9,1,0,8],
             [0,1,0,0,0,0,5,7,0]]
'''tabuleiro=[[0,0,5,3,0,0,0,0,0],
                   [8,0,0,0,0,0,0,2,0],
                    [0,7,0,0,1,0,5,0,0],
                    [4,0,0,0,0,5,3,0,0],
                    [0,1,0,0,7,0,0,0,6],
                    [0,0,3,2,0,0,0,8,0],
                    [0,6,0,5,0,0,0,0,9],
                    [0,0,4,0,0,0,0,3,0],
                    [0,0,0,0,0,9,7,0,0]]'''
tentativas = 0
l_tentativas = []
acertos = 0
porc = 0
foi = []
tempo_medio = 0
while True:
    
    tabuleiro = gerar_sudoku()
    
    #tabuleiro = [[0 for _ in range(9)]for _ in range(9)]
    time_i = time.time()
    l_tentativas.append(copy.deepcopy(tabuleiro))
    l_tentativas.append(tabuleiro)
    tentativas += 1
    tabuleiro_bot = tabuleiro
    resolver(tabuleiro_bot)
    if resolvido(tabuleiro_bot):
        acertos += 1
    time_elapsed = time.time() - time_i
    tempo_medio += time_elapsed
    if tentativas > 1:
        tempo_medio /= 2
    os.system('cls' if os.name == 'nt' else 'clear')
    porc = acertos*100/tentativas
    print(f'Resorvido: {resolvido(tabuleiro_bot)}')
    print(f'Jogo: {tentativas}/1000')
    print(f'Tempo: {time_elapsed}')
    print(f'Tempo médio: {tempo_medio}')
    print(f'Porcentagem de acertos: {porc}%')
    mostrar(tabuleiro_bot, tentativas)
    time.sleep(2)
    if tentativas == 1000:
        max_tentativas = 1000
        break
print(porc)
i = 1
while i != max_tentativas*2 + 1:
    input('pressione enter para continuar')
    print(i)
    print(foi[(i-1)//2])
    tabuleiro = l_tentativas[i-1:i+1]
    mostrar(tabuleiro[0])
    mostrar(tabuleiro[1])
    i+=2
input()