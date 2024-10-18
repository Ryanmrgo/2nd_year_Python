#Lecture 24 - Example 1

''' Example illustrating higher order function for different types of
series summation - FUNCTION AS A PARAMETER '''

def sumItUp(n, term):
        sum = 0
        ith = 1
        while ith <= n:
            sum = sum + term(ith)
            ith = ith + 1
        return sum

def naturalTerm(x):
        return x

def cubeTerm(x):
        return x * x * x; 

def series1Term(x):
        return 1/x

n = 10
print()

print("Using higher order functions ...")
print("-----------------------------------------")
print(str(sumItUp(n,naturalTerm)))

print("-----------------------------------------")
print(str(sumItUp(n,cubeTerm)))

print("-----------------------------------------")
print(str(sumItUp(n,series1Term)))


