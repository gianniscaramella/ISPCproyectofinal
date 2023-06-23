import funciones


def Menu(): 
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("Seleccione una opcion")
            print("1.- Listar leyes")
            print("2.- Registrar curso")
            print("3.- Actualizar curso")
            print("4.- Eliminar curso")
            print("5.- Salir\n")
            opcion = int(input("Seleccione una opción: "))
        
            if opcion < 1 or opcion > 5:
                print("\nOpción erronea, ingrese de nuevo.\n")
            elif opcion == 5:
             continuar = False
             print("¡Gracias por usar este sistema!")
            break
        else:
            opcionCorrecta = True
            ejecutarOpcion(opcion)
             
def ejecutarOpcion(opcion):
    print(opcion)
    
    conexionDB=conexionDB()
    
    if opcion == 1:
        try:
            Leyes = conexionDB.listarleyes()
            if len(Leyes) > 0:
                funciones.listarleyes(Leyes)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        curso = function.pedirDatosRegistro()
        try:
            conexionDB.registrarCurso(Leyes)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            cursos = conexionDB.listarleyes()
            if len(Leyes) > 0:
                curso = funciones.pedirDatosActualizacion(Leyes)
                if curso:
                    conexionDB.actualizarCurso(Leyes)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            cursos = conexionDB.listarCursos()
            if len(Leyes) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(Leyes)
                if not(codigoEliminar == ""):
                    conexionDB.eliminarCurso(codigoEliminar)
                else:
                    print("Código de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

Menu()    