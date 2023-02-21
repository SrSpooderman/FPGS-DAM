array =[[" w ", " S ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w "],
        [" w ", " c ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " c ", " w ", " w "],
        [" w ", " c ", " w ", " c ", " w ", " c ", " c ", " c ", " c ", " c ", " w ", " w "],
        [" w ", " c ", " w ", " c ", " w ", " c ", " w ", " w ", " c ", " w ", " w ", " w "],
        [" w ", " c ", " c ", " c ", " w ", " c ", " w ", " c ", " c ", " c ", " c ", " w "],
        [" w ", " w ", " w ", " c ", " c ", " c ", " w ", " c ", " w ", " w ", " c ", " w "],
        [" E ", " c ", " c ", " c ", " w ", " c ", " w ", " c ", " w ", " c ", " c ", " w "],
        [" w ", " w ", " c ", " w ", " w ", " c ", " w ", " c ", " w ", " w ", " w ", " w "],
        [" w ", " w ", " c ", " w ", " w ", " c ", " w ", " c ", " c ", " c ", " w ", " w "],
        [" w ", " c ", " c ", " w ", " w ", " c ", " w ", " w ", " w ", " c ", " w ", " w "],
        [" w ", " w ", " c ", " c ", " c ", " c ", " c ", " w ", " w ", " c ", " w ", " w "],
        [" w ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w ", " w "]]
muros = []
for y in range(0,len(array)):
    for x in range(0,len(array[y])):
        uwu = array[y][x]
        if uwu == " w ":
            muros.append([x,y])

print(muros)