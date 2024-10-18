def fun1():
    print("This is module test!")
    print(__name__)

if __name__ == "__main__":
    print("I am call from inside example.py")
    fun1()
