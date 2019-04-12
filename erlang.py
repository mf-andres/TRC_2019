#para calcular la funcion de erlang

def erlang(mf, A):
	inverse = 1
	for m in range(1, mf + 1):
		inverse = 1 +  ( m / A ) * inverse
	erlang = 1 / inverse
	print("erlang = ", erlang)
	return erlang
	
mf = int(input("give me m:"))
A = float(input("give me A:"))

erlang(mf,A)