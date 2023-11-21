# Carlos Luilquer Almeida Santos (20150465)
# Método de Gauss-Jacobi (Python)
# Referência: AZEVEDO, Anibal. Método de Gauss-Jacobi. 
# Disponível em: <https://youtu.be/t5o2CJzuk1I>

# importa a biblioteca para calcular
import math

# maximo de interação: maxiter = 10
# erro: eps     = 0.05

# função para definir a parada de interações 
def comparar(x,xk,eps):
  soma = 0
  zip_object = zip(x, xk)
  # for para subtrair o x_i+1 - x (módulo)
  for list1_i, list2_i in zip_object:
    soma = soma + math.fabs(list1_i-list2_i)
  # verifica se é menor que 0.05 (erro)
  if (soma < eps):
    return True
  else:
    return False   

# Função Gauss-Jacobi
def gaussJacobi(A,b,maxiter,eps):
  # pega o tamanho de B
  n = len(b)
  # Solução 
  sol = True
  x = b.copy()
  # percorre cada elemento do vetor x que é uma copia de B
  for i in list(range(1,n+1,1)):
    # verifica se a diagonal principal é maior que zero
    if (math.fabs(A[i-1][i-1]) > 0.0):
      # calcula o elemento
      x[i-1] = b[i-1]/A[i-1][i-1]
    else:
      sol = False
      break
  # verifica se não tem divisão por zero 
  if (sol):
    print("Iteração 0")
    print("x = ",x)
    xk = x.copy()
   
    
    # numero de interações
    iter    = 0

    # enquanto o número de Interação for menor que o maximo
    while (iter < maxiter):
      iter = iter + 1

      # para calcular a soma dos elementos
      for i in list(range(1,n+1,1)):
        s = 0
        for j in list(range(1,n+1,1)):
          if ((i-1) != (j-1)):
            s = s + A[i-1][j-1]*x[j-1] 

        # calculo do x_i
        xk[i-1] = (1/A[i-1][i-1])*(b[i-1]-s)
     
    #  exibi os dados na tela
      print("Iteração: ",iter)
      print("xk = ",xk)
      # comparação dos erros 
      if comparar(x,xk,eps):
        x = xk.copy()
        break    
      x = xk.copy()
     
  #  retorna o valor de x
  return x



# Definição da matriz A
A = [[10, -2,  1],
     [ 1, 12,  5],
     [ 1, 5, -10]]

# Vetor B
b = [5, 3, 10]

x = gaussJacobi(A,b,10,0.05)
print("\n\nResultado: ")
print("x = ",x)