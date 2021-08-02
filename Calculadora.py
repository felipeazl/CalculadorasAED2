from FuncCalc import soma, multiplicação_karatsuba
import time

# N = 1
inicio = time.time()
print('A soma de 5 + 7 é ',soma([5],[7]))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 5 x 7 é ',multiplicação_karatsuba(5,7))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 2
inicio = time.time()
print('A soma de 23 + 18 é ',soma([2,3],[1,8]))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 23 x 18 é ',multiplicação_karatsuba(23,18))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 3
inicio = time.time()
print('A soma de 325 + 567 é ',soma([3,2,5],[5,6,7]))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 325 x 567 é ',multiplicação_karatsuba(325,567))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 4
inicio = time.time()
print('A soma de 1245 + 4052 é ',soma([1,2,4,5],[4,0,5,2]))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 1245 x 4052 é ',multiplicação_karatsuba(1245,4052))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 5
inicio = time.time()
print('A soma de 50300 + 30050 é ',soma([5,0,3,0,0],[3,0,0,5,0]))
fim = time.time()
print("Tempo de execução:", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 50300 x 30050 é ',multiplicação_karatsuba(50300,30050))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 6
inicio = time.time()
print('A soma de 123456 + 654321 é ',soma([1,2,3,4,5,6],[6,5,4,3,2,1]))
fim = time.time()
print("Tempo de execução:", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 123456 x 654321 é ',multiplicação_karatsuba(123456,654321))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 7
inicio = time.time()
print('A soma de 1020304 + 9080708 é ',soma([1,0,2,0,3,0,4],[9,0,8,0,7,0,8]))
fim = time.time()
print("Tempo de execução:", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 1020304 x 9080708 é ',multiplicação_karatsuba(1020304,9080708))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 8
inicio = time.time()
print('A soma de 40302000 + 15092001 é ',soma([4,0,3,0,2,0,0,0],[1,5,0,9,2,0,0,1]))
fim = time.time()
print("Tempo de execução:", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 40302000 x 15092001 é ',multiplicação_karatsuba(40302000,15092001))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 9 
inicio = time.time()
print('A soma de 123456789 + 987654321 é ',soma([1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]))
fim = time.time()
print("Tempo de execução:", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 123456789 x 987654321 é ',multiplicação_karatsuba(123456789,987654321))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')

# N = 10
inicio = time.time()
print('A soma de 4097774675 + 3096662295 é ',soma([4,0,9,7,7,7,4,6,7,5],[3,0,9,6,6,6,2,2,9,5]))
fim = time.time()
print("Tempo de execução:", fim-inicio, 'milissegundos','\n')
inicio = time.time()
print('A multiplicação de 4097774675 x 3096662295 é ',multiplicação_karatsuba(4097774675,3096662295))
fim = time.time()
print("Tempo de execução: ", fim-inicio, 'milissegundos','\n')