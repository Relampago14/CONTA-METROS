rotas = {"T001": 10, "T002": 20, "T003": 30, "T004": 40, "T005": 50}

quantos_cabos = int(input("Quantos cabos serão usados? "))

for c in range(quantos_cabos):

    n_cabo = c + 1
    quais_rotas = str(input(f"Digite quais rotas o cabo {n_cabo} passa: (Ex: T001, T002...)"))
    
    lista = []
    repet = int(len(quais_rotas) / 4)
    
    i = 0
    f = 4
    
    for l in range(repet):
    
        lista.append(quais_rotas[i:f])
        
        i += 6
        f += 6
        
    chave = 0
    total = 0
        
    for c in range(len(lista)):
        
        total += rotas[lista[chave]]
        chave += 1
    
    print(f"O cabo {n_cabo} terá {total} metros")
