# coding=utf-8
def gauss(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
    x.append(b[i])
    i += 1

  for k in range(n):
    for i in range(k,n):
      if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
      else:
        pass

    for j in range(k+1,n):
      q = M[j][k] / M[k][k]
      for m in range(k, n+1):
        M[j][m] +=  q * M[k][m]

  x = [0 for i in range(n)]

  # print "n = ", n
  # print "x = ", x
  # for row in M:
  #   print row

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
      z = z + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]

  return x

def gauss_seidel(A,b):
  # Gauss Seidel
  A0 = 0
  B0 = 0
  e = float(0.001)

  condition = True
  while condition:
      #fA, fB las funciones donde se calcula cada vez
      A1 = fA(B0)
      B1 = fB(A0)
      e1 = ((abs(A0-A1))/A0)
      e2 = ((abs(B0-B1))/B0)
      x0 = x1
      y0 = y1
      
      condition = e1>e and e2>e

  print('\nSolution: x=%0.3f, y=%0.3f'% (x1,y1))
  return x1, y1



# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix
def seidel(a, x ,b):
    n = len(a)                   
    # calculo x y z
    for j in range(0, n):        
        #var temporal para guardar b[j]
        d = b[j]                  
          
        # calcula xi, yi, zi
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
        # update del valor         
        x[j] = d / a[j][j]
    # devuelve valor updateado          
    return x   