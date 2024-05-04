
import math
import tkinter as tk
ventana_principal = tk.Tk()
ventana_principal.geometry("500x800")
ventana_principal.config(bg="#FF5733")
ventana_principal.title("calculadora")


fuente = ("Helvetica",8)


#---------------------------Funciones-----------------------------------------
ancho = 0
cadena=""
resultado=0
pila = []
def mostrar(numero):
    alto = 3
    global ancho,cadena 
    cadena+=str(numero)
    print(cadena)
    num.config(text=cadena,width=len(cadena))
    
def calcular():
    global cadena,resultado
    
    resultado=evaluar_expresion(cadena)
    num.config(text=resultado)
    cadena=""

def limpiar():
    global cadena,resultado
    cadena=""
    resultado=0
    num.config(text="")



#--------------------------TDA--------------------------------------------------
# Función para verificar si un caracter es un operador
def es_operador(caracter):
    return caracter in ['+', '-', '*', '/','%', '√', '²']

# Función para verificar si un caracter es un paréntesis
def es_parentesis(caracter):
    return caracter in ['(', ')']

# Función para obtener la prioridad de un operador
def prioridad(operador):
    if operador in ['+', '-']:
        return 1
    elif operador in ['*', '/']:
        return 2
    elif operador in ['%', '√', '²']:
        return 3
    else:
        return 0

# Función para evaluar la expresión aritmética utilizando pilas
def evaluar_expresion(expresion):
    pila_operadores = []
    pila_operandos = []
    i = 0
    while i < len(expresion):
        caracter = expresion[i]
        if caracter == ' ':
            i += 1
            continue
        elif caracter.isdigit():
            
            operand = caracter
            while i+1 < len(expresion) and expresion[i+1].isdigit():
                if expresion[i+1] == '²':
                    pila_operadores.append(expresion[i+1])
                    i+=1
                    break
                operand += expresion[i+1]
                i += 1
            pila_operandos.append(int(operand))
        
            
        elif es_operador(caracter):
            while (pila_operadores and prioridad(pila_operadores[-1]) >= prioridad(caracter)):
                
                operador = pila_operadores.pop()
                if operador != '²' or operador == '√':
                    operand2 = pila_operandos.pop()
                    operand1 = pila_operandos.pop()
                else:
                    operand1 = pila_operandos.pop()
                if operador == '+':
                    pila_operandos.append(operand1 + operand2)
                elif operador == '-':
                    pila_operandos.append(operand1 - operand2)
                elif operador == '*':
                    pila_operandos.append(operand1 * operand2)
                elif operador == '/':
                    pila_operandos.append(operand1 / operand2)
                elif operador == '√':
                    pila_operandos.append(math.sqrt(operand1))
                elif operador == '²':
                    pila_operandos.append(operand1 ** 2)
                elif operador == '%':
                    pila_operandos.append(operand1 % operand2)
            pila_operadores.append(caracter)
        
        i+=1
    while pila_operadores:
        operador = pila_operadores.pop()
        if operador != '²' and operador != '√' :
            operand2 = pila_operandos.pop()
            operand1 = pila_operandos.pop()
        else:
            operand1 = pila_operandos.pop()
        if operador == '+':
            pila_operandos.append(operand1 + operand2)
        elif operador == '-':
            pila_operandos.append(operand1 - operand2)
        elif operador == '*':
            pila_operandos.append(operand1 * operand2)
        elif operador == '/':
            pila_operandos.append(operand1 / operand2)
        elif operador == '√':
            pila_operandos.append(math.sqrt(operand1))
            
        elif operador == '²':
           
            pila_operandos.append(operand1 ** 2)
        elif operador == '%':
            pila_operandos.append(operand1 % operand2)
    return pila_operandos[0]



#--------------------------Pantalla----------------------------------------------

pantalla =  tk.Frame(ventana_principal,bg="#FFFFFF")
pantalla.place(x=10,y=180, width=480 , height= 100)

num = tk.Label(pantalla,bg="#FFFFFF", height=3, font=("Arial", 13))  # Etiqueta para mostrar el contador
num.place(x=10,y=10, width=400)

#---------------------------Panel de los numeros y operaciones-------------------
numeros = tk.Frame(ventana_principal,bg="#B5361A")
numeros.place(x=10,y=300, width=485, height=490)


