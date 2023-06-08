import serial

# Create a serial connection
ser = serial.Serial(
    port='COM8',  # Replace with your serial port
    baudrate=9600,  # Set the baud rate of your RS485 module
    parity=serial.PARITY_NONE,  # Set parity as required
    stopbits=serial.STOPBITS_ONE,  # Set stop bits as required
    bytesize=serial.EIGHTBITS  # Set data bits as required
)

# Open the serial connection
ser.open()
