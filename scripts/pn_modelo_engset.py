def factorial(n):
	if n is 0:
		return 1
	else:
		return n * factorial(n-1)
		
def binomial_coeficient(n,x):
	return factorial(n) / (factorial(x) * factorial(n - x))
		
def sumatorio(N,m,alpha):
	if m is 0:
		return 1
	else:
		return (binomial_coeficient(N,m) * alpha**m) + sumatorio(N,m-1,alpha)
		
def pn(n,N,m,alpha):
	return (binomial_coeficient(N,n) * alpha**n) / (sumatorio(N,m,alpha))

n = int(input("give me n:"))
N = int(input("give me N:"))
m = int(input("give me m:"))
alpha = float(input("give me alpha:"))

print("p",n," = ",pn(n,N,m,alpha))