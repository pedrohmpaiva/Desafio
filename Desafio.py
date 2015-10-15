##Começar com while pois ao final da venda o usuário deverar escolher se vai querer continuar ou sair (Opção 6)
##Como não sabemos o número de vezes usuários irão comprar ou cancelar as vendas, iremos usar "while" e não "for"!
saida = 0
assento = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
populacao = [[['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']]]
while  saida == 0:
        ##Visualização primária do programa
        print ('---------------------------')
        print ('  SALA DE CINEMA – CINEPÊ  ')
        print ('---------------------------')
        print ('1- EXIBIR MAPA DA SALA')
        print ('2- DETALHAR INGRESSO')
        print ('3- VENDER INGRESSO')
        print ('4- CANCELAR VENDA')
        print ('5- INICIAR NOVA SESSÃO')
        print ('6- SAIR')
        opçao = input ('OPÇÃO DESEJADA: ')
        print ()
        if opçao == '1':
                print ('---------------------------')
                print ('  SALA DE CINEMA – CINEPÊ  ')
                print ('---------------------------')
                print (' MAPA DA SALA')
                print ('     A B C D E F G H I J')
                print ('  01 %s %s %s %s %s %s %s %s %s %s' %(assento [0] [0],assento [0] [1],assento [0] [2],assento [0] [3],assento [0] [4],assento [0] [5],assento [0] [6],assento [0] [7],assento [0] [8],assento [0] [9],))
                print ('  02 %s %s %s %s %s %s %s %s %s %s' %(assento [1] [0],assento [1] [1],assento [1] [2],assento [1] [3],assento [1] [4],assento [1] [5],assento [1] [6],assento [1] [7],assento [1] [8],assento [1] [9],))
                print ('  03 %s %s %s %s %s %s %s %s %s %s' %(assento [2] [0],assento [2] [1],assento [2] [2],assento [2] [3],assento [2] [4],assento [2] [5],assento [2] [6],assento [2] [7],assento [2] [8],assento [2] [9],))
                print ('  04 %s %s %s %s %s %s %s %s %s %s' %(assento [3] [0],assento [3] [1],assento [3] [2],assento [3] [3],assento [3] [4],assento [3] [5],assento [3] [6],assento [3] [7],assento [3] [8],assento [3] [9],))
                print ('  05 %s %s %s %s %s %s %s %s %s %s' %(assento [4] [0],assento [4] [1],assento [4] [2],assento [4] [3],assento [4] [4],assento [4] [5],assento [4] [6],assento [4] [7],assento [4] [8],assento [4] [9],))
                print ('  06 %s %s %s %s %s %s %s %s %s %s' %(assento [5] [0],assento [5] [1],assento [5] [2],assento [5] [3],assento [5] [4],assento [5] [5],assento [5] [6],assento [5] [7],assento [5] [8],assento [5] [9],))
                print ('  07 %s %s %s %s %s %s %s %s %s %s' %(assento [6] [0],assento [6] [1],assento [6] [2],assento [6] [3],assento [6] [4],assento [6] [5],assento [6] [6],assento [6] [7],assento [6] [8],assento [6] [9],))
                print ('  08 %s %s %s %s %s %s %s %s %s %s' %(assento [7] [0],assento [7] [1],assento [7] [2],assento [7] [3],assento [7] [4],assento [7] [5],assento [7] [6],assento [7] [7],assento [7] [8],assento [7] [9],))
                print ('  09 %s %s %s %s %s %s %s %s %s %s' %(assento [8] [0],assento [8] [1],assento [8] [2],assento [8] [3],assento [8] [4],assento [8] [5],assento [8] [6],assento [8] [7],assento [8] [8],assento [8] [9],))
                print ('  10 %s %s %s %s %s %s %s %s %s %s' %(assento [9] [0],assento [9] [1],assento [9] [2],assento [9] [3],assento [9] [4],assento [9] [5],assento [9] [6],assento [9] [7],assento [9] [8],assento [9] [9],))
                input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')
        elif opçao == '2':
                fileira = int( input ('Digite o número de uma FILEIRA (1 - 10): '))
                poltrona = input ('Digitea leira de uma FILEIRAPOLTRONA (A - J): ')
                if poltrona == "A" or poltrona == 'a':
                        poltrona = 0
                elif poltrona == "B" or poltrona == 'b':
                        poltrona = 1
                elif poltrona == "C" or poltrona == 'b':
                        poltrona = 2
                elif poltrona == "D" or poltrona == 'c':
                        poltrona = 3
                elif poltrona == "E" or poltrona == 'e':
                        poltrona = 4
                elif poltrona == "F" or poltrona == 'f':
                        poltrona = 5
                elif poltrona == "G" or poltrona == 'g':
                        poltrona = 6
                elif poltrona == "H" or poltrona == 'h':
                        poltrona = 7
                elif poltrona == "I" or poltrona == 'i':
                        poltrona = 8
                elif poltrona == "J" or poltrona == 'j':
                        poltrona = 9
                if fileira > 10 or assento [fileira -1] [poltrona] == '-':
                        print ('ERRO! POLTRONA NÃO RESERVADA OU NÃO EXISTENTE')
                else:
                        print ('CLIENTE: %s' %populacao [fileira -1] [poltrona] [0])
                        print ('ESTUDANTE: %s' %populacao [fileira -1] [poltrona] [1])
                        input (' PRESSIONE QUALQUER TECLA PARA VOLTAR... ')

        elif opçao == '3':

                fileira = int( input ('FILEIRA: '))
                poltrona = input ('POLTRONA: ')

                fileira = int( input ('Digite o número de uma FILEIRA (1 - 10): '))
                poltrona = input ('Digitea leira de uma FILEIRAPOLTRONA (A - J): ')
                if poltrona == "A" or poltrona == 'a':
                        poltrona = 0
                elif poltrona == "B" or poltrona == 'b':
                        poltrona = 1
                elif poltrona == "C" or poltrona == 'b':
                        poltrona = 2
                elif poltrona == "D" or poltrona == 'c':
                        poltrona = 3
                elif poltrona == "E" or poltrona == 'e':
                        poltrona = 4
                elif poltrona == "F" or poltrona == 'f':
                        poltrona = 5
                elif poltrona == "G" or poltrona == 'g':
                        poltrona = 6
                elif poltrona == "H" or poltrona == 'h':
                        poltrona = 7
                elif poltrona == "I" or poltrona == 'i':
                        poltrona = 8
                elif poltrona == "J" or poltrona == 'j':
                        poltrona = 9

                if assento [fileira - 1] [poltrona] == 'x' or fileira >= 11:
                        #Verifica se a poltrona existe ou se já esta reservada
                        print ('ERRO! POLTRONA NÃO EXISTENTE OU JÁ RESERVADA')
                else:
                        cliente = input ('CLIENTE: ')
                        estudante = input ('ESTUDANTE (S/N): ')
                        if estudante == 's' or estudante == 'S':
                                estudante = 'SIM'
                        elif estudante == 'n' or estudante == 'N':
                                estudante = 'NÃO'

                                assento [fileira - 1] [poltrona] = 'x'
                                #Primeira modificação em populacao sera para nome do cliente
                                populacao [fileira -1] [poltrona] [0] = cliente
                                #Segunda modificação sera para se o cliente é estudante
                                populacao [fileira -1] [poltrona] [1] = "%s" %(estudante)
                                input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')

        elif opçao == '4':
                fileira = int( input ('Digite o número de uma FILEIRA (1 - 10): '))
                poltrona = input ('Digitea leira de uma FILEIRAPOLTRONA (A - J): ')
                if poltrona == "A" or poltrona == 'a':
                        poltrona = 0
                elif poltrona == "B" or poltrona == 'b':
                        poltrona = 1
                elif poltrona == "C" or poltrona == 'b':
                        poltrona = 2
                elif poltrona == "D" or poltrona == 'c':
                        poltrona = 3
                elif poltrona == "E" or poltrona == 'e':
                        poltrona = 4
                elif poltrona == "F" or poltrona == 'f':
                        poltrona = 5
                elif poltrona == "G" or poltrona == 'g':
                        poltrona = 6
                elif poltrona == "H" or poltrona == 'h':
                        poltrona = 7
                elif poltrona == "I" or poltrona == 'i':
                        poltrona = 8
                elif poltrona == "J" or poltrona == 'j':
                        poltrona = 9

                if assento [fileira - 1] [poltrona] == 'x':
                        confirmacao = input ('CONFIRMAR CANCELAMENTO (S/N): ')
                        if confirmacao == 's' or 'S':
                                assento [fileira -1] [poltrona] = '-'
                                populacao [fileira -1] [poltrona] [0] = '-'
                                populacao [fileira -1] [poltrona] [1] = '-'
                                input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')
                        else:
                                pass
                else:
                        print ('ERRO! ASSENTO NÃO ESTA RESERVADO')

        elif opçao == '5':
                confirmacao = input ('CONFIRMAR NOVA SESSÃO (S/N): ')
                if confirmacao == 's' or confirmacao == 'S':
                        assento = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
                        populacao = [[['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']], [['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-'], ['-', '-']]]
                        print ('NOVA SESSÃO INICIADA!')
                        input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')
                else:
                        pass

        elif opçao == '6':
                saida = 1
        else:
                input ("OPEÇÃO INCORRENTA! ESCOLHA UM DAS OPÇÃO ACIMA")

