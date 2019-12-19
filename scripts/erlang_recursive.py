
def erlang_inverse(m,A):
	if(m == 0):
		return 1
	else: 
		return 1 +  ( m / A ) * erlang_inverse(m-1,A)
		
def erlang(m,A):
	return 1 / erlang_inverse(m,A)
	
m = float( input("give me m:"))
A = float( input("give me A:"))

erlang = erlang(m,A)
print("erlang = ", erlang)
