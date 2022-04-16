""" Situación

Una Universidad colombiana asesorada por la Universidad El Bosque y siguiendo su mismo espíritu de ayuda a las clases menos favorecidas,
ha diseñado un esquema de porcentajes de ayuda (descuento sobre la matrícula) para sus nuevos estudiantes que funciona de la siguiente manera:

• Cada estudiante candidato deberá dar su nombre y apellidos, su edad en años y el número decimal de salarios mínimos mensuales que tiene
de ingreso familiar.
• Presentar un examen de aptitud académica y razonamiento, que será calificado en números enteros de 0 a 100.

• Cálculo del porcentaje de apoyo según los siguientes criterios:

• Si la edad está en el rango 15 a 18 años dar 25%,
de 19 a 21 años dar 15%
y de 22 a 25 años dar 10%,
para mayores de 25 no dar ningún apoyo por edad.

• Si el ingreso familiar es inferior o igual a un salario mínimo dar 30%,
si es mayor a un salario mínimo e inferior o igual a 2 salarios mínimos dar 20%,
si es mayor a dos salarios mínimos e inferior o igual a 3 salarios mínimos dar 10%,
si es mayor a tres salarios mínimos e inferior o igual a 4 salarios mínimos dar 5%,
para ingresos superiores no dar ningún apoyo por ingreso familiar.

• Si su puntaje de ingreso es mayor o igual a 80 y menor de 86 dar 30%,
si es mayor o igual a 86 y menor de 91 dar 35%,
si es mayor o igual a 91 y menor de 96 dar 40%,
y si es mayor o igual a 96 dar 45%.
Para puntajes menores de ochenta, no hay apoyo por puntaje de examen.

• Los apoyos recibidos por edad, por ingreso familiar y por puntaje de examen se deben sumar para dar el porcentaje total de apoyo que
recibirá el beneficiario, es decir, el porcentaje de descuento sobre el valor de la matrícula.

El dueño de la Universidad le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:

• Leer desde el teclado el nombre y apellido del candidato, su edad entera en años, y el número decimal de salarios mínimos
mensuales de su ingreso familiar.
• Calcular el valor total de descuento del candidato según los criterios antes definidos.
• Mostrar en consola el nombre y apellido del beneficiario, el descuento recibido por edad, el el recibido por el ingreso familiar,
el recibido por el puntaje del examen y el descuento total que recibirá sobre el valor de la matrícula.

Autor: Alejandro Meneses Roldan
Fecha: 13/05/2021
"""

nombres = ''
apellidos = ''
nombre_op = ''
edad = int(0)
ing_fam = float(0)
ing_enminimos = float(0)
examen = int(0)
porcentaje_total = float(0)
registro_estudiante = 0
centinela_nota = int(0)
acu_alumnos = int(0)

#Proyecto Matrices
m_total = []                           #la matrices no son necesarias en este ejercicio, no las piden, pero solo quiero
m_nombre = []                          #practicar y aprender mas, experimentar con nuevos conociemientos
m_edad = []
m_ingresos = []
m_examen = []
m_contador = int (0)
contador2 = int (0)
#Fin Proyecto Matrices

#Proyecto de funciones
def porciento_edad(edad):                                                                       #en el ejercicio no dice que se tenga que trabajar basado en funciones
    if edad >= 15 and edad <= 18 :  #Si la edad está en el rango 15 a 18 años dar 25%           #yo nunca las habia trabajado antes, y pues vi la posibilidad de hacerlo en
        porc_edad = 0.25                                                                        #este ejercicio asi que me anime a generar una funcion para calcular cada
    else:                                                                                       #porcentaje y dejar el codigo solo para pedir datos y hacer algunas operaciones
        if  edad >= 19 and edad <= 21 :     #de 19 a 21 años dar 15% y de 22 a 25 años dar 10%, #muy concretas que no vale la pena meter en funciones, el codigo se ve mas limpio
            porc_edad = 0.15                                                                    #y mejor estructurado
        else:
            if  edad >= 22 and edad <= 25 :  # de 22 a 25 años dar 10%
                porc_edad = 0.10
            else:                           #mayores de 25 no dar ningún apoyo por edad
                porc_edad = 0
    return porc_edad

def porciento_salario (ing_fam):
    if  ing_fam <= 1 :           #Si el ingreso familiar es inferior o igual a un salario mínimo dar 30%
        porc_ingresos = 0.30
    else:
        if ing_fam > 1 and ing_fam <= 2 :   # si es mayor a un salario mínimo e inferior o igual a 2 salarios mínimos dar 20%
            porc_ingresos = 0.20
        else:
            if ing_fam > 2 and ing_fam <= 3 :   #si es mayor a dos salarios mínimos e inferior o igual a 3 salarios mínimos dar 10%
                porc_ingresos = 0.10
            else:
                if ing_fam > 3 and ing_fam <= 4 :  #si es mayor a tres salarios mínimos e inferior o igual a 4 salarios mínimos dar 5%
                    porc_ingresos = 0.05
                else:
                    porc_ingresos = 0               #para ingresos mayores no recibe descuento
    return porc_ingresos

