import RPi.GPIO as GPIO
import time
import mail
import lcd

trig1 = 23
echo1 = 24

trig2 = 25
echo2 = 8
buzz = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig1, GPIO.OUT)
GPIO.setup(trig2, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)
GPIO.setup(echo1, GPIO.IN)
GPIO.setup(echo2, GPIO.IN)

count = 0
sp = 0


def main():
    GPIO.output(buzz, GPIO.LOW)
    global count, t1, t2, t, sp
    lcd.main2()
    GPIO.output(trig1, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig1, GPIO.LOW)
    while GPIO.input(echo1) == 0:
        start_time = time.time()
    while GPIO.input(echo1) == 1:
        stop_time = time.time()
    duration = stop_time - start_time
    distance = duration * 17150
    print("Distance1:", distance)
    time.sleep(1)

    GPIO.output(trig2, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig2, GPIO.LOW)
    while GPIO.input(echo2) == 0:
        start_time2 = time.time()
    while GPIO.input(echo2) == 1:
        stop_time2 = time.time()
    duration2 = stop_time2 - start_time2
    distance2 = duration2 * 17150
    print("Distance2:", distance2)
    time.sleep(1)

    if distance < 6.0:
        count = count + 1
        print(count)
        t1 = time.time()
        print(t1)
    if distance2 < 6.0:
        t2 = time.time()
        t = t2 - t1
        print("dutation:", t)
        sp = (50 / t)*(18/5)
        sp = round(sp,2)
        print("Speed(km/hr):",sp)
        time.sleep(1)
        lcd.main("Speed(km/hr):",str(sp))
        time.sleep(2)
        if sp > 55:
            GPIO.output(buzz, GPIO.HIGH)
            mail.main()
            GPIO.output(buzz, GPIO.LOW)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
