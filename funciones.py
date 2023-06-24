def listarLeyes(leyes):
    print("\nLeyes: \n")
    contador = 1
    for cur in leyes:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} créditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese código: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente.")

    leyes = (codigo, nombre, creditos)
    return ley

def pedirDatosActualizacion(leyes):
    listarLeyes(leyes)
    existeCodigo = False
    codigoEditar = input("Ingrese el código de ley a editar: ")
    for cur in leyes:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre a modificar: ")

        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese créditos a modificar: ")
            if creditos.isnumeric():
                if (int(creditos) > 0):
                    creditosCorrecto = True
                    creditos = int(creditos)
                else:
                    print("Los créditos deben ser mayor a 0.")
            else:
                print("Créditos incorrectos: Debe ser un número únicamente.")

        ley = (codigoEditar, nombre, creditos)
    else:
        ley = None

    return ley


def pedirDatosEliminacion(leyes):
    listarLeyes(leyes)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código de ley a eliminar: ")
    for cur in leyes:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar
