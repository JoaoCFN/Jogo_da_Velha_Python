# NECESSÁRIO PARA O PC REALIZAR AS ESCOLHAS
from random import randint
# NECESSÁRIO PARA LIMPAR O CONSOLE
import os

# FUNÇÃO QUE MOSTRA TABULEIRO NA TELA AO USUÁRIO
def tabuleiro(linha1, linha2, linha3):
    print("TABULEIRO DA PARTIDA")
    print("{} {} {}".format(linha1[0], linha1[1], linha1[2]))
    print("{} {} {}".format(linha2[0], linha2[1], linha2[2]))
    print("{} {} {}".format(linha3[0], linha3[1], linha3[2]))

# FUNÇÃO QUE MOSTRA O TABULEIRO NÚMERADO COM AS OPÇÕES DO JOGADOR
def tabuleiro_numerado(linha1, linha2, linha3):
    print("POSIÇÕES")
    print("0){} 1){} 2){}".format(linha1[0], linha1[1], linha1[2]))
    print("3){} 4){} 5){}".format(linha2[0], linha2[1], linha2[2]))
    print("6){} 7){} 8){}".format(linha3[0], linha3[1], linha3[2]))

# FUNÇÃO QUE CONTÉM TODA A LÓGICA DO JOGO DA VELHA
def start_game(linha1, linha2, linha3, avatar_player1, avatar_player2):
    # LIMPAR TELA
    os.system('cls')
    # VAR PARA CONVERSOR DE PARÂMETRO
    jogada = 0
    numero_jogadas_player = 0
    print("=" * 40)
    print("COMEÇOU!")
    tabuleiro(linha1, linha2, linha3)
    print("=" * 40)
    while True:
        tabuleiro_numerado(linha1, linha2, linha3)
        opcao_jogador = int(input("DIGITE ONDE DESEJA JOGAR\n"))
        # LIMPAR TELA
        os.system('cls')

        if opcao_jogador >= 0 and opcao_jogador <= 8:
            if opcao_jogador >= 0 and opcao_jogador <= 2:
                # TESTA SE A POSIÇÃO ESCOLHIDA ESTÁ DISPONÍVEL PARA JOGAR
                if linha1[opcao_jogador] == "-":
                    # REALIZA A JOGADA COM O AVATAR DO COMPETIDOR
                    linha1[opcao_jogador] = avatar_player1
                    numero_jogadas_player += 1
                else:
                    print("NÃO DÁ PARA JOGAR NESSA POSIÇÃO")
                    # SE A JOGADA NÃO FOR REALIZADA PELO JOGADOR ELE PULA O RESTANTE
                    # DO BLOCO E RETORNA AO LOOP
                    continue
            elif opcao_jogador > 2 and opcao_jogador <= 5:
                # CONVERSÃO DA OPÇÃO ESCOLHIDA PELO USUÁRIO EM UM NÚMERO QUE ESTEJA
                # NO RANGE DOS VETORES
                if opcao_jogador == 3: jogada = 0
                elif opcao_jogador == 4: jogada = 1
                elif opcao_jogador == 5: jogada = 2
                # TESTA SE A POSIÇÃO ESCOLHIDA ESTÁ DISPONÍVEL PARA JOGAR
                if linha2[jogada] == "-":
                    # REALIZA A JOGADA COM O AVATAR DO COMPETIDOR
                    linha2[jogada] = avatar_player1
                    numero_jogadas_player += 1
                else:
                    print("NÃO DÁ PARA JOGAR NESSA POSIÇÃO")
                    # SE A JOGADA NÃO FOR REALIZADA PELO JOGADOR ELE PULA O RESTANTE
                    # DO BLOCO E RETORNA AO LOOP
                    continue
            elif opcao_jogador > 5 and opcao_jogador <= 8:
                # CONVERSÃO DA OPÇÃO ESCOLHIDA PELO USUÁRIO EM UM NÚMERO QUE ESTEJA
                # NO RANGE DOS VETORES
                if opcao_jogador == 6: jogada = 0
                elif opcao_jogador == 7: jogada = 1
                elif opcao_jogador == 8: jogada = 2
                # TESTA SE A POSIÇÃO ESCOLHIDA ESTÁ DISPONÍVEL PARA JOGAR
                if linha3[jogada] == "-":
                    # REALIZA A JOGADA COM O AVATAR DO COMPETIDOR
                    linha3[jogada] = avatar_player1
                    numero_jogadas_player += 1
                else:
                    print("NÃO DÁ PARA JOGAR NESSA POSIÇÃO")
                    # SE A JOGADA NÃO FOR REALIZADA PELO JOGADOR ELE PULA O RESTANTE
                    # DO BLOCO E RETORNA AO LOOP
                    continue

            # SE O JOGO NÃO FOR FINALIZADO EM 5 RODADAS É POR QUE DEU VERA
            if numero_jogadas_player == 5:
                print("DEU VERA")
                break
            else:
                jogadas_pc(linha1, linha2, linha3, avatar_player2, opcao_jogador)

                # TESTES LÓGICOS DO JOGO DA VELHA EM SI
                # TESTE VERTICAL - COLUNAS
                if linha1[0] == "X" and linha2[0] == "X" and linha3[0] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha1[1] == "X" and linha2[1] == "X" and linha3[1] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha1[2] == "X" and linha2[2] == "X" and linha3[2] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha1[0] == "O" and linha2[0] == "O" and linha3[0] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
                if linha1[1] == "O" and linha2[1] == "O" and linha3[1] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
                if linha1[2] == "O" and linha2[2] == "O" and linha3[2] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break


                # TESTE HORIZONTAL - LINHAS
                if linha1[0] == "X" and linha1[1] == "X" and linha1[2] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha2[0] == "X" and linha2[1] == "X" and linha2[2] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha3[0] == "X" and linha3[1] == "X" and linha3[2] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha1[0] == "O" and linha1[1] == "O" and linha1[2] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
                if linha2[0] == "O" and linha2[1] == "O" and linha2[2] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
                if linha3[0] == "O" and linha3[1] == "O" and linha3[2] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
                # DIAGONAL 1
                if linha1[0] == "X" and linha2[1] == "X" and linha3[2] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha1[0] == "O" and linha2[1] == "O" and linha3[2] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
                # DIAGONAL 2
                if linha1[2] == "X" and linha2[1] == "X" and linha3[0] == "X":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ VENCEU!")
                    else:
                        print("VOCÊ PERDEU!")
                    break
                if linha1[2] == "O" and linha2[1] == "O" and linha3[0] == "O":
                    tabuleiro(linha1, linha2, linha3)
                    if avatar_player1 == "X":
                        print("VOCÊ PERDEU!")
                    else:
                        print("VOCÊ VENCEU!")
                    break
            print("=" * 40)
            tabuleiro(linha1, linha2, linha3)
            print("=" * 40)

        else:
            print("Opção Inválida")

    finalizar = input("Digite algo para finalizar")
