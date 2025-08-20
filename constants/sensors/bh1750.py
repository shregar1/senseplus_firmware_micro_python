from constants.sensors.abstraction import ISensorConstant


class BH1750SensorConstant(ISensorConstant):
    """
    BH1750SensorConstant is a constant for the BH1750 sensor.
    """

    NAME = ISensorConstant.BH1750
    I2C_SCL = 22
    I2C_SDA = 21
