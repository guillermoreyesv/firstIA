import tensorflow as tf
import numpy as np


class FirstIA:
    def __init__(self, inches):
        # Initial values
        self.inches = inches
        self.centimeters = [float(i*2.54) for i in inches]
        self.model = None
        pass

    def train(self, epochs, model_name='inches.h5', verbose=False):
        inches_np = np.array(object=self.inches, dtype=float)
        centimeters_np = np.array(object=self.centimeters, dtype=float)

        layer_one = tf.keras.layers.Dense(units=1, input_shape=[1])
        try:
            model = tf.keras.models.load_model(model_name)
        except Exception:
            print(f'Not found model, creating new {model_name}')
            model = tf.keras.Sequential([layer_one])

            model.compile(
                optimizer=tf.keras.optimizers.Adam(0.01),
                loss='mean_squared_error'
            )

            model.fit(
                x=inches_np,
                y=centimeters_np,
                epochs=epochs,
                verbose=False)

            model.save(model_name)

        # plt.xlabel('Epoch')
        # plt.ylabel('Loss')
        # plt.plot(training.history['loss'])
        self.model = model

    def predict(self, value):
        resultado = self.model.predict([value])
        return resultado[0][0]
