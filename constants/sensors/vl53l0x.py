from constants.sensors.abstraction import ISensorConstant


class VL53L0XSensorConstant(ISensorConstant):
    """
    VL53L0XSensorConstant is a constant for the VL53L0X sensor.
    """

    NAME = ISensorConstant.VL53L0X
    I2C_SCL = 22
    I2C_SDA = 21
    MEASUREMENT_TIMING_BUDGET = 20000
