# calculadora.py

def sumar(a, b):
	return a + b

def restar(a, b):
	return a - b

def multiplicar(a, b):
	return a * b

def dividir(a, b):
	if b == 0:
		"Error: no es posible dividir entre cero"
	return a / b

def presentacion():
    print("====================================")
    print("  CALCULADORA MODULAR EN PYTHON     ")
    print("====================================")

if __name__ == "__main__":
    presentacion()
