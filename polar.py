import pylab

k=30
theta=[]
r=[]
for i in range (1,k):
    def Fibonacci(n): 
        if n<0: 
            print("Incorrect input") 
    # First Fibonacci number is 0 
        elif n==1: 
            return 0
    # Second Fibonacci number is 1 
        elif n==2: 
            return 1
        else: 
            return Fibonacci(n-1)+Fibonacci(n-2)

    theta.append(Fibonacci(i))
    r.append(Fibonacci(i))

#theta=range(10000)

#r=range(10000)

print(r)
print(theta)
pylab.polar(theta,r,ls='',marker='o')
pylab.show()


#pylab.plot(range(10), linestyle='', marker='o', color='b')
#pylab.show()
