class Cancion:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
    
    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_canciones(canciones):
    if canciones:
        print("Canciones ingresadas:")
        for cancion in canciones:
            print(cancion)
    else:
        print("No se han ingresado canciones.")


def eliminar_cancion(canciones):
    if canciones:
        nombre = input("Ingrese el nombre de la canción a eliminar: ")
        canciones = [cancion for cancion in canciones if cancion.nombre != nombre]
        print("Canción eliminada exitosamente.")
    else:
        print("No se han ingresado canciones.")


def modificar_cancion(canciones):
    if canciones:
        nombre = input("Ingrese el nombre de la canción a modificar: ")
        for cancion in canciones:
            if cancion.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la canción: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la canción: "))
                cancion.nombre = nuevo_nombre
                cancion.anio = nuevo_anio
                print("Canción modificada exitosamente.")
                return
        print("No se encontró una canción con ese nombre.")
    else:
        print("No se han ingresado canciones.")


def ordenar_canciones(canciones, criterio):
    if canciones:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                canciones.sort(key=lambda cancion: cancion.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(canciones):
                    n = len(canciones)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = canciones[i]
                            j = i

                            while j >= gap and canciones[j - gap].nombre > temp.nombre:
                                canciones[j] = canciones[j - gap]
                                j -= gap

                            canciones[j] = temp

                        gap //= 2

                shell_sort_nombre(canciones)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(canciones, low, high):
                    pivot = canciones[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if canciones[j].nombre < pivot:
                            i += 1
                            canciones[i], canciones[j] = canciones[j], canciones[i]

                    canciones[i + 1], canciones[high] = canciones[high], canciones[i + 1]
                    return i + 1

                def quick_sort_nombre(canciones, low, high):
                    if low < high:
                        pivot_index = partition_nombre(canciones, low, high)
                        quick_sort_nombre(canciones, low, pivot_index - 1)
                        quick_sort_nombre(canciones, pivot_index + 1, high)

                quick_sort_nombre(canciones, 0, len(canciones) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                canciones.sort(key=lambda cancion: cancion.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(canciones):
                    n = len(canciones)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = canciones[i]
                            j = i

                            while j >= gap and canciones[j - gap].anio > temp.anio:
                                canciones[j] = canciones[j - gap]
                                j -= gap

                            canciones[j] = temp

                        gap //= 2

                shell_sort_anio(canciones)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(canciones, low, high):
                    pivot = canciones[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if canciones[j].anio < pivot:
                            i += 1
                            canciones[i], canciones[j] = canciones[j], canciones[i]

                    canciones[i + 1], canciones[high] = canciones[high], canciones[i + 1]
                    return i + 1

                def quick_sort_anio(canciones, low, high):
                    if low < high:
                        pivot_index = partition_anio(canciones, low, high)
                        quick_sort_anio(canciones, low, pivot_index - 1)
                        quick_sort_anio(canciones, pivot_index + 1, high)

                quick_sort_anio(canciones, 0, len(canciones) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado canciones.")


def menu():
    canciones = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar canción")
        print("2. Mostrar canciones")
        print("3. Eliminar canción")
        print("4. Modificar canción")
        print("5. Ordenar canciones por nombre")
        print("6. Ordenar canciones por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la canción: ")
            anio = int(input("Ingrese el año de la canción: "))
            cancion = Cancion(nombre, anio)
            canciones.append(cancion)
            print("Canción ingresada exitosamente.")
        elif opcion == "2":
            mostrar_canciones(canciones)
        elif opcion == "3":
            eliminar_cancion(canciones)
        elif opcion == "4":
            modificar_cancion(canciones)
        elif opcion == "5":
            ordenar_canciones(canciones, "nombre")
        elif opcion == "6":
            ordenar_canciones(canciones, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
