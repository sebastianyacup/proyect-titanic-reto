import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_data_info(df):
    if df is not None:
        try:
            logging.info("Dimensiones del DataFrame: %s", df.shape)
            logging.info("Número de datos: %s", df.size)
            logging.info("Nombres de las columnas: %s", df.columns.tolist())
            logging.info("Nombres de las filas: %s", df.index.tolist())
            logging.info("Tipos de datos de las columnas: %s", df.dtypes)
            logging.info("Las 10 primeras filas:")
            logging.info(df.head(10))
            logging.info("Las 10 últimas filas:")
            logging.info(df.tail(10))
        except Exception as e:
            logging.error(f"Error al mostrar la información del DataFrame: {str(e)}")