from Models import Livro, Estante
import View, Construtor

livro1 = Livro.Livro("A Turma da Mônica", "Mauricio de Souza", 400)
livro2 = Livro.Livro("Sitio do Pica Pau Amarelo", "Monteiro Lobato", 200)
estante = Estante.Estante()

estante.adicionar_livro(livro1)
estante.adicionar_livro(livro2)

print(livro1)
print("Página Atual:", livro1.get_pagina_atual())
print("Marcando página...")
livro1.marcar_pagina(200)
print("Página marcada!")
print("Página Atual:",livro1.get_pagina_atual())
print("Quantidade de páginas restantes:",livro1.get_quant_paginas_restantes())
print(f"Percentual de Leitura: {livro1.get_percentual_leitura()}%")
livro1.atualizar_status(livro1.get_percentual_leitura())
livro2.atualizar_status(livro2.get_percentual_leitura())

print("\nLIVROS CADASTRADOS:")
View.View.imprimir_lista(estante.get_lista_livros())

print("\nLEITURAS NÃO INICIADAS")
View.View.imprimir_lista(estante.get_lista_livros_nao_iniciados())

print("\nLEITURAS EM CURSO")
View.View.imprimir_lista(estante.get_lista_livros_em_curso())

print("\nLEITURAS FINALIZADAS")
View.View.imprimir_lista(estante.get_lista_livros_finalizados())
