n=int(raw_input())
a = 0
temp = n
while temp > 0:
	b = temp % 10
	a += b ** 3
	temp //= 10
if n == a:
	print "yes"
else:
	print "no"
