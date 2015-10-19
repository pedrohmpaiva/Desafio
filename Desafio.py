##Começar com while pois ao final da venda o usuário deverar escolher se vai querer continuar ou sair (Opção 6)
##Como não sabemos o número de vezes usuários irão comprar ou cancelar as vendas, iremos usar "while" e não "for"!

#Variaveis para o usuário definir quantas colunas e quantos assento possui enfileirados
quantidade_fileira = 10

quantidade_poltrona = 'J'# Valor da quantidade_fileira tem de ser menor ou igual a 25 para que esteja entre o alfabeto maiusculo

quantidade_poltronafmt = quantidade_poltrona #Variavel usada para apresentar ao usuário quando pedir valores da poltrona
quantidade_poltrona = ord (quantidade_poltrona) - ord ('A') + 1

#Lista que vai conter representação do caracter '-', para assento vazio, e 'x para assento reservado'
assento = []

for icoluna in range (quantidade_fileira):
    coluna = []
    for ipoltrona in range (quantidade_poltrona):
        poltrona = '-'
        coluna.append (poltrona)
    assento.append (coluna)

#Lista para dados das pessoas que iram ocupar os assentos
populacao = []

for icoluna in range (quantidade_fileira):
    coluna = []
    for ipoltrona in range (quantidade_poltrona):
        nome_estudante = ['-','-']
        coluna.append (nome_estudante)
    populacao.append (coluna)

