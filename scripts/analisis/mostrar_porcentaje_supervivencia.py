import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_survival_percentage(df):
    if df is not None:
        try:
            survived_percentage = df['Survived'].value_counts(normalize=True) * 100
            logging.info("Porcentaje de personas que sobrevivieron: %s", survived_percentage[1])
            logging.info("Porcentaje de personas que murieron: %s", survived_percentage[0])
        except Exception as e:
            logging.error(f"Error al calcular el porcentaje de supervivencia: {str(e)}")