def porciento_examen(examen):
    if examen >= 80 and examen < 86:  #Si su puntaje de ingreso es mayor o igual a 80 y menor de 86 dar 30%
        porc_examen = 0.30
    else:
        if examen >= 86 and examen < 91:  #si es mayor o igual a 86 y menor de 91 dar 35%,
            porc_examen = 0.35
        else:
            if examen >= 91 and examen < 96:  # si es mayor o igual a 91 y menor de 96 dar 40%,
                porc_examen = 0.40
            else:
                if examen >= 96 and examen <= 100:      #y si es mayor o igual a 96 dar 45%
                    porc_examen = 0.45
                else:
                    porc_examen = 0                   #para puntuaciones mas bajas no recibe descuento
    return porc_examen
#fin proyecto de funciones

print('')
print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░')
print('   ▒                                                                               ▒')
print('   ▓  ░░▒▒▓▓██  BIENVENIDO AL SISTEMA DESCUENTOS EN MATRICULA EL BOSQUE  ██▓▓▒▒░░  ▓')
print('   █                                                                               █')
print('   ▓                                       ░░▒▒▓▓██   Powered By MINTIC  ██▓▓▒▒░░  ▓')
print('   ▒                                                                               ▒')
print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░')
print('')
nombre_op = input(print('Buen día, por favor digite su nombre: '))    #Pide el nombre de la persona que usara el programa
print('')
registro_estudiante = int(input(print(nombre_op,'bienvenido al sistema, ¿Desea registrar un estudiante? 1 = SI - 2 = NO')))    #pregunta si desea comenzar a registrar estudiantes
print('')
while registro_estudiante == 1:         #mientras le usuario siga presionando 1 en su respuesta seguira registrando estudiantes

    acu_alumnos += 1        #me va a contrar todos los alumnos que fueron registrados, no lo pide el ejercicio pero me parece un dato importante

    nombres = input(print(nombre_op,'Por favor digite los nombres del estudiante: \n'))        #este bloque se encarga de perdir nombre y apellidos por separado
    apellidos =  input(print(nombre_op,'Por favor digite los apellidos del estudiante: \n'))   #estudiante, los concatena y los agrega a la matriz de nombre que usare al final
    m_nombre.append(nombres + ' ' + apellidos)                                          #para mostrar una lista de resultados, no la pide pero quiero practicar

    edad =  int(input(print(nombre_op,'Por favor digite la edad del estudiante: \n')))         #este bloque se encarga de pedir la edad, con el valor llama a la funcion
    porcentaje_edad = float(porciento_edad(edad))                                              #que me asigna el porcentaje por edad, no dice que se haga basado en funciones
    m_edad.append(porcentaje_edad * 100)                                                #pero quiero practicar funciones y el dato se agrega a la matriz de edad

    ing_fam =  float(input(print(nombre_op,'Por favor digite la cantidad de ingresos familiares mensuales que reporta el estudiante en salarios minimos: \n')))
    porcentaje_ingresos = float(porciento_salario(ing_fam))                                    #este bloque hace lo mismo anterior pero con los ingresos familiares
    m_ingresos.append(porcentaje_ingresos * 100)                                         #toma el dato llama a la funcion y agrega el resultado a la matriz de ingresos

    examen = int(input(print(nombre_op,'Por favor digite la puntuación del examen de aptitud académica y razonamiento del estudiante (RANGO DE 0 A 100): \n')))
    while centinela_nota == 0:                                                                                      #este bloque hace lo mismo que los anteriores solo que tiene
        if examen < 0 or examen > 100 :                                                                             #una particularidad tiene un rango cerrado, por lo cual si
            print('───────────────────────────────────────────────────────────────────────────────────────────')    #ingresa por error un numero menor que 0 o mayor que 100 no
            print('   ░░▒▒▓▓██  NOTA NO VALIDA EL RANGO DE LA PUNTUACION DEBE ESTAR ENTRE 0 Y 100  ██▓▓▒▒░░   ')    #deberia poder seguir y pedir nuevamente el numero, use un
            print('───────────────────────────────────────────────────────────────────────────────────────────')    #ciclo While con un IF que me va a controla que la persona hasta
            print('                                                                                           ')    #que no digite un numero en el rango no pueda continuar
            examen = int(input(print(nombre_op,'Por favor digite la puntuación del examen de aptitud académica y razonamiento del estudiante (RANGO DE 0 A 100): \n\n')))
        else:
            centinela_nota = 1                                                      #ya saliendo del ciclo toma el data llama a la funcion y me trae
    centinela_nota = 0                                                              #porcentaje correspondiente y lo agrega a la Matriz de examen
    porcentaje_examen = float(porciento_examen(examen))
    m_examen.append(porcentaje_examen * 100)

    porcentaje_total = float (porcentaje_edad + porcentaje_ingresos + porcentaje_examen)*100     #ya teniendo los 3 descuentos hace la respectiva suma
    m_total.append("{0:.2f}".format(porcentaje_total))                                     #y lo agrega a la matriz de total

    #nueva presentacion

    m_contador = len(m_nombre) - 1
    print('')
    print('╔══════════════════════════════════════════════════════════════════════════════════════════════════')        #esto ya es solo presentacion muestra lo que pide el enunciado
    print('║ El/La estudiante',m_nombre [m_contador], 'recibe los siguientes descuentos en su matrícula:      ')           #nombre, porcentaje de cada categoria y el porcentaje total
    print('╠══════════════════════════════════════════════════════════════════════════════════════════════════')        #el cuadrito y todo eso no lo pide asi pero se ve bonito y
    print('║                                                                                                  ')        #es para practicar
    print('║ Con una edad de',edad,'años, tiene derecho a un descuento de',m_edad [m_contador],'%                ')
    print('║ Con unos ingresos familiares mensuales de',ing_fam,'salarios mínimos, tiene un descuento de',m_ingresos [m_contador],'%')
    print('║ Con una puntuacion de', examen,'puntos en el examen de aptitud, tiene un descuento de',m_examen [m_contador],'%')
    print('║                                                                                                  ')
    print('╠══════════════════════════════════════════════════════════════════════════════════════════════════')
    print('║                                                                                                  ')         #tambien pregunta si vamos a registrar otro estudiante, el
    print('║ EL TOTAL DE DESCUENTOS EN SU MATRICULA ES DE',m_total [m_contador],'%                            ')         #ejercicio nunca dice cuantos alumnos vamos a registrar, pero
    print('║                                                                                                  ')         #no se me hace funcional un programa que se haga para una sola
    print('╚══════════════════════════════════════════════════════════════════════════════════════════════════\n')       #vez y si se quiere repertir tener que ejecurlo otra vez, no dicen
    #fin nueva presentacion                                                                                              #que tenga que ser asi pero se me hace funcional y quiero practicar


    registro_estudiante = int(input(print(nombre_op,' el estudiante ha sido registrado, ¿Desea registrar otro estudiante? SI = 1 - NO = 2 \n')))   #pregunta si queremos registrar mas estudiantes

