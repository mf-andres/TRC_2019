#programa para calcular la aproximacion de wilkinson

def wilkinson(alpha, mp, A):
	wilkinson = alpha * ( 1 - alpha + ( A / ( mp + 1 + alpha - A ) ) )
	print("wilkinson = ", wilkinson)
	return wilkinson

mp = int( input("Give me mp:") )	
A = float( input("Give me A:") )
alpha = float( input("Give me alpha:") )

wilkinson(alpha,mp,A)

