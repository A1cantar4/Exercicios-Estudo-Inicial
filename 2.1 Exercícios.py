# Exercícios de Variáveis envolvendo operadores (vou comentar no final apenas)

cadernos = 6
livros = 10
diferença_livro_cadernos = livros - cadernos
capítulos_em_cada_livro = 50
folhas_em_cada_capítulo = 30
total_de_folhas_por_livro = folhas_em_cada_capítulo * capítulos_em_cada_livro
total_de_folhas_geral = livros * total_de_folhas_por_livro

print("Nesta sala há:", total_de_folhas_geral, "Folhas")

if livros > cadernos:
    print("Há", diferença_livro_cadernos, "Livros a mais do que Cadernos!")
else:
    print("Há menos Livros do que Cadernos!")

# apenas (pegadinha do malandro kkkkkkk)
