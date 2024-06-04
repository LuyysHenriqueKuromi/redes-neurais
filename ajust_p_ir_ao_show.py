#learning rate(taxa de aprendizado)
h = 0.1
#resultado entregue pela rede
func_sn = 0
#resultado real
y = 1

#valores de entrada
x1 = 0
x2 = 0
x3 = 1
x0 = 1 #o x do bias(w0) sempre será 1

#pesos
w1 = -0.1
w2 = -0.1
w3 = 0.1
w0 = 0.1

dw1 = h * (y - func_sn) * x1
w1 = w1 + dw1
print(f"w1: {w1}")

dw2 = h * (y - func_sn) * x2
w2 = w2 + dw2
print(f"w2: {w2}")

dw3 = h * (y - func_sn) * x3
w3 = w3 + dw3
print(f"w3: {w3}")

dw0 = h * (y - func_sn) * x0
w0 = w0 + dw0
print(f"w0: {w0}")