
def factorial(n):
	if n is 0:
		return 1
	else:
		return n * factorial(n-1)
		
def sumatorio(m,A):
	if m is 0:
		return 1
	else:
		return (A**m / factorial(m)) + sumatorio(m-1,A)
		
def pn(n,m,A):
	return A**n / (factorial(n) * sumatorio(m,A))

n = int(input("give me n:"))
m = int(input("give me m:"))
A = float(input("give me A:"))

print("p",n," = ",pn(n,m,A))