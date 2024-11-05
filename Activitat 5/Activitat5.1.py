import pandas as pd
import matplotlib.pyplot as plt

# Configuración de parámetros globales
paises = ['Afghanistan', 'India', 'United States', 'Brazil', 'Russia', 'France', 'Italy', 'Spain', 'Germany', 'China']
meses = ['2021-01', '2021-02', '2021-03', '2021-04']
ciudades = ['Malé', 'Manila', 'Bogor', 'Titagarh', 'Baranagar', 'Paris', 'Tokyo', 'Mexico City', 'Shanghai', 'New York']
ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]


### SECCIÓN A: Funciones de Análisis de COVID-19

def cargar_datos_covid(df, paises, meses):
    df['month'] = pd.to_datetime(df['date']).dt.to_period('M')
    return df[(df['location'].isin(paises)) & (df['month'].astype(str).isin(meses))]


def casos_totales_por_mes(df):
    cases_per_month = df.groupby(['location', 'month'])['total_cases'].sum().unstack()
    return cases_per_month


def muertes_totales_por_mes(df):
    deaths_per_month = df.groupby(['location', 'month'])['total_deaths'].sum().unstack()
    return deaths_per_month


def tasa_reproduccion(df):
    reproduction_rate_per_month = df.groupby(['location', 'month'])['reproduction_rate'].mean().unstack()
    return reproduction_rate_per_month


def main_covid_analysis(df, paises, meses):
    df_filtered = cargar_datos_covid(df, paises, meses)
    cases = casos_totales_por_mes(df_filtered)
    deaths = muertes_totales_por_mes(df_filtered)
    reproduction_rate = tasa_reproduccion(df_filtered)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    for country in cases.index:
        plt.plot(cases.columns.astype(str), cases.loc[country], label=country)
    plt.title("Casos Totales por Mes")
    plt.xlabel("Mes")
    plt.ylabel("Casos Totales")
    plt.legend()

    plt.subplot(1, 3, 2)
    for country in deaths.index:
        plt.plot(deaths.columns.astype(str), deaths.loc[country], label=country)
    plt.title("Muertes Totales por Mes")
    plt.xlabel("Mes")
    plt.ylabel("Muertes Totales")
    plt.legend()

    plt.subplot(1, 3, 3)
    for country in reproduction_rate.index:
        plt.plot(reproduction_rate.columns.astype(str), reproduction_rate.loc[country], label=country)
    plt.title("Tasa de Reproducción por Mes")
    plt.xlabel("Mes")
    plt.ylabel("Tasa de Reproducción")
    plt.legend()

    plt.tight_layout()
    plt.show()


### SECCIÓN B: Funciones de Análisis de Densidad de Población en Ciudades

def cargar_datos_ciudades(df, ciudades):
    return df[df['City'].isin(ciudades)]


def poblacion_total_ciudad(df):
    # Elimina comas y cualquier nota como [1]
    df['Population'] = df['Population'].str.replace(r'[^\d]', '', regex=True).astype(int)
    poblacion = df.set_index('City')['Population']
    return poblacion



def densidad_km2(df):
    densidad_km2 = df.set_index('City')['Density (/km²)'].astype(int)
    return densidad_km2


def densidad_m2(df):
    densidad_m2 = (df['Density (/km²)'] / 1e6).rename("Density (/m²)")
    densidad_m2.index = df['City']
    return densidad_m2


def main_ciudades_analysis(df, ciudades):
    df_filtered = cargar_datos_ciudades(df, ciudades)

    poblacion = poblacion_total_ciudad(df_filtered)
    densidad_km2_values = densidad_km2(df_filtered)
    densidad_m2_values = densidad_m2(df_filtered)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.pie(poblacion, labels=poblacion.index, autopct='%1.1f%%')
    plt.title("Población Total por Ciudad")

    plt.subplot(1, 3, 2)
    plt.pie(densidad_km2_values, labels=densidad_km2_values.index, autopct='%1.1f%%')
    plt.title("Densidad por KM²")

    plt.subplot(1, 3, 3)
    plt.pie(densidad_m2_values, labels=densidad_m2_values.index, autopct='%1.1f%%')
    plt.title("Densidad por M²")

    plt.tight_layout()
    plt.show()


### SECCIÓN C: Funciones de Análisis de Datos de Teléfonos Móviles

def cargar_datos_moviles(df, ids):
    return df[df['id'].isin(ids)]


def clock_speed_por_id(df):
    return df.set_index('id')['clock_speed']


def megapixeles_por_id(df):
    return df.set_index('id')['fc']


def potencia_bateria_por_id(df):
    return df.set_index('id')['battery_power']


def main_moviles_analysis(df, ids):
    df_filtered = cargar_datos_moviles(df, ids)

    clock_speed = clock_speed_por_id(df_filtered)
    megapixels = megapixeles_por_id(df_filtered)
    battery_power = potencia_bateria_por_id(df_filtered)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    clock_speed.plot(kind='bar', color='blue')
    plt.title("Clock Speed por ID")
    plt.xlabel("ID")
    plt.ylabel("Clock Speed (GHz)")

    plt.subplot(1, 3, 2)
    megapixels.plot(kind='bar', color='green')
    plt.title("Megapíxeles por ID")
    plt.xlabel("ID")
    plt.ylabel("Megapíxeles")

    plt.subplot(1, 3, 3)
    battery_power.plot(kind='bar', color='orange')
    plt.title("Potencia de Batería por ID")
    plt.xlabel("ID")
    plt.ylabel("Battery Power (mAh)")

    plt.tight_layout()
    plt.show()


### Función main para ejecutar todas las secciones

def main():
    # Ruta a la carpeta de Descargas en Windows
    ruta_descargas = 'C:/Users/Jass/Downloads/'

    # Cargar los archivos de datos
    df_covid = pd.read_csv(ruta_descargas + 'df_covid19_countries.csv')
    df_world_cities = pd.read_csv(ruta_descargas + 'List of world cities by population density.csv')
    df_test = pd.read_csv(ruta_descargas + 'test.csv')

    # Ejecutar el análisis de cada sección
    print("Sección A: Análisis de COVID-19")
    main_covid_analysis(df_covid, paises, meses)

    print("Sección B: Análisis de Densidad de Población en Ciudades")
    main_ciudades_analysis(df_world_cities, ciudades)

    print("Sección C: Análisis de Datos de Teléfonos Móviles")
    main_moviles_analysis(df_test, ids)


# Ejecutar la función main solo si este script se ejecuta como programa principal
if __name__ == "__main__":
   main()
