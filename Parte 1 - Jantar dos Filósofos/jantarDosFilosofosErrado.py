import threading
import time

N = 5
garfos = [threading.Lock() for _ in range(N)]

def pensar(p):
    print(f"Filósofo {p} está pensando.")
    time.sleep(0.5)

def comer(p):
    print(f"Filósofo {p} está comendo.")
    time.sleep(0.5)

def filosofo(p):
    left = p
    right = (p + 1) % N

    pensar(p)

    print(f"Filósofo {p} está com fome.")

    garfos[left].acquire()
    print(f"Filósofo {p} pegou o garfo {left}.")

    # Aumenta a chance de deadlock
    time.sleep(0.5)

    garfos[right].acquire()
    print(f"Filósofo {p} pegou o garfo {right}.")

    comer(p)

    garfos[right].release()
    garfos[left].release()

    print(f"Filósofo {p} devolveu os garfos.")

threads = []

for i in range(N):
    t = threading.Thread(target=filosofo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()