# FUNÇÃO QUE POSSIBILITA O PC REALIZAR SUAS JOGADAS
def jogadas_pc(linha1, linha2, linha3, avatar_player2, opcao_jogador):
    # VAR PARA CONVERSOR DE PARÂMETRO
    jogada = 0
    # VAR PARA SABER SE O PC JOGOU OU NÃO
    jogou = False

    #ELE SÓ SAIRÁ DO LOOP QUANDO A JOGADA FOR REALIZADA
    while jogou != True:
        opcao_pc = opcao_jogador
        # IGUALO A OPÇÃO DO PC AO DO USUÁRIO E FORÇO ELE A ESCOLHER UMA DIFERENTE
        while opcao_pc == opcao_jogador:
            opcao_pc = randint(0, 8)

        if opcao_pc >= 0 and opcao_pc <= 2:
            # TESTA SE A POSIÇÃO ESCOLHIDA ESTÁ DISPONÍVEL PARA JOGAR
            if linha1[opcao_pc] == '-':
                # REALIZA A JOGADA COM O AVATAR DO COMPETIDOR
                linha1[opcao_pc] = avatar_player2
                jogou = True
        elif opcao_pc > 2 and opcao_pc <= 5:
            # CONVERSÃO DA OPÇÃO ESCOLHIDA PELO USUÁRIO EM UM NÚMERO QUE ESTEJA
            # NO RANGE DOS VETORES
            if opcao_pc == 3: jogada = 0
            elif opcao_pc == 4: jogada = 1
            elif opcao_pc == 5: jogada = 2
            # TESTA SE A POSIÇÃO ESCOLHIDA ESTÁ DISPONÍVEL PARA JOGAR
            if linha2[jogada] == "-":
                # REALIZA A JOGADA COM O AVATAR DO COMPETIDOR
                linha2[jogada] = avatar_player2
                jogou = True
        elif opcao_pc > 5 and opcao_pc <= 8:
            # CONVERSÃO DA OPÇÃO ESCOLHIDA PELO USUÁRIO EM UM NÚMERO QUE ESTEJA
            # NO RANGE DOS VETORES
            if opcao_pc == 6:jogada = 0
            elif opcao_pc == 7: jogada = 1
            elif opcao_pc == 8: jogada = 2
            # TESTA SE A POSIÇÃO ESCOLHIDA ESTÁ DISPONÍVEL PARA JOGAR
            if linha3[jogada] == "-":
                # REALIZA A JOGADA COM O AVATAR DO COMPETIDOR
                linha3[jogada] = avatar_player2
                jogou = True

# FUNÇÃO PRINCIPAL
def main():
    #TABULEIRO FORMADO POR 3 VETORES
    linha1 = ["-", "-", "-"]
    linha2 = ["-", "-", "-"]
    linha3 = ["-", "-", "-"]

    print("=" * 40)
    print("SEJA VEM VINDO AO JOGO DA VELHA")
    print("=" * 40)
    print("ESSE SERÁ O TABULEIRO DE JOGO:")
    tabuleiro(linha1, linha2, linha3)
    print("=" * 40)

    # TESTE QUE CAPTURA ERROS DE DIGITAÇÃO DO USUÁRIO
    try:
        player1 = int(input("OPÇÕES DE JOGADOR:\n1) PARA SER O 'X' \n2) PARA SER O 'O'\n"))
        # INICIO O GAME PASSANDO OS 3 VETORES E AS OPÇÕES DO JOGADOR COMO PARÂMETRO
        if player1 == 1:
            start_game(linha1, linha2, linha3, "X", "O")
        elif player1 == 2:
            start_game(linha1, linha2, linha3, "O", "X")
        else:
            print("Opção Inválida")
    except ValueError:
        print("Digite algo válido")

#INICIA O PROGRAMA
main()
