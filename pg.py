a, b, c = [float(x) for x in input().strip().split(' ')]

#formulaDeBhaskara: x =(-b + (b**2 - 4ac)**0.5)/2a E x =(-b + (b**2 - 4ac)**0.5)/2a

delta = (b**2) - (4*a*c)

if delta < 0 or a <=0:
	print("Impossivel calcular")
else:
	xP = (-b + (delta)**0.5)/(2*a)
	xN = (-b - (delta)**0.5)/(2*a)
#print("Sem arredondar: ", xP)
print("R1 = %.5f" %xP)
print("R1 = %.5f" %xN)