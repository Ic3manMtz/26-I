import Alex

alex = Alex.AnalizadorLexico("entrada.txt")
alex.crearLista()

total = len(alex.L)
print(f"\nTokens generados: {total}\n")

token = alex.obtenerToken()
while token is not None:
    print(token)
    token = alex.obtenerToken()