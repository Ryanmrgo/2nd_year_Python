class Fish():
   def swim(self):
      print("The Fish is swimming.")

   def swim_backwards(self):
      print("The Fish can swim backwards, but can sink backwards.")

   def skeleton(self):
      print("The fish's skeleton is made of cartilage.")

class Clownfish():
   def swim(self):
      print("The clownfish is swimming.")

   def swim_backwards(self):
      print("The clownfish can swim backwards.")

   def skeleton(self):
      print("The clownfish's skeleton is made of bone.")

a = Fish()
a.skeleton()
b = Clownfish()
b.skeleton()

