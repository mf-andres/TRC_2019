#python programm that calculates the inverse of the engset function

N = float( input("Give me N: ") )
m_final = int( input("Give me m: ") )
alpha = float( input("Give me alpha: ") )
previous_inverse = 1

for m in range( 1, m_final + 1):
	inverse = 1 + ( m / ( alpha * ( N - m ) ) ) *  previous_inverse
	print("inverse = ", inverse)
	previous_inverse = inverse

engset = 1 / inverse	
print("engset = ", engset)