import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_average_age_female_by_class(df):
    if df is not None:
        try:
            average_age_female_by_class = df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean()
            logging.info("Edad media de las mujeres que viajaban en cada clase:")
            logging.info(average_age_female_by_class)
        except Exception as e:
            logging.error(f"Error al calcular la edad media de las mujeres por clase: {str(e)}")