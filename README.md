# Desafio
# Introdução
Desafio proposto em sala de aula com objetivo de controle de vendas de ingressos de uma
sala de cinema com assentos reservados.
##Requisitos software
O programa deverá exibir o seguinte menu principal:
```objc
---------------------------
  SALA DE CINEMA – CINEPÊ
---------------------------
  1- EXIBIR MAPA DA SALA
  2- DETALHAR INGRESSO
  3- VENDER INGRESSO
  4- CANCELAR VENDA
  5- INICIAR NOVA SESSÃO
  6- SAIR
  OPÇÃO DESEJADA
```
## As opções deverão funcionar da seguinte forma:

#1. EXIBIR MAPA DA SALA
Exibir um mapa da sala do cinema, onde as poltronas livres serão sinalizadas com o caractere “-” e as
poltronas reservadas com o caractere “x”, como ilustrado a seguir:
```objc
---------------------------
  SALA DE CINEMA – CINEPÊ
---------------------------
      MAPA DA SALA
   A B C D E F G H I J
01 - - - - - - - x - -
02 x x - - x - - - x -
03 - x x - x - x x - -
04 - - - - x - - x - -
05 - x - x - - - x - x
06 - x - - x x - x x -
07 - x - - - - - x x -
08 x x x - x - - - - x
09 - x x x x - - x - x
10 x x x x x x - x - -
PRESSIONE QUALQUER TECLA PARA VOLTAR...
```
Ao ser pressionada alguma tecla, deverá voltar ao menu principal.

#2. DETALHAR INGRESSO
Solicitar a digitação do número da fileira (1 - 10) e poltrona (A – J). Caso a poltrona não esteja reservada ou
não exista, uma mensagem de erro deverá ser exibida. Caso contrário, os detalhes do ingresso deverão ser
exibidos, de acordo a seguinte ilustração:
```objc
    FILEIRA: 2
    POLTRONA: E
    CLIENTE: NOME DO CLIENTE
    ESTUDANTE: NÃO
    PRESSIONE QUALQUER TECLA PARA VOLTAR...
```
 Ao ser pressionada alguma tecla, deverá voltar ao menu principal.
#3. VENDER INGRESSO
Solicitar número da fileira, poltrona, nome do cliente e se é ou não estudante, de acordo com a ilustração a
seguir:
```objc
    FILEIRA: 2
    POLTRONA: F
    CLIENTE: FULANO DE TAL
    ESTUDANTE (S/N): S
    PRESSIONE QUALQUER TECLA PARA VOLTAR...
```
O sistema deverá validar se a poltrona existe e se está disponível para reserva. Caso não esteja disponível
ou não exista, uma mensagem de erro deverá ser exibida antes mesmo de serem solicitados os dados do
cliente.
Ao ser pressionada alguma tecla, deverá ser exibido o menu principal.

#4. CANCELAR VENDA
Solicitar número da fileira e poltrona. Caso exista ingresso vendido para a posição especificada, a
confirmação de cancelamento será solicitada, conforme ilustração a seguir. Caso contrário, uma mensagem
de erro deverá ser exibida.
```objc
  FILEIRA: 2
  POLTRONA: F
  CONFIRMAR CANCELAMENTO (S/N): S
  PRESSIONE QUALQUER TECLA PARA VOLTAR...
```
Ao ser pressionada alguma tecla, deverá ser exibido o menu principal.

#5. INICIAR NOVA SESSÃO
Iniciar uma nova sessão na sala do cinema, disponibilizando todas as poltronas para venda. Deverá ser
solicitada a confirmação do usuário, conforme ilustrado a seguir:
```objc
    CONFIRMAR NOVA SESSÃO (S/N): S
    NOVA SESSÃO INICIADA!
    PRESSIONE QUALQUER TECLA PARA VOLTAR...
```
Ao ser pressionada alguma tecla, deverá ser exibido o menu principal.

#6. SAIR
Encerrar o programa.
Obs.: Não utilizar nenhuma técnica ou recurso da linguagem ainda não estudado!