saida = False
#Feito converção para string para programa posteriormente se usuário esta entrando com valor incorreto
while  not saida:
        ##Visualização primária do programa
        print ()
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
                print ()
                print ('---------------------------')
                print ('  SALA DE CINEMA – CINEPÊ  ')
                print ('---------------------------')
                print ('       MAPA DA SALA')
                poltronaFmt = ('     ')
                #Imprimir as letras que representam as poutronas
                for c in range (quantidade_fileira):
                    poltronaFmt += chr(ord('A') + c) + ' '
                print (poltronaFmt)

                #Impressão das fileiras juntamente com o número de representação de cada uma
                for icoluna in range (quantidade_fileira):
                    #Foi colocado decisões para que o layout da impressão do mapa não seja impresso incorretamente
                    if icoluna < 9:
                        fileiraFmt = ('   ')
                    else:
                        fileiraFmt = ('  ')
                    for ipoltrona in range (quantidade_poltrona):
                        fileiraFmt += str (assento [icoluna] [ipoltrona]) + ' '
                    #Soma icoluna + 1 é para imprimir números de fileiras começando com 1
                    print (icoluna + 1, fileiraFmt)

                input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')
        elif opçao == '2':

                # Verificação para entrada de dados corretos
                mataburro = []
                for i in range (quantidade_fileira):
                    valor_burro = str (i + 1)
                    mataburro.append (valor_burro)

                fileira = input ('Digite o número de uma FILEIRA (1 - %d): '%quantidade_fileira)

                while fileira not in mataburro:
                    fileira = input ('ENTRADA INCORRETA!!!Digite o número de uma FILEIRA (1 - %d): '%quantidade_fileira)

                fileira = int (fileira)



                poltrona = input ('Digite a letra de uma POLTRONA (A - %s): '%quantidade_poltronafmt)

                # Verificação para entrada de dados corretos.Caso usuário entre com outro dados a não ser letras maiúsculas
                while ord (poltrona) < ord ('A') or ord(poltrona) > ord ('Z'):
                    poltrona = input ('ENTRADA INCORRETA!!!Digite a letra de uma POLTRONA (A - %s): '%quantidade_poltronafmt)


                #Converção de representação de poltrona para inteiro para utilização mais fácil posteriormente se atingir na flexibilidade do programa
                poltrona = ord (poltrona) - ord ('A')

                if fileira > 10 or assento [fileira -1] [poltrona] == '-' or poltrona > ord('Z'):
                        print ()
                        print ('ERRO! POLTRONA NÃO RESERVADA OU NÃO EXISTENTE')
                else:
                        print ()
                        print ('CLIENTE: %s' %populacao [fileira -1] [poltrona] [0])
                        print ('ESTUDANTE: %s' %populacao [fileira -1] [poltrona] [1])
                        print ()
                        input ('PRESSIONE QUALQUER TECLA PARA VOLTAR... ')
                        print ()

        elif opçao == '3':

                # Verificação para entrada de dados corretos
                mataburro = []
                for i in range (quantidade_fileira):
                    valor_burro = str (i + 1)
                    mataburro.append (valor_burro)

                fileira = input ('Digite o número de uma FILEIRA (1 - %d): '%quantidade_fileira)

                while fileira not in mataburro:
                    fileira = input ('ENTRADA INCORRETA!!!Digite o número de uma FILEIRA (1 - %d): '%quantidade_fileira)

                fileira = int (fileira)



                poltrona = input ('Digite a letra de uma POLTRONA (A - %s): '%quantidade_poltronafmt)

                # Verificação para entrada de dados corretos.Caso usuário entre com outro dados a não ser letras maiúsculas
                while ord (poltrona) < ord ('A') or ord(poltrona) > ord ('Z'):
                    poltrona = input ('ENTRADA INCORRETA!!!Digite a letra de uma POLTRONA (A - %s): '%quantidade_poltronafmt)


                #Converção de representação de poltrona para inteiro para utilização mais fácil posteriormente se atingir na flexibilidade do programa
                poltrona = ord (poltrona) - ord ('A')

                if assento [fileira -1] [poltrona] == 'x' or fileira > quantidade_fileira:
                        #Verifica se a poltrona existe ou se já esta reservada
                        print ('ERRO! POLTRONA NÃO EXISTENTE OU JÁ RESERVADA')
                else:
                        cliente = input ('CLIENTE: ')
                        estudante = input ('ESTUDANTE (S/N): ')
                        if estudante == 's' or estudante == 'S':
                                estudante = 'SIM'
                        elif estudante == 'n' or estudante == 'N':
                                estudante = 'NÃO'
                        assento [fileira -1] [poltrona] = 'x'
                        #Primeira modificação em populacao sera para nome do cliente
                        populacao [fileira -1] [poltrona] [0] = cliente
                        #Segunda modificação sera para se o cliente é estudante
                        populacao [fileira -1] [poltrona] [1] = "%s" %(estudante)
                        input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')

        elif opçao == '4':

                # Verificação para entrada de dados corretos
                mataburro = []
                for i in range (quantidade_fileira):
                    valor_burro = str (i + 1)
                    mataburro.append (valor_burro)

                fileira = input ('Digite o número de uma FILEIRA (1 - %d): '%quantidade_fileira)

                while fileira not in mataburro:
                    fileira = input ('ENTRADA INCORRETA!!!Digite o número de uma FILEIRA (1 - %d): '%quantidade_fileira)

                fileira = int (fileira)



                poltrona = input ('Digite a letra de uma POLTRONA (A - %s): '%quantidade_poltronafmt)

                # Verificação para entrada de dados corretos.Caso usuário entre com outro dados a não ser letras maiúsculas
                while ord (poltrona) < ord ('A') or ord(poltrona) > ord ('Z'):
                    poltrona = input ('ENTRADA INCORRETA!!!Digite a letra de uma POLTRONA (A - %s): '%quantidade_poltronafmt)


                #Converção de representação de poltrona para inteiro para utilização mais fácil posteriormente se atingir na flexibilidade do programa
                poltrona = ord (poltrona) - ord ('A')

                if assento [fileira - 1] [poltrona] == 'x':
                    confirmacao = input ('CONFIRMAR CANCELAMENTO (S/N): ')
                    if confirmacao == 's' or confirmacao == 'S':
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
                        for icoluna in range (quantidade_fileira):
                            linha = []
                            for ipoltrona in range (quantidade_poltrona):
                                poltrona = '-'
                                linha.append (poltrona)
                            assento.append (linha)


                        for icoluna in range (quantidade_fileira):
                            linha = []
                            for ipoltrona in range (quantidade_poltrona):
                                poltrona = ['-','-']
                                linha.append (poltrona)
                            populacao.append (linha)

                        print ('NOVA SESSÃO INICIADA!')
                        input ('PRESSIONE QUALQUER TECLA PARA VOLTAR...')
                else:
                        pass

        elif opçao == '6':
                saida = True
        else:
                input ("OPEÇÃO INCORRENTA! ESCOLHA UM DAS OPÇÃO ACIMA")
