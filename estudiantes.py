import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ingresar_datos():
    datos = []
    while True:
        nombre = input("Nombre del estudiante (o 'salir' para terminar): ").strip()
        if nombre.lower() == 'salir':
            break
        notas_str = input("Calificaciones separadas por coma: ")
        try:
            notas = list(map(float, notas_str.split(',')))
            datos.append({'Nombre': nombre, 'Notas': notas})
        except ValueError:
            print("Error: por favor, ingresa solo números.")
    return pd.DataFrame(datos)

def calcular_promedios(df):
    if df.empty:
        print("No hay datos para calcular promedios.")
        return df
    df['Promedio'] = df['Notas'].apply(lambda x: sum(x)/len(x) if len(x) > 0 else 0)
    print("Promedios calculados.")
    return df

def mostrar_mejor(df):
    if df.empty or 'Promedio' not in df.columns:
        print("Primero ingresa datos y calcula los promedios.")
        return
    mejor = df.loc[df['Promedio'].idxmax()]
    print("Mejor estudiante: {} con promedio {:.2f}".format(mejor['Nombre'], mejor['Promedio']))

def guardar_archivo(df):
    if df.empty or 'Promedio' not in df.columns:
        print("Primero ingresa datos y calcula los promedios.")
        return
    with open('resultados.txt', 'w') as archivo:
        for _, row in df.iterrows():
            archivo.write("{}: Notas: {}, Promedio: {:.2f}\n".format(row['Nombre'], row['Notas'], row['Promedio']))
    print("Datos guardados en 'resultados.txt'")

def graficar(df):
    if df.empty or 'Promedio' not in df.columns:
        print("Primero ingresa datos y calcula los promedios.")
        return
    sns.barplot(x='Nombre', y='Promedio', data=df)
    plt.title('Promedios de estudiantes')
    plt.ylim(0, 10)
    plt.show()

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ingresar datos de estudiantes")
    print("2. Calcular promedios")
    print("3. Mostrar mejor estudiante")
    print("4. Guardar resultados en archivo")
    print("5. Mostrar gráfico de promedios")
    print("6. Salir")

def main():
    df = pd.DataFrame()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == '1':
            df = ingresar_datos()
        elif opcion == '2':
            df = calcular_promedios(df)
        elif opcion == '3':
            mostrar_mejor(df)
        elif opcion == '4':
            guardar_archivo(df)
        elif opcion == '5':
            graficar(df)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intenta otra vez.")

if __name__ == "__main__":
    main()

