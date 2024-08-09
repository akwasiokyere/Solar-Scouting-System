# import all the neessary librarieDigital Converters

from machine import Pin, I2C, ADC # import Pin module to control the pins on the raspberry pi pico w
                                  # import 12C to control the communiction protocol
                                  # import the(Analog to Digital Converter) to control the signals coming to the solar panel


import utime # import time module to control the time in the program
import lcd_api # import module to control the LCD
from pico_i2c_lcd import I2clcd # import module to control the LCD

#Set up 12C for the Lcd screen
#We use pins  GP0 for SDA (data line) and GP1 for SCL (clock line)
i2c = I2C (0, scl=Pin(1), sda=Pin(0),freq=4000000) # The I2c is a communication protcol the helps the raspberry pi to communicate with the LCD

lcd = I2cLcd(i2c, 0x27, 2, 16)# Lcd address

adc = ADC(Pin(26))

vref = 3.3 # The maximum voltage the ADC pin can read
adc_resolution = 65535 # The range of values/different levels the ADC pin can read or output

#list to store the timestamp and voltage data or reading
timestamp = []
voltage = []


#Function to calculate voltage
def calculate_voltage():
    #Get the raw value from the ADC(a number between 0 to 65535)
    raw_value = adc.read_u16()
    
    #Convert the raw value to voltage(a number between 0 to 3.3)
    voltage = (raw_value / adc_resolution) * vref
    return voltage

def append_data_to_file(timestamp_str,voltage):
    try:
        with open("Voltage_data.csv", "a") as data_file: # Open file in append mode
            data_file.write("{}. (:.2f)\n".format(timestamp_str, voltage))
    except: Exception as e:
        print("Error writing to file:" e)
        
def main():
    while true:
        
        with open("voltage_data_file.csv" "w",) as data_file
        data_file.write("Timestamp, voltage \n")
        
        # Read analog voltage(Voltage from the solar panel)
        voltage = calculate_voltage ()
        
        # Clear the LCD screen
        lcd.clear()
        
        # Show the voltage on the LCD screen
        
        lcd.putstr("Voltage:{:2f}V".format(voltage))
        
        timestamp = utime.localtime()
        timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(timestamp[0], timestamp[1],timestamp[2],
                                                                           timestamp[3], timestamp[4], timestamp[5])
        print("Timestamp: (), Voltage: {;2f}V".format(timestamp_str, voltage))
        
        append_data_to_file(timestamp_str, voltage)
        
        #wait for one second before voltage is read
        utime.sleep(1)
        
        lcd = Pin(5, Pin.Out)
        
        # Turn on the Lcd
        lcd.value(1)
        
        utime.sleep(1)
        
        # Turn off LCD
        lcd.value(0)
        
        # Pause for 2 seconds
        utime.sleep(2)
        
# Call the main function of the program
# Code should stop running
try:
    main()
except KeyboardInterrupt:
        print("Data file closed")

try:
    with open("voltage_data.csv")as data_file:
        pass
except OSError:
    with open("voltage_data.csv", "w") as data_file
    data_file_write("Timeastamp, voltage \n")
        