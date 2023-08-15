

from sys import argv
from os import system as comando

if len(argv) == 1: #caso o usuário não bote o arquivo como parâmetro, o programa vai ler os arquivos com os nomes padrão
  arquivo_configuracao = 'arq_01_cfg.txt'
  arquivo_jogo = 'arq_01_jog.txt'
else:
  try:
    arquivo_configuracao = argv[1]
    arquivo_jogo = argv[2]
  except IndexError: # se o usuario não botar o nome do segundo arquivo, o programa vai ler só o de configuracao
    arquivo_configuracao = argv[1]

def limpa_tela():
  comando('clear')

def grade_sudoku_jogo(lista, matriz2):
  # LAÇO QUE FAZ O PRINT DA GRADE'
    print('    A   B   C    D   E   F    G   H   I')
    print(' ++---+---+---++---+---+---++---+---+---++')
    for i in range(9):
      print(i+1, end = '||') # posições das linhas
      for j in range(9):
        if matriz2[i][j] != '0' and lista[i][j] == ' ':
           print(f'\033[1;93m {str(matriz2[i][j])} \033[m', end = '|')
        else:
          print(f' {str(lista[i][j])} ', end = '|') # valores da matriz
        if (j+1) % 3 == 0: 
          print('|', end = '') # depois de 3 valores printa a divisória ||
      print(i+1)
      if (i+1) < 9 and (i+1) % 3 == 0: # depois de 3 linhas printa a divisória ++===++...
        print(' ++===+===+===++===+===+===++===+===+===++')
      else: 
        print(' ++---+---+---++---+---+---++---+---+---++')
    print('    A   B   C    D   E   F    G   H   I')

def grade_sudoku(lista):
  # LAÇO QUE FAZ O PRINT DA GRADE'
    print('    A   B   C    D   E   F    G   H   I')
    print(' ++---+---+---++---+---+---++---+---+---++')
    for i in range(9):
      print(i+1, end = '||') # posições das linhas
      for j in range(9):
        print('', lista[i][j], '', end = '|') # valores da matriz
        if (j+1) % 3 == 0: 
          print('|', end = '') # depois de 3 valores printa a divisória ||
      print(i+1)
      if (i+1) < 9 and (i+1) % 3 == 0: # depois de 3 linhas printa a divisória ++===++...
        print(' ++===+===+===++===+===+===++===+===+===++')
      else: 
        print(' ++---+---+---++---+---+---++---+---+---++')
    print('    A   B   C    D   E   F    G   H   ')
  
def gerador_de_matriz_para_grade(nomedoarquivo):
    matriz = []
    colunaA = []
    colunaB = []
    colunaC = []
    colunaD = []
    colunaE = []
    colunaF = []
    colunaG = []
    colunaH = []
    colunaI = []
    for i in range(9):
        matriz.append([' '] * 9)

    with open(nomedoarquivo, 'r') as arquivo:
        informacoes = arquivo.readlines()

    for i in range(len(informacoes)):
        informacoes[i] = informacoes[i].replace('\n', '')

    for a in range(1, 10):
        for linha in informacoes:
            if ('A,{}'.format(a)) in linha:
                colunaA.append(linha)
            elif ('B,{}'.format(a)) in linha:
                colunaB.append(linha)
            elif ('C,{}'.format(a)) in linha:
                colunaC.append(linha)
            elif ('D,{}'.format(a)) in linha:
                colunaD.append(linha)
            elif ('E,{}'.format(a)) in linha:
                colunaE.append(linha)
            elif ('F,{}'.format(a)) in linha:
                colunaF.append(linha)
            elif ('G,{}'.format(a)) in linha:
                colunaG.append(linha)
            elif ('H,{}'.format(a)) in linha:
                colunaH.append(linha)
            elif ('I,{}'.format(a)) in linha:
                colunaI.append(linha)

    for i in range(1, 10):
        for c in range(1, 10):
            if ('A,{}:{}'.format(i, c)) in colunaA:
                matriz[i - 1][0] = c
            if ('B,{}:{}'.format(i, c)) in colunaB:
                matriz[i - 1][1] = c
            if ('C,{}:{}'.format(i, c)) in colunaC:
                matriz[i - 1][2] = c
            if ('D,{}:{}'.format(i, c)) in colunaD:
                matriz[i - 1][3] = c
            if ('E,{}:{}'.format(i, c)) in colunaE:
                matriz[i - 1][4] = c
            if ('F,{}:{}'.format(i, c)) in colunaF:
                matriz[i - 1][5] = c
            if ('G,{}:{}'.format(i, c)) in colunaG:
                matriz[i - 1][6] = c
            if ('H,{}:{}'.format(i, c)) in colunaH:
                matriz[i - 1][7] = c
            if ('I,{}:{}'.format(i, c)) in colunaI:
                matriz[i - 1][8] = c
    return (matriz)

