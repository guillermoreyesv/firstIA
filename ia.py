import tensorflow as tf
import numpy as np


class FirstIA:
    def __init__(self, inches):
        # VALORES INICIALES
        self.inches = inches
        # PARA ESTE EJEMPLO, DEFINIMOS LOS CM CON BASE A UNA FORMULA
        self.centimeters = [float(i*2.54) for i in inches]
        self.model = None

    def train(self, epochs, model_name='inches.h5', verbose=False):
        # DEFINIMOS VALORES DE ENTRADA
        inches_np = np.array(object=self.inches, dtype=float)
        # DEFINIMOS VALORES DE SALIDA
        centimeters_np = np.array(object=self.centimeters, dtype=float)

        # DEFINIMOS LAS CAPAS Y LAS NEURONAS
        layer_one = tf.keras.layers.Dense(units=1, input_shape=[1])
        try:
            # SI YA EXISTE UN MODELO PREVIAMENTE GUARDADO LO USAMOS
            model = tf.keras.models.load_model(model_name)
        except Exception:
            print(f'Not found model, creating new {model_name}')
            # AGREGAMOS LAS CAPAS
            model = tf.keras.Sequential([layer_one])

            # COMPILAMOS LA RED
            model.compile(
                optimizer=tf.keras.optimizers.Adam(0.01),
                loss='mean_squared_error'
            )

            # ENTRENAMOS LA RED
            model.fit(
                x=inches_np,
                y=centimeters_np,
                epochs=epochs,
                verbose=False)

            # GUARDAMOS PARA FUTUROS USOS
            model.save(model_name)

        self.model = model

    def predict(self, value):
        # CALCULAMOS EL VALOR
        resultado = self.model.predict([value], verbose=False)
        return resultado[0][0]
