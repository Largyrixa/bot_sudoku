import os, time

def resolver(grid, p=0):
    """
    Resolve o quebra-cabeça de Sudoku usando uma abordagem iterativa para reduzir o tempo de uso da função recursiva.
    
    Parameters:
        grid (list): A grade de Sudoku como uma lista de listas.
        p (int): Profundidade atual na recursão (padrão é 0).
    
    Returns:
        bool: True se o quebra-cabeça foi resolvido, False caso contrário.
    """
    i = 0
    while i < 9:
        j = 0
        while j < 8:
            j += 1
            j %= 9
            if grid[i][j] == 0:
                vizinhos = get_vizinhos(grid, i, j)
                possiveis = [x for x in range(1, 10) if x not in vizinhos]
                mostrar(grid, i, j, possiveis[:], p=p)
                if len(possiveis) > 1:
                    continue
                if len(possiveis) == 1:
                    grid[i][j] = possiveis[0]
                    i = 0
                    j = -1
        i += 1
        j %= 9
    if resolvido(grid):
        return True
    return resolver_recursivo(grid, p=p)

def resolver_recursivo(grid, i=0, j=0, p=0):
    """
    Resolve o quebra-cabeça de Sudoku usando uma abordagem recursiva.
    
    Parameters:
        grid (list): A grade de Sudoku como uma lista de listas.
        i (int): Índice da linha atual (padrão é 0).
        j (int): Índice da coluna atual (padrão é 0).
        p (int): Profundidade atual na recursão (padrão é 0).
    
    Returns:
        bool: True se o quebra-cabeça foi resolvido, False caso contrário.
    """
    if j == 9:
        if i == 8:
            return True
        j = 0
        i += 1

    if grid[i][j] > 0:
        return resolver_recursivo(grid, i, j + 1, p + 1)

    for num in range(1, 10):
        if is_valid_move(grid, i, j, num):
            grid[i][j] = num
            if resolver_recursivo(grid, i, j + 1, p + 1):
                return True
        mostrar(grid, i, j, num, p=p)
        grid[i][j] = 0

    return False

def mostrar(grid, i=-1, j=-1, num=None, p=81):
    """
    Exibe a grade de Sudoku com destaque na célula atual e nas informações relevantes.
    
    Parameters:
        grid (list): A grade de Sudoku como uma lista de listas.
        i (int): Índice da linha atual (padrão é -1).
        j (int): Índice da coluna atual (padrão é -1).
        num (int): Número analisado (padrão é None).
        p (int): Profundidade atual na recursão (padrão é 81).
    """
    if num is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Célula analisada: ({i},{j})')
        print(f'Número(s) analisado(s): {num}')
        print(f'Profundidade: {p} ({p*100//81}%) ')
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print('--- + --- + ---')
        for y in range(9):
            print(f'\033[1;31m{grid[x][y]}\033[m' if x == i and y == j else grid[x][y],
                  end=' | ' if (y + 1) % 3 == 0 and y != 0 and y != 8 else '')
        print()
    time.sleep(1 / 59)

def is_valid_move(grid, i, j, num):
    for x in grid[i]:
        if x == num:
            return False
    
    for x in range(9):
        if grid[x][j] == num:
            return False
    i_i = i - i % 3
    i_j = j - j % 3
    celula = [grid[i_i + x][i_j + y] for y in range(3) for x in range(3)]
    
    for x in celula:
        if x == num:
            return False
    return True

def resolvido(grid):
    for x in range(9):
        soma = 0
        for y in range(9):
            soma += grid[x][y]
        if soma != 45: return False
    return True

def get_vizinhos(grid,i,j):
    viz = [x for x in grid[i] if x != 0]
    viz.extend(grid[x][j] for x in range(9))
    i_i = i - i % 3
    i_j = j - j % 3
    celula = [grid[i_i + x][i_j + y] for y in range(3) for x in range(3)]
    for l in celula:
        viz.append(l)
    i = 0
    while len(viz) > 0:
        if viz[0] == 0:viz.pop(0)
        imax = len(viz)
        if viz[i] == 0:
            viz.pop(i)
            i = -1
        i += 1
        if imax == i:break
    return viz
    