m_contador = len(m_nombre)
print('Lista terminada\n\n\n\n')
print('══════════════════════════════════════════════════════════════════════════════════════════')
print('            ░░▒▒▓▓██  LISTA DE ALUMNOS CON SU DESCUENTO EN MATRICULA  ██▓▓▒▒░░            ')
print('══════════════════════════════════════════════════════════════════════════════════════════')
while contador2 < m_contador:
       print ('¤ Nombre',m_nombre[contador2])                                            #esta parte no la pide el ejercicio, pero nuevemente todo es para practicar
       print ('¤ Descuento por edad:',m_edad[contador2],'%')                             #y aprender mas, diseñe una lista final con todos los datos de los alumnos
       print ('¤ Descuento por ingresos:',m_ingresos[contador2],'%')                     #registrados, con sus respectivos descuentos en cada categoria y con el total
       print ('¤ Descuento por examen:',m_examen[contador2],'%')                         #sobre la matricula, tambien muestra el numero de todos los alumnos registrados
       print ('¤ Descuento total en matricula',m_total[contador2],'%')                   #pense en poner un contador que me contara los descuentos por persona, por ejemplo
       contador2 = contador2 + 1                                                         #si la persona recibe dos descuentos pues me muestre el 2 o 0 si no recibe ninguo
       print('──────────────────────────────────────────────────────────────────────────────────────────')   #pero ya me dio pereza ademas que me parece poco importante
print('TOTAL DE ALUMNOS REGISTRADOS', acu_alumnos                                                 )
print('══════════════════════════════════════════════════════════════════════════════════════════\n\n')
print('Hasta luego',nombre_op,'\n\n\n')
print('')
print('')                                                                                           #se despide de la persona que ingreso el nombre al principio
print(' Hecho por Alejandro Meneses Roldan ♠                                    ')                  #y la firma final
print(' Proyecto MINTIC 2022 UNIVERSIDAD EL BOSQUE                              ')










