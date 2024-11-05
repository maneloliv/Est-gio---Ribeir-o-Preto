def veriftexto(string, letra):
    contagem = string.count(letra.lower()) + string.count(letra.upper())
    
    if contagem > 0:
       print(f"A letra '{letra}' aparece {contagem} vezes no texto.")
    else:
        print(f"A letra '{letra}' não está no texto.")

texto = input("Digite um texto: ")
letra = input("Digite a Letra: ")
veriftexto(texto, letra)
