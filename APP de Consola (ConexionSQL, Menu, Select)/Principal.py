from BD.conexion import DAO
import funciones


def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar Leyes")
            print("2.- Registrar Ley")
            print("3.- Actualizar Ley")
            print("4.- Eliminar Ley")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            leyes= dao.listarLeyes()
            if len(cursos) > 0:
                funciones.listarLeyes(leyes)
            else:
                print("No se encontraron leyes...")
        except:
            print("Ocurrió un error...")

            
    elif opcion == 2:
        ley = funciones.pedirDatosRegistro()
        try:
            dao.registrarLey(ley)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            leyes = dao.listarLeyes()
            if len(leyes) > 0:
                ley = funciones.pedirDatosActualizacion(leyes)
                if curso:
                    dao.actualizarLey(ley)
                else:
                    print("Código de ley a actualizar no encontrado...\n")
            else:
                print("No se encontraron leyes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            leyes = dao.listarLeyes()
            if len(leyes) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(leyes)
                if not(codigoEliminar == ""):
                    dao.eliminarLey(codigoEliminar)
                else:
                    print("Código de ley no encontrado...\n")
            else:
                print("No se encontraron leyes...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal() 