
# this will configure the person sensor from useful sensors to store the isentify of a user in slot 0 and save it in nvram. 
# https://www.sparkfun.com/products/21231
# https://github.com/usefulsensors/person_sensor_docs

import board
import busio
i2c = board.I2C()
i2c.try_lock()
i2c.writeto(0x62, bytes([0x05,0x01])) // sets the board to save the ID to the NVRAM
i2c.writeto(0x62, bytes([0x04,0x00])) // trains the next face it sees to (in this case) slot 0