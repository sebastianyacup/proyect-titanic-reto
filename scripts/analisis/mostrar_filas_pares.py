import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_even_rows(df):
    if df is not None:
        try:
            logging.info("Filas pares del DataFrame:")
            logging.info(df.iloc[::2])
        except Exception as e:
            logging.error(f"Error al mostrar las filas pares del DataFrame: {str(e)}")
