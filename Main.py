import funciones


def Menu(): 
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("Seleccione una opcion")
            print("1.- Listar leyes")
            print("2.- Registrar ley")
            print("3.- Actualizar ley")
            print("4.- Eliminar ley")
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
                print("No se encontraron leyes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        ley = function.pedirDatosRegistro()
        try:
            conexionDB.registrarLey(Leyes)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            leyes = conexionDB.listarleyes()
            if len(Leyes) > 0:
                ley = funciones.pedirDatosActualizacion(Leyes)
                if ley:
                    conexionDB.actualizarLey(Leyes)
                else:
                    print("Código de ley a actualizar no encontrado...\n")
            else:
                print("No se encontraron leyes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            leyes = conexionDB.listarLeyes()
            if len(Leyes) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(Leyes)
                if not(codigoEliminar == ""):
                    conexionDB.eliminarLey(codigoEliminar)
                else:
                    print("Código de ley no encontrado...\n")
            else:
                print("No se encontraron leyes...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

Menu()    
