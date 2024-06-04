#valores de entrada
x1 = 1 #é longe?
x2 = 0 #é caro?
x3 = 1 #é amigos?

#resultado real
y = 1 #ele foi = 1 / ele não foi = 0

#pesos
w1 = 0
w2 = 0
w3 = 0.1
w0 = 0.1

#função do F(z)
z = w1 * x1 + w2 * x2 + w3 * x3 + w0
print(z)

#função do ϕ(z)
func_sn = 0
if z > 0:
    func_sn = 1
elif z <= 0:
    func_sn = 0

if func_sn == 0:
    print("Não vai")
elif func_sn == 1:
    print("Vai")
