Algoritmo "Lucas Hartmann - Loja de Picol�s"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Autor(a)    : Lucas
// Data atual  : 31/10/2024
Var
   quantidade, quantidadeTotal, number, number2, quantidadeAtual : inteiro
   desconto, parcelas, acrescimo : inteiro
   descontoTotal, parcelasTotal, acrescimoTotal : inteiro
   valorTotal, picoleValue, valorFinal, valorParcelado, valorAtual: real
   condicao, condicao2 : caractere
   valorParceladoTotal, valorFinalAtual: real

Inicio
   condicao <- "s"
   condicao2 <- "s"
   number <- 0

   enquanto ((condicao2 = "s") ou (condicao2 = "S")) faca
      enquanto ((condicao = "s") ou (condicao = "S")) faca
         enquanto (number <= 0) ou (number > 6) faca
            Escreval("#### VENDA DE PICOL�S ####")
            escreval()
            Escreval("#### MENU ####")
            Escreval("1 -- Picol� de Uva (R$1,00)")
            Escreval("2 -- Picol� de Laranja (R$1,25)")
            Escreval("3 -- Picol� de Milho (R$1,50)")
            Escreval("4 -- Picol� de Coco queimado (R$1,80)")
            Escreval("5 -- Picol� de Tamarindo (R$2,00)")
            escreval("6 -- Encerrar Programa")
            Escreval("Digite o n�mero correspondente ao picol�s que voc� deseja: ")
            leia (number)
            escolha(number)
            Caso 1
               Escreval("Quantos picol�s deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.00)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.00)
               picoleValue <- quantidade * 1.00
               escreval("###############")
               Escreval("Quantidade de picol�s de Uva comprado(s): ", quantidade)
               escreval("Valor gasto com picol�s de Uva: R$", picoleValue)
            Caso 2
               Escreval("Quantos picol�s deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.25)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.25)
               picoleValue <- quantidade * 1.25
               escreval("###############")
               Escreval("Quantidade de picol�s de Laranja comprado(s): ", quantidade)
               escreval("Valor gasto com picol�s de Laranja: R$", picoleValue)
            Caso 3
               Escreval("Quantos picol�s deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.50)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.50)
               picoleValue <- quantidade * 1.50
               escreval("###############")
               Escreval("Quantidade de picol�s de Milho comprado(s): ", quantidade)
               escreval("Valor gasto com picol�s de Milho: R$", picoleValue)
            Caso 4
               Escreval("Quantos picol�s deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.80)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.80)
               picoleValue <- quantidade * 1.80
               escreval("###############")
               Escreval("Quantidade de picol�s de Coco queimado comprado(s): ", quantidade)
               escreval("Valor gasto com picol�s de Coco queimado: R$", picoleValue)
            Caso 5
               Escreval("Quantos picol�s deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 2.00)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 2.00)
               picoleValue <- quantidade * 2.00
               escreval("###############")
               Escreval("Quantidade de picol�s de Tamarindo comprado(s): ", quantidade)
               escreval("Valor gasto com picol�s de Tamarindo: R$", picoleValue)
            caso 6
               Escreval()
               escreval("Voc� escolheu sair!")
               fimalgoritmo
            outrocaso
               escreval("N�mero digitado incorreto. Tente novamente")
         fimescolha
      fimenquanto
   escreval()
   escreval("###############")
   Escreval("Quantidade de picol�s comprados no total: ", quantidadeAtual)
   Escreval("Valor a ser pago no total: R$", valorAtual)
   escreval()
   escreval("Deseja seguir comprando? (S/N) ")
   leia(condicao)
      se ((condicao = "s") ou (condicao = "S")) entao
         condicao <- "s"
         condicao2 <- "s"
         number <- 0
         number2 <- 0
      fimse
   fimenquanto

   number2 <- 0
   enquanto (number2 <= 0) ou (number2 > 6) faca
      escreval()
      Escreval("#### CAIXA ####")
      Escreval("1 -- � vista em dinheiro ou PIX (10% OFF)")
      Escreval("2 -- No cart�o de d�bito (5% OFF)")
      Escreval("3 -- No cart�o de cr�dito em 1x")
      Escreval("4 -- No cart�o de cr�dito em 2x (+5% acr�scimo)")
      Escreval("5 -- No cart�o de cr�dito em 3x (+10% acr�scimo)")
      Escreval("6 -- No cart�o de cr�dito em 4x (+15% acr�scimo)")
      Escreval("Digite o n�mero correspondente � forma de pagamento: ")
      leia (number2)
      escolha(number2)
      caso 1
         desconto <- 10
         descontoTotal <- descontoTotal + 10
         valorFinalAtual <- valorAtual - (valorAtual * 0.10)
         valorFinal <- valorTotal - (valorTotal * 0.10)
      caso 2
         descontoTotal <- descontoTotal + 5
         desconto <- 5
         valorFinalAtual <- valorAtual - (valorAtual * 0.05)
         valorFinal <- valorTotal - (valorTotal * 0.05)
      caso 3
      caso 4
         parcelasTotal <- parcelasTotal + 2
         acrescimoTotal <- acrescimoTotal + 5
         parcelas <- 2
         acrescimo <- 5
         valorFinalAtual <- valorAtual + (valorAtual * 0.05)
         valorFinal <- valorTotal + (valorTotal * 0.05)
         valorParcelado <- valorFinal / parcelas
         valorParceladoTotal <- valorFinal / parcelasTotal
      caso 5
         parcelasTotal <- parcelasTotal + 3
         acrescimoTotal <- acrescimoTotal + 10
         parcelas <- 3
         acrescimo <- 10
         valorFinalAtual <- valorAtual + (valorAtual * 0.10)
         valorFinal <- valorTotal + (valorTotal * 0.10)
         valorParcelado <- valorFinal / parcelas
         valorParceladoTotal <- valorFinal / parcelasTotal
      caso 6
         parcelasTotal <- parcelasTotal + 4
         acrescimoTotal <- acrescimoTotal + 15
         parcelas <- 4
         acrescimo <- 15
         valorFinalAtual <- valorAtual + (valorAtual * 0.15)
         valorFinal <- valorTotal + (valorTotal * 0.15)
         valorParceladoTotal <- valorFinal / parcelasTotal
         valorParcelado <- valorFinal / parcelas
      outrocaso
         ESCREVAL("o n�mero digitado � inv�lido! Tente novamente")
      fimescolha
   fimenquanto

   escreval()
   Escreval("#### RECIBO DA COMPRA ATUAL #####")
   Escreval("Quantidade de picol�s comprados: ", quantidadeAtual)
   Escreval("Valor total: R$", valorAtual:2:1)
   Escreval("Desconto: ", desconto,"%")
   Escreval("Acr�scimo: ", acrescimo,"%")
   Escreval("N�mero de parcelas: ", parcelas)
   Escreval("Valor por parcela: R$", valorParcelado)
   Escreval("Valor final pago: R$", valorFinalAtual:2:1)

   escreval()
   escreval("Deseja seguir comprando? (S/N) ")
   leia(condicao2)
   se ((condicao2 = "s") ou (condicao2 = "S")) entao
      condicao <- "s"
      condicao2 <- "s"
      number <- 0
      quantidadeAtual <- 0
      valorAtual <- 0
      number2 <- 0
   fimse
   fimenquanto

escreval()
Escreval("#### RECIBO DO TOTAL DE TODAS COMPRAS #####")
Escreval("Quantidade total de picol�s comprados: ", quantidadeTotal)
Escreval("Valor total: R$", valorTotal:2:1)
Escreval("Desconto total: ", descontoTotal,"%")
Escreval("Acr�scimo total: ", acrescimoTotal,"%")
Escreval("N�mero de parcelas total: ", parcelasTotal)
Escreval("Valor por parcela no total: R$", valorParceladoTotal)
Escreval("Valor final pago total: R$", valorFinal:2:1)
escreval()
escreval("Obrigado por comprar conosco!")

Fimalgoritmo