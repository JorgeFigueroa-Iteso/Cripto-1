mod=int(input("Ingresa el modulo: "))

x=[]
for num in range(1, mod):
  x.append(num)
print("Rango manejado: ",x)
matrix_mult=[[(i*j)%mod for j in range (mod)] for i in range(mod)]
matrix_sum=[[(i+j)%mod for j in range (mod)] for i in range(mod)]

#for fila in matrix:
#  print(fila)

def tables(matrix):
  for x in range(mod):
    for y in range(mod):
#      if matrix[x][y]!=0:
        print(matrix[x][y],end=" ")
#      else:
#        print("",end=" ")
    print()

  print("\nDiagonal: ", end="")
  for z in range(mod):
#    if matrix[z][z]!=0:
      print(matrix[z][z],end=" ")
#    else:
#      print("",end=" ")

print("Tabla de multiplicación modular: " )
tables(matrix_mult)
print("\nTabla de suma modular: " )
tables(matrix_sum)
