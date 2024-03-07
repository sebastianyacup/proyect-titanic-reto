import logging



logging.basicConfig(level=logging.INFO, format='%(message)s')
def display_first_class_passengers(df):
    if df is not None:
        try:
            first_class_passengers = df[df['Pclass'] == 1]['Name'].sort_values()
            logging.info("Nombres de personas que iban en primera clase ordenados alfabéticamente:")
            logging.info(first_class_passengers)
        except Exception as e:
            logging.error(f"Error al mostrar los nombres de las personas que iban en primera clase: {str(e)}")