import pyb
from pyb import I2C
_MODE_REGISTER = const(0x3d)
_CONFIG_MODE = const(0)
_NDOF_MODE = const(0x0c)
_CALIB_REGISTER = const(0x35)
_POWER_MODE = const(0x3E)
_MSB_TEMP_REG = const(0xFA)
_LSB_TEMP_REG = const(0xFB)
_STAT_TEMP_REG = const(0xF3)  


class IMU:  
    def __init__(self, i2c, address = 0x28):
        self.i2c = i2c
        self.address = address
        
    def calibration(self, calArray = bytearray(4)):
        buf=bytearray(1)
        self.i2c.mem_read(buf, self.address, const(0x35), 100)
        calData = buf[0]
        calArray[0] = (calData >> 6) & 0x03
        calArray[1] = (calData >> 3) & 0x03
        calArray[2] = (calData >> 2) & 0x03
        calArray[3] = calData & 0x03
        print('sys {} gyro {} accel {} mag {}'.format(*calArray))
        
    def calib(self):
        val = self.read(1, _CALIB_REGISTER)
        sys_cal = (val[0] >> 6) & 0x03
        gyro_cal = (val[0] >> 3) & 0x03
        acc_cal = (val[0] >> 2) & 0x03
        mag_cal = val[0] & 0x03
        print(val)


    def setMode(self, mode):
        self.write(_CONFIG_MODE, self.address, _MODE_REGISTER)
        pyb.delay(20)
        if(mode != _CONFIG_MODE):
            self.write(mode, self.address, _MODE_REGISTER)
            pyb.delay(10)
    
    def currentMode(self):
        val = self.read(2, _MODE_REGISTER)
        mode = val[1] << 8 | val[0]
        print(mode)
 
    def read(self, numBytes, reg):
        data = self.i2c.mem_read(numBytes, self.address, reg)
        return data
    
    def readTemp(self, numBytes, reg):
        data = self.i2c.mem_read(numBytes, 0x76, reg)
        return data
    
    def write(self, mode, devReg, valReg):
        self.i2c.mem_write(mode, devReg, valReg)
    
    

            
        
    '''  
    def eulerAngles(self):   
    def angularVelocities(self): 
    '''

if __name__ == '__main__':
    
    i = 0
    '''
     i2c = I2C(1, I2C.MASTER)
     imu = IMU(i2c) 
     imu.mode(_NDOF_MODE)
    '''
    i2c = pyb.I2C(1, pyb.I2C.MASTER)
    imu = IMU(i2c)
    imu.setMode(_CONFIG_MODE)
    imu.currentMode()
    imu.setMode(_NDOF_MODE)
    imu.read(1, _POWER_MODE)
    imu.write(0x03 ,0x76,0xF4)
    while i < 100:
        print(imu.readTemp(1, _MSB_TEMP_REG))
        print(imu.readTemp(1, _LSB_TEMP_REG))
        print(imu.readTemp(1, _STAT_TEMP_REG))
        i += 1
    '''imu.calib()'''

'''
    data = imu.read(1, 0x35)
    acc_cal = int((data[0] >> 2) & 0b11)
    print(data)
 '''   

    
        
        