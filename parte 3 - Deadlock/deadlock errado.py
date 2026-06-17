import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread1(): #aqui ele chama o lock A primeiro e depois o lock B evitando o deadlock, fazendo com que cada um seja adquirido na mesma ordem, evitando o impasse.
    print("Thread 1 tentou adquirir LOCK_A")
    with LOCK_A:
        print("Thread 1 conseguiu adquirir LOCK_A")
        
        time.sleep(0.05)
        
        print("Thread 1 Tentou adquirir LOCK_B")
        with LOCK_B:
            print("Thread 1 Conseguiu adquirir LOCK_B")
def thread2(): #aqui ele adquire o lock B ao inves do lock A, tentando adquirir o lock A depois causando impasse.
    print("Thread 2 Tentou adquirir LOCK_B")
    with LOCK_B:
        print("Thread 2 Conseguiu adquirir LOCK_B")

        time.sleep(0.05)
        
        print("Thread 2 Tentou adquirir LOCK_A")
        with LOCK_A:
            print("Thread 2 Conseguiu adquirir LOCK_A") #devido a ordem acima, ele nunca consegue adquirir o lock A.
            
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Programa finalizado")     