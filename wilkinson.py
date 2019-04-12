#programa para calcular la aproximacion de wilkinson

def erlang(mf, A):
	inverse = 1
	for m in range(1, mf + 1):
		inverse = 1 +  ( m / A ) * inverse
	erlang = 1 / inverse
	print("erlang = ", erlang)
	return erlang
		

def wilkinson(mp, A):
	alpha = A * erlang(mp, A)
	wilkinson = alpha * ( 1 - alpha + ( A / ( mp + 1 + alpha - A ) ) )
	print("wilkinson = ", wilkinson)
	return wilkinson

mp = int( input("Give me mp:") )	
A = float( input("Give me A:") )

wilkinson(mp,A)

