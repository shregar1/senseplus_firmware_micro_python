from constants.sensors.abstraction import ISensorConstant


class BME280SensorConstant(ISensorConstant):
    """
    BME280SensorConstant is a constant for the BME280 sensor.
    """

    NAME = ISensorConstant.BME280
    I2C_SCL = 22
    I2C_SDA = 21
