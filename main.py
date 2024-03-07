import os
import pandas as pd
import logging

from scripts.analisis import cargar_datos, mostrar_informacion, mostrar_pasajero, \
    mostrar_filas_pares, mostrar_primera_clase, mostrar_porcentaje_supervivencia, \
    eliminar_edad_desconocida, anadir_columna_menor_edad, \
    mostrar_porcentaje_supervivencia_edad, mostrar_porcentaje_supervivencia_clase, \
    mostrar_edad_media_mujeres_clase


logging.basicConfig(level=logging.INFO, format='%(message)s')



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def main():
    file_path = os.path.join("datos", "titanic.csv")
    df = cargar_datos.load_data(file_path)

    if df is None:
        return

    while True:
        print("\nMENU DE OPCIONES:")
        print("1. Mostrar información general del DataFrame")
        print("2. Mostrar información de un pasajero por ID")
        print("3. Mostrar filas pares del DataFrame")
        print("4. Mostrar nombres de personas en primera clase ordenados alfabéticamente")
        print("5. Mostrar porcentaje de supervivencia")
        print("6. Mostrar porcentaje de supervivencia por clase")
        print("7. Eliminar pasajeros con edad desconocida")
        print("8. Mostrar edad media de mujeres por clase")
        print("9. Añadir columna para indicar si el pasajero es menor de edad")
        print("10. Mostrar porcentaje de supervivencia por grupo de edad")
        print("11. Salir")
        print("")

        choice = input("Ingrese el número de la opción que desee: ")

        if choice == "1":
            mostrar_informacion.display_data_info(df)
        elif choice == "2":
            passenger_id = int(input("Ingrese el ID del pasajero: "))
            mostrar_pasajero.display_passenger_info(df, passenger_id)
        elif choice == "3":
            mostrar_filas_pares.display_even_rows(df)
        elif choice == "4":
            mostrar_primera_clase.display_first_class_passengers(df)
        elif choice == "5":
            mostrar_porcentaje_supervivencia.display_survival_percentage(df)
        elif choice == "6":
            mostrar_porcentaje_supervivencia_clase.display_survival_percentage_by_class(df)
        elif choice == "7":
            df = eliminar_edad_desconocida.remove_unknown_age_passengers(df)
            logging.info("Los pasajeros con edad desconocida han sido eliminados.")
        elif choice == "8":
            mostrar_edad_media_mujeres_clase.display_average_age_female_by_class(df)
        elif choice == "9":
            df = anadir_columna_menor_edad.add_minor_column(df)
            logging.info("Se ha añadido una columna para indicar si el pasajero es menor de edad.")
        elif choice == "10":
            mostrar_porcentaje_supervivencia_edad.display_survival_percentage_by_age_group(df)
        elif choice == "11":
            logging.info("Saliendo del programa...")
            break
        else:
            logging.info("Opción no válida. Por favor, ingrese un número del 1 al 11.")

if __name__ == "__main__":
    main()
