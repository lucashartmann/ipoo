Algoritmo "Menu Aluno"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/11/2024
Var
   // Se��o de Declara��es das vari�veis
   nome, turma: caractere
   idade, option, condicao : inteiro

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   condicao <- 0
   enquanto condicao = 0 faca
      Escreval("## Menu ##")
      Escreval("1 -- Cadastrar/editar nome")
      escreval("2 -- Cadastrar/editar Idade")
      escreval("3 -- Cadastrar/editar turma")
      escreval("4 -- Exibir dados do aluno")
      escreval("5 -- Sair do menu")
      leia(option)
      escolha(option)
      caso 1
         escreva("Digite o nome: ")
         leia(nome)
      caso 2
         escreval("Digite a idade: ")
         leia(idade)
      caso 3
         escreva("Digite a turma: ")
         leia(turma)
      caso 4
         escreval("Aluno: [Nome: ", nome, ", Idade: ", idade, ", turma: ", turma, "]")
      caso 5
         escreva("Saindo")
         condicao <- 1
      outrocaso
         escreval("Numero digitado � inv�lido, tente novamente")
      fimescolha
   fimenquanto

Fimalgoritmo