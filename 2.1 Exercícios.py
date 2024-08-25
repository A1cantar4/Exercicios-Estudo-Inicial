# Exercícios de Variáveis envolvendo operadores (vou comentar no final apenas)

cadernos = 6
livros = 10
diferença_livro_cadernos = livros - cadernos
capítulos_em_cada_livro = 50
capítulos_em_cada_caderno = 10
folhas_em_cada_capítulo_livro = 30
folhas_em_cada_capítulo_caderno = 25
total_de_folhas_por_livro = folhas_em_cada_capítulo_livro * capítulos_em_cada_livro
total_de_folhas_geral_livro = livros * total_de_folhas_por_livro
total_de_folhas_por_caderno = folhas_em_cada_capítulo_caderno * capítulos_em_cada_caderno
total_de_folhas_geral_caderno = cadernos * total_de_folhas_por_caderno

total_de_folhas_união = total_de_folhas_geral_livro + total_de_folhas_geral_caderno

print("Nesta sala há:", total_de_folhas_união, "Folhas")

if livros > cadernos:
    print("Há", diferença_livro_cadernos, "Livros a mais do que Cadernos!")
else:
    print("Há menos Livros do que Cadernos!")

# apenas (pegadinha do malandro kkkkkkk)