def numero_de_valores_validacao():
    
    with open(arquivo_configuracao, 'r') as arquivo:
        informacoes = arquivo.readlines()

    for i in range(len(informacoes)):
        informacoes[i] = informacoes[i].replace('\n', '')
    if len(informacoes) != len(set(informacoes)):
        print('Valores repetidos!')
        return 0
    elif len(informacoes) < 1 or len(informacoes) > 80:
        print('Quantidade de pistas fora do intervalo especificado')
        return 0
    else:
        return 1

def validacao_matriz(matriz):
  #AQUI EU TESTO CADA ELEMENTO COM CADA COLUNA PARA VER SE SÃO REPETIDOS
    valida = 1
    for l in range(9):
        for c in range(9):
            for c2 in range(9):
                if valida == 1 and matriz[l][c] != (' ') and matriz[l][c2] != (' ') and c2 != c and matriz[l][c] == matriz[l][c2]:
                  return 0
                  valida = 0
                  
    #AQUI EU TESTO CADA ELEMENTO COM CADA LINHA PARA VER SE SÃO VÁLIDOS                
    if valida == 1:
        for c in range(9):
            for l in range(9):
                for l2 in range(9):
                    if valida == 1 and matriz[l][c] != (' ') and matriz[l2][c] != (' ') and l2 != l and matriz[l][c] == matriz[l2][c]:
                      return 0
                      valida = 0
                        

    # AQUI COMEÇA A VALIDAR AS PEQUENAS MATRIZES

    ## MATRIZ 1 (0,2 - 0,2)
    list1 = []
    if valida == 1:
        for l in range(0, 3):
            for c in range(0, 3):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

      

    ## MATRIZ 2 (3,5 - 0,2)
    list1 = []
    if valida == 1:
        for l in range(3, 6):
            for c in range(0, 3):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

    ## MATRIZ 3 ( 6,8 - 0, 2)
    list1 = []
    if valida == 1:
        for l in range(6, 9):
            for c in range(0, 3):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

    ## MATRIZ 4 ( 0,2 - 3-5 )
    list1 = []
    if valida == 1:
        for l in range(0, 3):
            for c in range(3, 6):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

    ## MATRIZ 5 (3,5 - 3,5)
    list1 = []
    if valida == 1:
        for l in range(3, 6):
            for c in range(3, 6):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

    ## MATRIZ 6 (6,8 - 3,5)
    list1 = []
    if valida == 1:
        for l in range(6, 9):
            for c in range(3, 6):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0
    

    ## MATRIZ 7 ( 0,2 - 6,8)
    list1 = []
    if valida == 1:
        for l in range(0, 3):
            for c in range(6, 9):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

    ## MATRIZ 8 ( 4,5 - 6,8)
    list1 = []
    if valida == 1:
        for l in range(3, 6):
            for c in range(6, 9):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0
    

    ## MATRIZ 9 ( 6,8 - 6,8)
    list1 = []
    if valida == 1:
        for l in range(6, 9):
            for c in range(6, 9):
                if matriz[l][c] != ' ':
                    list1.append(matriz[l][c])
    if len(list1) != len(set(list1)):
      valida = 0
      return 0

    # aqui acaba de validar as pequenas matrizes
    if valida == 0:
      return 0
    elif valida == 1:
      return 1

