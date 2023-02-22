def fun1():
    print("IN F1")
    fun2()
    print("OUT F1")
def fun2():
    print("IN F2")
    fun3()
    print("IN F2")
def fun3():
    print("IN F3")
    try:
        print("HOLA")
        print(3/0)
        print("ADIOS")
    except:
        print("indefinido")
    finally:
        print("OUT F3")
fun1()