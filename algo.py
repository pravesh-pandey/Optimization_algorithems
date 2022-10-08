from cmath import inf
e=2.718281828459045
def f(x):
	return pow(e,x)-pow(x,3)
def df(x):
	dx=.001
	return (f(x+dx)-f(x-dx))/(2*dx)
def ddf(x):
	dx=.001
	return (f(x + dx) + f(x - dx) - 2 * f(x)) / (dx * dx)

E=.001

def Netwons(x):
	x0 = x
	i=0
	while(abs(df(x0))>E):
		print("Iteration no ",i)
		print("--x = ",x0)
		print("--f'(x) = ",df(x0))
		print("--f''(x) = ",ddf(x0))
		x1 = x0-df(x0)/ddf(x0)
		x0=x1
		i=i+1
	print("-----x",i," = ",x0)
	print("-----f'(x) = ",df(x0))
	print("-----f(x) = ",f(x0))

def Bisection(a,b):
	i=0
	print("--a = ",a)
	print("--b = ",b)
	print("--df(a) =",df(a))
	print("--df(b) =",df(b))
	z=(a+b)/2
	while(abs(b-a)>E and df(a)*df(b)<0):
		print("Iteration no ",i)
		z=(a+b)/2
		print("--z = ",z)
		print("--df(z) =",df(z))
		if(df(a)*df(z)<0):
			b=z
		else:
			a=z
		print("--a = ",a)
		print("--b = ",b)
		i=i+1
	print("--b = ",a)
	print("--f(a) =",f(a))
	print("--f'(b) =",df(a))
	print("--f'(b) =",df(b))

def GoldenSection(a,b):
	i=0
	print("--a = ",a)
	print("--b = ",b)
	while(abs(b-a)>E):
		print("Iteration no ",i)
		x1,x2=b-(b-a)*0.618,a+(b-a)*0.618
		print("a =",a,"b =",b)
		print("x1 =",x1,"x2 =",x2)
		print("f(x1) =",f(x1),"f(x2) =",f(x2))
		if(f(x1)>f(x2)):
			a=x1
		else:
			b=x2
		i=i+1

def Secant(a,b):
	i,x1,x2=0,a,b
	while(abs(df(x1))>E and df(x1)*df(x2)<0):
		print("Iteration no ",i)
		print("--x1 = ",x1)
		print("--f'(x1) = ",df(x1))
		print("--x2 = ",x2)
		print("--f'(x2) = ",df(x2))
		x3 = x2-(df(x2)*(x2-x1))/(df(x2)-df(x1))
		print("x3 = ",x3)
		x1,x2=x2,x3
		i=i+1
	print("-----x",i," = ",x3)
	print("-----f'(x) = ",df(x3))


def Quadratic(x):
	delta,i=1,0
	x1=x
	x2=x+delta
	x3=0
	x_min=inf
	z=0
	f_min = min(f(x1),f(x2),f(x3))
	if(f(x1)>f(x2)):
		x3=x1+2*delta
	else:
		x3=x1-delta
	while ( (abs(x_min-z)>E) or (abs(f_min-f(z))>E)):
		print("iteration no",i)
		x1,x2,x3 = sorted([x1,x2,x3])
		print("x1, x2, x3=",x1,x2,x3)
		a0 = f(x1)
		a1 = (f(x2)-f(x1))/(x2-x1)
		a2 = (((f(x3)-f(x1))/(x3-x1)) - a1)/(x3-x2)
		print("a0=",a0)
		print("a1=",a1)
		print("a2=",a2)
		z=(x1+x2)/2-a1/(2*a2)
		print("z=",z)
		print("f1=",f(x1))
		print("f2=",f(x2))
		print("f3=",f(x3))
		print("fz=",f(z))
		f_min = min(f(x1),f(x2),f(x3))
		if(f(x1)>f(x2)):
			x_min=x2
		else:
			x_min=x1
		if(f(x_min)>f(x3)):
			x_min=x3
		if(f(x1)>f(x2)):
			i=i+1
		x1,x2,x3,z=sorted([x1,x2,x3,z])
		if(f(x2)>f(x3)):
			x1,x2,x3=x2,x3,z
		else:
			x1,x2,x3=x1,x2,x3

	print("Final x=",x_min)
	print("Final f(x)=",f(x_min))


def ExhaustiveSearch(a,b):
	n,j=10,0
	while(abs(b-a)>E):
		print("iteration no",j)
		print("a=",a)
		print("b=",b)
		dx=(b-a)/10
		print("del x=",dx)
		x=[a+i*dx for i in range(0,11)]
		for i in range(1,10):
			if(f(x[i-1])>f(x[i]) and f(x[i+1])>f(x[i])):
				a,b=x[i-1],x[i+1]
				print("x",i-1,"=",x[i-1])
				print("x",i+1,"=",x[i+1])
				print("f(x[i]=",f(x[i]))
				print("f(x[i-1]=",f(x[i-1]))
				print("f(x[i+1]=",f(x[i+1]))
				break
		j=j+1
	print("a=",a)
	print("f(a)=",f(a))

# ExhaustiveSearch(,10)
# Bisection(2,3)
GoldenSection(0,5)
# Netwons(0)
# Secant(2.75,2.875)

# for i in range(0,100):
# 	if(df(i)>0):
# 		print(i)
# 		break