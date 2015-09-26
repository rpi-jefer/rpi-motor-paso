import RPi.GPIO as GPIO
import time
 
# variables
delay = 85
steps = 4

# Pines de Salida 
salida_a = 12
salida_b = 16
salida_c = 18
salida_d = 22

# Setup Pines de Salida  
GPIO.setup(salida_a, GPIO.OUT)
GPIO.setup(salida_b, GPIO.OUT)
GPIO.setup(salida_c, GPIO.OUT)
GPIO.setup(salida_d, GPIO.OUT)
 
# Funcion adelante()
def adelante(delay, steps):  
  for i in range(0, steps):
    setPaso(1, 0, 0, 0)
    time.sleep(delay)
    setPaso(0, 1, 0, 0)
    time.sleep(delay)
    setPaso(0, 0, 1, 0)
    time.sleep(delay)
    setPaso(0, 0, 0, 1)
    time.sleep(delay)

# Funcion setPaso() 
def setPaso(a1, a2, a3, a4):
  GPIO.output(salida_a, a1)
  GPIO.output(salida_b, a2)
  GPIO.output(salida_c, a3)
  GPIO.output(salida_d, a4)

count = 0
while (count < 1):
  adelante(int(delay) / 1000.0, int(steps))
  print 'Cuenta: ', count
  count = count + 1

setPaso(0, 0, 0, 0)