print('''
   SSSSSSSSSSSSSSSUUUUUUUU     UUUUUUUDDDDDDDDDDDDD            OOOOOOOOO    KKKKKKKKK    KKKKKKUUUUUUUU     UUUUUUUU
 SS:::::::::::::::U::::::U     U::::::D::::::::::::DDD       OO:::::::::OO  K:::::::K    K:::::U::::::U     U::::::U
S:::::SSSSSS::::::U::::::U     U::::::D:::::::::::::::DD   OO:::::::::::::OOK:::::::K    K:::::U::::::U     U::::::U
S:::::S     SSSSSSUU:::::U     U:::::UDDD:::::DDDDD:::::D O:::::::OOO:::::::K:::::::K   K::::::UU:::::U     U:::::UU
S:::::S            U:::::U     U:::::U  D:::::D    D:::::DO::::::O   O::::::KK::::::K  K:::::KKKU:::::U     U:::::U
S:::::S            U:::::D     D:::::U  D:::::D     D:::::O:::::O     O:::::O K:::::K K:::::K   U:::::D     D:::::U
 S::::SSSS         U:::::D     D:::::U  D:::::D     D:::::O:::::O     O:::::O K::::::K:::::K    U:::::D     D:::::U
  SS::::::SSSSS    U:::::D     D:::::U  D:::::D     D:::::O:::::O     O:::::O K:::::::::::K     U:::::D     D:::::U
    SSS::::::::SS  U:::::D     D:::::U  D:::::D     D:::::O:::::O     O:::::O K:::::::::::K     U:::::D     D:::::U
       SSSSSS::::S U:::::D     D:::::U  D:::::D     D:::::O:::::O     O:::::O K::::::K:::::K    U:::::D     D:::::U
            S:::::SU:::::D     D:::::U  D:::::D     D:::::O:::::O     O:::::O K:::::K K:::::K   U:::::D     D:::::U
            S:::::SU::::::U   U::::::U  D:::::D    D:::::DO::::::O   O::::::KK::::::K  K:::::KKKU::::::U   U::::::U
SSSSSSS     S:::::SU:::::::UUU:::::::UDDD:::::DDDDD:::::D O:::::::OOO:::::::K:::::::K   K::::::KU:::::::UUU:::::::U
S::::::SSSSSS:::::S UU:::::::::::::UU D:::::::::::::::DD   OO:::::::::::::OOK:::::::K    K:::::K UU:::::::::::::UU
S:::::::::::::::SS    UU:::::::::UU   D::::::::::::DDD       OO:::::::::OO  K:::::::K    K:::::K   UU:::::::::UU
 SSSSSSSSSSSSSSS        UUUUUUUUU     DDDDDDDDDDDDD            OOOOOOOOO    KKKKKKKKK    KKKKKKK     UUUUUUUUU
''')


z = int(input('Entre 1 para iniciar modo interativo, 2 para modo BACH  e 0 para sair: '))
if z == 0:
    print('Até mais!')
