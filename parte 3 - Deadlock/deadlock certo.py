import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread1():
    
    print("Thread 1 tentou aquirir LOCK_A")
    
    with LOCK_A: #aqui ele adquire o lock A primeiro, e depois tenta adquirir o lock B, fazendo com que cada um seja adquirido na mesma ordem, evitando o impasse.
        print("Thread 1 conseguiu adquirir lOCK_A")
        time.sleep(0.05)
        print("Thread 1 tentou adquirir LOCK_B")
        with LOCK_B:
            print("Thread 1 entrou em situação critica")
            time.sleep(1)
    print("Thread 1 concluida")
    
def thread2():
    
    print("Thread 2 tentou aquirir LOCK_A")
    with LOCK_A: #aqui ele adquire o lock A primeiro, e depois tenta adquirir o lock B, fazendo com que cada um seja adquirido na mesma ordem, evitando o impasse.
        print("Thread 2 conseguiu adquirir lOCK_A")
        time.sleep(0.05)
        print("Thread 2 tentando adquirir LOCK_B")
        with LOCK_B:
            print("Thread 2 entrou em situação critica")
            time.sleep(1)
            
    print("Thread 2 concluida")
    
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print("programa finalizado com sucesso")