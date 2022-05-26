import sensor
import lcd
import time

lcd.main("Speed","Measurement")
time.sleep(2)
lcd.main2()

while True:
    sensor.main()
    