elif z == 1:
    #####  UTILIZAR FUNÇÃO GERADORA DA GRADE SUDOKU A PARTIR DA MATRIZ 
    ##### UTILIZAR APÓS FUNÇÃO GERADORA DA MATRIZ A PARTIR DO ARQUIVO TXT 
    ##### UTILIZAR APÓS FUNÇÃO QUE VALIDA A ENTRADA DO ARQUIVO TXT (ANTES DE MONTAR MATRIZ) 
    ##### UTILIZAR FUNÇÃO QUE VALIDA A MATRIZ DEPOIS DE MONTADA
    limpa_tela()

    x = numero_de_valores_validacao()
    if x == 1:
        ç = gerador_de_matriz_para_grade(arquivo_configuracao)
        y = validacao_matriz(ç)
        if y == 1:
            grade_sudoku(gerador_de_matriz_para_grade(arquivo_configuracao))
        else:
            quit('Valores nao compativeis com as regras do Sudoku')
    elif x == 0:
        quit()

    ############ PARTE DE INTERAÇÃO ###########

    ## 1) PRIMEIRA PARTE, ACEITAR COMANDOS
    ## 2) RETIRAR ESPAÇOS E COLOCAR TUDO EM UPPER CASE X.UPPER()
    ## 3) REJEITAR NUMEROS MAIORES QUE 9 OU MENORES QUE 1
    ## 4) MODIFICAR MATRIZ (AD OU DEL) E COMPARAR COM MATRIZ PÉTREA ( QUE NÃO PODE SER ALTERADA )
    ## 5) MOSTRAR NOVA MATRIZ
    ## 6) SE MATRIZ COMPLETA , FINALIZAR

    ######################################
    Matriz1 = gerador_de_matriz_para_grade(arquivo_configuracao)
    Matriz2 = Matriz1
    terminodejogo = 0
    jogadas_cont = 0
    while terminodejogo == 0:
        jogada = input(('Qual a sua jogada? Utilize o formato (COLUNA(A-I),LINHA(1-9):VALOR) , Voce pode deletar uma jogada anterior digitando (D<COLUNA>,<LINHA>): '))
        jogadas_cont += 1
      # isso limpa a tela e faz parecer que a grade tá atualizando
        limpa_tela()
        jogada = jogada.upper()
        jogada = jogada.replace(" ", "")
        jogadavalida = 1

        if len(jogada) > 5 and len(jogada) < 5:
            print('Por favor, utilize caracteres de A a I  e numeros de 0 a 9')
            jogadavalida = 3

        if jogadavalida == 1:
            for a in range(0, 9):
                Matriz1 = gerador_de_matriz_para_grade(arquivo_configuracao)
                if jogada == ('DA,{}'.format(a + 1)) and Matriz1[a][0] == ' ':
                    jogadavalida = 2
                    Matriz2[a][0] = (' ')
                elif jogada == ('DB,{}'.format(a + 1)) and Matriz1[a][1] == ' ':
                    jogadavalida = 2
                    Matriz2[a][1] = (' ')
                elif jogada == ('DC,{}'.format(a + 1)) and Matriz1[a][2] == ' ':
                    jogadavalida = 2
                    Matriz2[a][2] = (' ')
                elif jogada == ('DD,{}'.format(a + 1)) and Matriz1[a][3] == ' ':
                    jogadavalida = 2
                    Matriz2[a][3] = (' ')
                elif jogada == ('DE,{}'.format(a + 1)) and Matriz1[a][4] == ' ':
                    jogadavalida = 2
                    Matriz2[a][4] = (' ')
                elif jogada == ('DF,{}'.format(a + 1)) and Matriz1[a][5] == ' ':
                    jogadavalida = 2
                    Matriz2[a][5] = (' ')
                elif jogada == ('DG,{}'.format(a + 1)) and Matriz1[a][6] == (' '):
                    jogadavalida = 2
                    Matriz2[a][6] = (' ')
                elif jogada == ('DH,{}'.format(a + 1)) and Matriz1[a][7] == (' '):
                    jogadavalida = 2
                    Matriz2[a][7] = (' ')
                elif jogada == ('DI,{}'.format(a + 1)) and Matriz1[a][8] == (' '):
                    jogadavalida = 2
                    Matriz2[a][8] = (' ')

        if jogadavalida == 1:
            for a in range(0, 9):
                for b in range(1, 10):
                    if jogada == ('A,{}:{}'.format(a + 1, b)) and Matriz1[a][0] == (' ') and jogadavalida == 1:
                        Matriz2[a][0] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][0] = (' ')
                    elif jogada == ('B,{}:{}'.format(a + 1, b)) and Matriz1[a][1] == (' ') and jogadavalida == 1:
                        Matriz2[a][1] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][1] = (' ')
                    elif jogada == ('C,{}:{}'.format(a + 1, b)) and Matriz1[a][2] == (' ') and jogadavalida == 1:
                        Matriz2[a][2] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][2] = (' ')
                    elif jogada == ('D,{}:{}'.format(a + 1, b)) and Matriz1[a][3] == (' ') and jogadavalida == 1:
                        Matriz2[a][3] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][3] = (' ')
                    elif jogada == ('E,{}:{}'.format(a + 1, b)) and Matriz1[a][4] == (' ') and jogadavalida == 1:
                        Matriz2[a][4] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][4] = (' ')
                    elif jogada == ('F,{}:{}'.format(a + 1, b)) and Matriz1[a][5] == (' ') and jogadavalida == 1:
                        Matriz2[a][5] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][5] = (' ')
                    elif jogada == ('G,{}:{}'.format(a + 1, b)) and Matriz1[a][6] == (' ') and jogadavalida == 1:
                        Matriz2[a][6] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][6] = (' ')
                    elif jogada == ('H,{}:{}'.format(a + 1, b)) and Matriz1[a][7] == (' ') and jogadavalida == 1:
                        Matriz2[a][7] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][7] = (' ')
                    elif jogada == ('I,{}:{}'.format(a + 1, b)) and Matriz1[a][8] == (' ') and jogadavalida == 1:
                        Matriz2[a][8] = b
                        jogadavalida = 4
                        v = validacao_matriz(Matriz2)
                        if v == 0:
                            jogadavalida = 3
                            Matriz2[a][8] = (' ')

        if jogadavalida == 1:
            print('Jogada invalida, lembre-se de utilizar caracteres de A-I e numeros de 0-9 que nao estejam presentes na posicao inicial ')
        elif jogadavalida == 3:
            print('Valores nao compativeis com as regras do Sudoku')

        # QUANDO TERMINAR A PARTIDA
        contador = 0
        for o in range(9):
            for p in range(9):
                if Matriz2[o][p] == (' '):
                    contador = contador + 1
        if contador == 0:
            terminodejogo = 1
            print('Parabéns! Você venceu!')
            print(f'Quantidade de jogadas: {jogadas_cont}')
        grade_sudoku_jogo(Matriz1, Matriz2)


