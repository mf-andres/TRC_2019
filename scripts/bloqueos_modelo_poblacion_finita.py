#programa que calcula el bloqueo de llamada de un modelo de colas con poblacion

def engset(N, m_final, alpha):
	inverse = 1
	for m in range( 1, m_final + 1):
		inverse = 1 + ( m / ( alpha * ( N - m ) ) ) *  inverse
	return 1 / inverse	

def call_block(B, alpha):
	return B / ( 1 + ( 1 - B) * alpha )

N = float( input("Give me N: ") )
m = int( input("Give me m: ") )
alpha = float( input("Give me alpha: ") )

B = engset(N, m, alpha)

print("B =  ", B)

BT = engset(N + 1, m, alpha)

print("BT = ", BT)

BA =  call_block(B, alpha)

print("BA = ", BA)
