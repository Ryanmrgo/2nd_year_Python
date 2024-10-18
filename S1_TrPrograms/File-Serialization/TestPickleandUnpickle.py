# import required python modules

import pickle

import uuid

 

# Trivial definition of a car

class Car:

    manufacturer    = ""

    modelName       = ""

   

    def __init__(self, manufacturer, modelName):

        self.manufacturer    = manufacturer

        self.modelName       = modelName

       

    def identify(self):

        print("Manufacturer: %s"%(self.manufacturer))

        print("Model Name: %s"%(self.modelName))

 

# Trivial definition of a ServiceRecord

class ServiceRecord:

    id              = -1

    milesReading    = -1

    serviceCount    = -1

   

    def __init__(self, id, milesReading, serviceCount):

        self.id              = uuid.uuid4()

        self.milesReading    = milesReading

        self.serviceCount    = serviceCount

       

    def identify(self):

        print("Service Id: %s"%(self.id))

        print("Miles: %s"%(self.milesReading))

        print("Service Count: %s"%(self.serviceCount))

 

# Get car and service instances   

print("Creating objects")

 

car = Car("Toyota",  "Corolla")

s1  = ServiceRecord(1, 5000, 1)

s2  = ServiceRecord(2, 15000, 2)

 

# Print object information

car.identify()

s1.identify()

s2.identify()

 

# Create a file for storing objects 

objectRep = open("ServiceInfo.picl", "wb")

 

print("Pickling...")

# Pickle the objects

pickle.dump(car, objectRep, protocol=pickle.HIGHEST_PROTOCOL)

pickle.dump(s1,  objectRep, protocol=pickle.HIGHEST_PROTOCOL)

pickle.dump(s2,  objectRep, protocol=pickle.HIGHEST_PROTOCOL)

 

# Close the file

objectRep.close()

print("Pickling complete")

print("-------------------")

 

# Open the file in read mode

objectRep = open("ServiceInfo.picl", "rb")

 

print("Unpickling...")

# Unpickle the objects

object1 = pickle.load(objectRep)

object1.identify()

 

object2 = pickle.load(objectRep)

object2.identify()

 

object3 = pickle.load(objectRep)

object3.identify()

print("Unpickling complete")

 

objectRep.close()

 