elif z == 2:
  loop = True
  while loop:
########### MODO BACH ###################
# 1) testar se os valores se sobrepoem
# 2) testar se as colunas e linhas sao iguais
# 3) testar se as matrizes são válidas
    try:
      MatrizJogadas = gerador_de_matriz_para_grade(arquivo_jogo)
      MatrizPistas = gerador_de_matriz_para_grade(arquivo_configuracao)
      validadematrizPistas = validacao_matriz(MatrizPistas)
      if validadematrizPistas == 0:
          print('Configuracao de dicas invalida.')
      else:
      
          with open(arquivo_jogo, 'r') as arquivo:
              informacoes = arquivo.readlines()
      
          for i in range(len(informacoes)):
              informacoes[i] = informacoes[i].replace('\n', '')
      
          MatrizPistas = gerador_de_matriz_para_grade(arquivo_configuracao)
          MatrizPistas2 = MatrizPistas
          MatrizPistas3 = MatrizPistas
      
          for i in range(len(informacoes)):
              coluna = informacoes[i][0]
              linha = informacoes[i][2]
              linha = int(linha)
              linhareal = linha -1
              valor = informacoes[i][4]
              valor = int(valor)
              MatrizPistas2 = MatrizPistas
              v = validacao_matriz(MatrizPistas2)
              if coluna == 'A':
                  MatrizPistas2[linhareal][0] = valor
                  if MatrizPistas[linhareal][0] == ' ':
                      print('A jogada (A,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (A,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][0] = valor
      
      
              elif coluna == 'B':
                  MatrizPistas2[linhareal][1] = valor
                  if MatrizPistas[linhareal][1] == ' ':
                      print('A jogada (B,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (B,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][1] = valor
      
              elif coluna == 'C':
                  MatrizPistas2[linhareal][2] = valor
                  if MatrizPistas[linhareal][2] == ' ':
                      print('A jogada (C,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (C,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][2] = valor
              elif coluna == 'D':
                  MatrizPistas2[linhareal][3] = valor
                  if MatrizPistas[linhareal][3] == ' ':
                      print('A jogada (D,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (D,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][3] = valor
              elif coluna == 'E':
                  MatrizPistas2[linhareal][4] = valor
                  if MatrizPistas[linhareal][4] == ' ':
                      print('A jogada (E,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (E,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][4] = valor
              elif coluna == 'F':
                  MatrizPistas2[linhareal][5] = valor
                  if MatrizPistas[linhareal][5] == ' ':
                      print('A jogada (F,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (F,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][5] = valor
              elif coluna == 'G':
                  MatrizPistas2[linhareal][6] = valor
                  if MatrizPistas[linhareal][6] == ' ':
                      print('A jogada (G,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (G,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][6] = valor
              elif coluna == 'H':
                  MatrizPistas2[linhareal][7] = valor
                  if MatrizPistas[linhareal][7] == ' ':
                      print('A jogada (H,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (H,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][7] = valor
              elif coluna == 'I':
                  MatrizPistas2[linhareal][8] = valor
                  if MatrizPistas[linhareal][8] == ' ':
                      print('A jogada (I,{}) = {} eh invalida!'.format(linha,valor))
                  elif v == 0 :
                      print('A jogada (I,{}) = {} eh invalida!'.format(linha, valor))
                  elif v == 1 :
                      MatrizPistas3[linhareal][8] = valor
      
      
          verificador = 0
          for a in range(9):
              for b in range(9):
                  if MatrizPistas3[a][b] == (' '):
                      verificador = 1
          if verificador == 1:
              print('A grade foi nao foi preenchida!')
              break
          else:
              print('A grade foi preenchida com sucesso!')
              break
    except IndexError:
      print('Apenas um arquvo foi informado...')
      break
