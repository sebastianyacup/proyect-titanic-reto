import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_survival_percentage_by_class(df):
    if df is not None:
        try:
            survived_percentage_by_class = df.groupby('Pclass')['Survived'].mean() * 100
            logging.info("Porcentaje de personas que sobrevivieron en cada clase:")
            logging.info(survived_percentage_by_class)
        except Exception as e:
            logging.error(f"Error al calcular el porcentaje de supervivencia por clase: {str(e)}")