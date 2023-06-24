def listarLeyes(Leyes):
    print("\nLeyes: \n")
    contador = 1
    for ley in ley:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} créditos)"
        print(datos.format(contador, ley[0], ley[1], ley[2]))
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

    ley = (codigo, nombre, creditos)
    return ley

def pedirDatosActualizacion(leyes):
    listarLeyes(leyes)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del curso a editar: ")
    for ley in cursos:
        if ley[0] == codigoEditar:
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

    return leyes


def pedirDatosEliminacion(leyes):
    listarLeyes(leyes)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for ley in leyes:
        if ley[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar