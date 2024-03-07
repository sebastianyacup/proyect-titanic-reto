import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_survival_percentage_by_age_group(df):
    if df is not None:
        try:
            survived_percentage_minor_by_class = df[df['Minor'] == True].groupby('Pclass')['Survived'].mean() * 100
            survived_percentage_adult_by_class = df[df['Minor'] == False].groupby('Pclass')['Survived'].mean() * 100
            logging.info("Porcentaje de menores que sobrevivieron en cada clase:")
            logging.info(survived_percentage_minor_by_class)
            logging.info("Porcentaje de adultos que sobrevivieron en cada clase:")
            logging.info(survived_percentage_adult_by_class)
        except Exception as e:
            logging.error(f"Error al calcular el porcentaje de supervivencia por grupo de edad: {str(e)}")
