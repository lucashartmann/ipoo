Algoritmo "Sistema de conversao"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/10/2024
Var
   reais, dolar, cotacao_dolar: real

Inicio
   Escreval("## Sistema de convers�o de reais para dolar")
   cotacao_dolar <- 5,71
   Escreval("Informe o valor para a convers�o:")
   leia (reais)
   Escreval("Informe a cota��o atual do dolar:")
   leia(cotacao_dolar)
   dolar <- reais / cotacao_dolar
   Escreval("Sua quantidade de dolar: ", dolar:2:2)
   escreval()

   Escreval("## Sistema de convers�o de dolar para reais")
   Escreval("Informe o valor para a convers�o:")
   leia (dolar)
   Escreval("Informe a cota��o atual do dolar:")
   leia(cotacao_dolar)
   reais <- dolar * cotacao_dolar
   Escreval("Sua quantidade de reais: ", reais:2:2)
   escreval()

Fimalgoritmo