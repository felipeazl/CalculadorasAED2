def soma(valor1, valor2):
    vai_um = 0
    total = 0
    tamanho1 = len(valor1)
    tamanho2 = len(valor2)
    tamanho_total = max(tamanho1, tamanho2)
    
    resultado = [0] + [0] * tamanho_total 

    for i in range(1, tamanho_total + 1):
        
        if tamanho1 - i >= 0:
            a = valor1[tamanho1 - i] 
        if tamanho2 - i >= 0:
            b = valor2[tamanho2 - i] 
        
        total = a + b + vai_um
        resultado[tamanho_total - i + 1] = total % 10
        vai_um = total // 10

    if vai_um > 0: 
        resultado[0] = vai_um
    
    return "".join(map(str, resultado)) if resultado[0] != 0 else "".join(map(str,resultado[1:]))

def multiplicação_karatsuba(valor1, valor2):
	if len(str(valor1)) == 1 or len(str(valor2)) == 1:
		return valor1*valor2
	else:
		n = max(len(str(valor1)),len(str(valor2)))
		aux = int(n / 2)
		
		a = int(valor1 / 10**(aux))
		b = valor1 % 10**(aux)
		c = int(valor2 / 10**(aux))
		d = valor2 % 10**(aux)
		
		ac = multiplicação_karatsuba(a,c)
		bd = multiplicação_karatsuba(b,d)
		adbc = multiplicação_karatsuba(a+b,c+d) - ac - bd

		produto = ac * 10**(2*aux) + (adbc * 10**aux) + bd

		return produto