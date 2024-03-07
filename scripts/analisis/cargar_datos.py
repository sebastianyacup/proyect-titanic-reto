import pandas as pd
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        logging.error("El archivo no se encuentra en la ruta especificada.")
        return None