#---------------------------columna 1 de los numeros-----------------------------
numeros_col = tk.Frame(numeros,bg="#B5361A")
numeros_col.place(x=0,y=0, width=120, height=490)

boton1 = tk.Button(numeros_col, height=5, width=17,text="---  C  ---",font=fuente, command = limpiar)
boton1.place(x=8,y=395)

boton1 = tk.Button(numeros_col, height=5, width=17,text="---  1  ---",font=fuente, command = lambda : mostrar(1))
boton1.place(x=8,y=305)

boton4 = tk.Button(numeros_col, height=5, width=17,text="---  4  ---",font=fuente,command = lambda : mostrar(4))
boton4.place(x=8,y=205)

boton7 = tk.Button(numeros_col, height=5, width=17,text="---  7  ---",font=fuente,command = lambda : mostrar(7))
boton7.place(x=8,y=105)

boton_cuadrado = tk.Button(numeros_col, height=5, width=17,text="---  X²  ---",font=fuente,command = lambda : mostrar('²'))
boton_cuadrado.place(x=8,y=10)
#---------------------------columna 2 de los numeros-----------------------------

numeros_col2 = tk.Frame(numeros,bg="#B5361A")
numeros_col2.place(x=120,y=0, width=120, height=490)

boton0 = tk.Button(numeros_col2, height=5, width=17,text="---  0  ---",font=fuente,command = lambda : mostrar(0))
boton0.place(x=8,y=395)

boton2 = tk.Button(numeros_col2, height=5, width=17,text="---  2  ---",font=fuente,command = lambda : mostrar(2))
boton2.place(x=8,y=305)

boton5 = tk.Button(numeros_col2, height=5, width=17,text="---  5  ---",font=fuente,command = lambda : mostrar(5))
boton5.place(x=8,y=205)

boton8 = tk.Button(numeros_col2, height=5, width=17,text="---  8  ---",font=fuente,command = lambda : mostrar(8))
boton8.place(x=8,y=105)

boton_raiz = tk.Button(numeros_col2, height=5, width=17,text="---  √X  ---",font=fuente,command = lambda : mostrar('√'))
boton_raiz.place(x=8,y=10)


#---------------------------columna 3 de los numeros-----------------------------
numeros_col3 = tk.Frame(numeros,bg="#B5361A")
numeros_col3.place(x=240,y=0, width=120, height=490)

boton3 = tk.Button(numeros_col3, height=5, width=17,text="---  3  ---",font=fuente,command = lambda : mostrar(3))
boton3.place(x=8,y=305)

boton6 = tk.Button(numeros_col3, height=5, width=17,text="---  6  ---",font=fuente,command = lambda : mostrar(6))
boton6.place(x=8,y=205)

boton9 = tk.Button(numeros_col3, height=5, width=17,text="---  9  ---",font=fuente,command = lambda : mostrar(9))
boton9.place(x=8,y=105)

boton_modulo = tk.Button(numeros_col3, height=5, width=17,text="---  %  ---",font=fuente,command = lambda : mostrar('%'))
boton_modulo.place(x=8,y=10)

boton_coma = tk.Button(numeros_col3, height=5, width=17,text="---  ,  ---",font=fuente,command = lambda : mostrar(','))
boton_coma.place(x=8,y=395)

#---------------------------columna 4 de los numeros-----------------------------
numeros_col4 = tk.Frame(numeros,bg="#B5361A")
numeros_col4.place(x=360,y=0, width=120, height=490)

boton_mas = tk.Button(numeros_col4, height=5, width=17,text="---  +  ---",font=fuente,command = lambda : mostrar('+'))
boton_mas.place(x=8,y=305)

boton_menos = tk.Button(numeros_col4, height=5, width=17,text="---  -  ---",font=fuente,command = lambda : mostrar('-'))
boton_menos.place(x=8,y=205)

boton_multiplicacion = tk.Button(numeros_col4, height=5, width=17,text="---  *  ---",font=fuente,command = lambda : mostrar('*'))
boton_multiplicacion.place(x=8,y=105)

boton_division = tk.Button(numeros_col4, height=5, width=17,text="---  /  ---",font=fuente,command = lambda : mostrar('/'))
boton_division.place(x=8,y=10)

boton_igual = tk.Button(numeros_col4, height=5, width=17,text="---  =  ---",font=fuente, command =  calcular)
boton_igual.place(x=8,y=395)



ventana_principal.mainloop()