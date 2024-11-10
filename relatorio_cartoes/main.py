import csv

soma_c6 = 0
soma_nupf = 0
soma_nupj = 0
soma_bb = 0

uber = 0
giassi = 0
facebook = 0
fort = 0
mercado_livre = 0
bom_gosto = 0
imperat = 0

with open('./dados.csv', "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        #print(linha)
        banco = linha[0]
        descricao = linha[1]
        valor = float(linha[2])
        
        # Somando o valor de cada cartão
        match banco:
            case "C6":
                soma_c6 += valor
            case "BB":
                soma_bb += valor
            case "NUBANK PJ":
                soma_nupj += valor
            case "NUBANK":
                soma_nupf += valor

        if("UBER" in descricao):
            uber += valor
        elif("GIASSI" in descricao):
            giassi += valor
        elif("FACEBOOK" in descricao):
            facebook += valor
        elif("FORT" in descricao):
            fort += valor
        elif("MERCADOLIVRE" in descricao):
            mercado_livre += valor
        elif("BOM GOSTO" in descricao):
            bom_gosto += valor
        elif("IMPERAT" in descricao):
            imperat += valor
        




# Arrendondando os valores para 2 casas
soma_c6 = round(soma_c6,2)
soma_bb = round(soma_bb,2)
soma_nupj = round(soma_nupj,2)
soma_nupf = round(soma_nupf,2)
uber = round(uber,2)
giassi = round(giassi,2)
facebook = round(facebook,2)
fort = round(fort,2)
imperat = round(imperat,2)
mercado_livre = round(mercado_livre,2)
bom_gosto = round(bom_gosto,2)


print("SOMA DOS BANCOS")
print("Soma Banco C6: ", soma_c6)
print("Soma Banco BB: ", soma_bb)
print("Soma Banco NuPF: ", soma_nupj)
print("Soma Banco NuPJ: ", soma_nupf)

print("PRINCIPAIS COMPRAS")
print("Soma Uber: ", uber)
print("Soma Giassi: ", giassi)
print("Soma Facebook: ", facebook)
print("Soma Fort: ", fort)
print("Soma Imperatriz: ", imperat)
print("Soma Mercado Livre: ", mercado_livre)
print("Soma Bom Gosto: ", bom_gosto)





