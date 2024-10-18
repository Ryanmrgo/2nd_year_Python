
class Duck:  
       def swim(self):  
             print("I'm a duck, and I can swim.")  
       
class Sparrow:  
         def swim(self):  
             print("I'm a sparrow, and I can swim.")  
       
class Crocodile:  
         def swim(self):  
             print("I'm a Crocodile, and I can swim, but not quack.")  
       
def duck_testing(animal):
    animal.swim()

print('calling Duck')       
duck_testing(Duck())
print('calling Sparrow')
duck_testing(Sparrow())
print('callig Crocodile')
duck_testing(Crocodile())  

##Another exampleCredit:https://dev.to/gaurbprajapati/duck-typing-in-python-244n
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
duck = Duck()

print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(duck)) # Output: Quack!
###Another example
class MP3:
    def play(self):
        print("Playing MP3 audio")

class WAV:
    def play(self):
        print("Playing WAV audio")

class FLAC:
    def play(self):
        print("Playing FLAC audio")

def play_audio(audio):
    audio.play()

mp3 = MP3()
wav = WAV()
flac = FLAC()

play_audio(mp3)  # Output: Playing MP3 audio
play_audio(wav)  # Output: Playing WAV audio
play_audio(flac) # Output: Playing FLAC audio


