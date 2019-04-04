import threading
from threading import Thread

def func1() :

      for i in range(1000) :
            print ("\nFUNCTION 1")


def func2() :

      for i in range(1000) :
            print ("\nFUNCTION 2")

def func3() :
      for i in range(1000) :
            print ("\nFUNCTION 3")
def func4() :
      for i in range(1000) :
            print ("\nFUNCTION 4")

def func5() :
      for i in range(1000) :
            print ("\nFUNCTION 5")

def ca():

      Thread(target= func1).start()
      Thread(target= func2).start()
      Thread(target= func3).start()
      Thread(target= func4).start()
      Thread(target= func5).start()
      
ca()
      
