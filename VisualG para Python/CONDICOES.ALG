Algoritmo "Condicoes"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Lucas
// Data atual  : 23/10/2024
Var

   numero : inteiro

Inicio

   escreval("## JOGO DO TIGRINHO ##")
   escreval("Digite um n�mero")
   leia (numero)
   se (numero = 10) entao
      escreval("Parab�ns, voc� ganhou!!!")
   senao
      escreval("Infelizmente voc� n�o ganhou. Tente novamente")
   fimse

   escreval()

   Escreval("## M�ltiplos ##")
   se(numero mod 2 = 0) entao
      escreval("� m�ltiplo de dois")
   senao("N�o � m�ltiplo de dois")
   fimse

Fimalgoritmo