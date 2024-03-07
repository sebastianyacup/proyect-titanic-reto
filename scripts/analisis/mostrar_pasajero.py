import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def display_passenger_info(df, passenger_id):
    if df is not None:
        try:
            passenger = df.loc[df['PassengerId'] == passenger_id]
            if not passenger.empty:
                logging.info("Datos del pasajero con identificador %s:", passenger_id)
                logging.info(passenger)
            else:
                logging.info("No se encontraron datos para el pasajero con identificador %s", passenger_id)
        except Exception as e:
            logging.error(f"Error al mostrar la información del pasajero con identificador {passenger_id}: {str(e)}")
