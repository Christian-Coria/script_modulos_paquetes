import sys
from calculadora.matematica_avanzada import calculo_esfuerzo

#pasamos argumentos por sysargv
calculo_esfuerzo(int(sys.argv[1]),int(sys.argv[2]))

#debemos pasar argumentos en la consola pasa sys.argv


#numeros
a = input("a: ")
b = input("b: ")

calculo_esfuerzo(int(a),int(b))

