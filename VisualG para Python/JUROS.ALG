Algoritmo "juros"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/10/2024
Var
   prestacao, juros : real
   dias : inteiro

Inicio
   escreval("## SISTEMA DE COBRAN�A DE JUROS")
   escreva("Informe sua presta��o: ")
   leia (prestacao)
   escreva("Informe os dias de atraso: ")
   leia (dias)
   juros <- 2 / 100
   juros <- (prestacao * juros) * dias
   escreval
   escreval("## RESULTADO DA CONSULTA")
   escreval("Valor da presta��o: R$",prestacao:2:2)
   escreval("Dias em atraso: ", dias)
   escreval("Valor do juros: R$", juros:2:2)
   prestacao <- prestacao + juros
   escreva("Valor final para pagar: R$", prestacao:2:2)

Fimalgoritmo