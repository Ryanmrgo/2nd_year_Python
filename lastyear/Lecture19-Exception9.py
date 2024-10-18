#Example illustrating assertion in Python

def toFahrenheit(temperature):
        assert (temperature >= 0),"Colder than absolute zero!"
        return ((temperature-273)*1.8)+32

#print(toFahrenheit(373))
#print(int(toFahrenheit(505.78)))
print(toFahrenheit(-5))
