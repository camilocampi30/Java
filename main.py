from Operaciones import Operaciones


seleccion = ''

while (seleccion != 'salir'):

    seleccion = input('Que deseas hacer? Digita "S" sumar, "R" restar, "M" multiplñicar, "D" Dividir, "salir" para salir: ')

    if(seleccion == 'S' or seleccion == 'R' or seleccion == 'M' or seleccion == 'D'):

        valorA = int(input('Digita el primer valor: '))
        valorB = int(input('Digita el segundo valor: '))
        resultado = Operaciones(valorA, valorB)

        if(seleccion == 'S'):
            print(resultado.calcularSuma())
        if(seleccion == 'R'):
            print(resultado.calcularResta())
        if(seleccion == 'M'):
            print(resultado.calcularmultiplicacion())
        if(seleccion == 'D'):
            print(resultado.calcularDivision())
    else:
        seleccion = 'salir'

print('Hasta pronto!')
quit()
