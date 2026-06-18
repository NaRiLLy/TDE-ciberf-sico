import threading
import time

contador = 0

# num_threads define quantas threads serão criadas
# repeticoes define quantas vezes cada thread incrementa o contador
num_threads = 8
repeticoes = 200_000

# Semáforo binário: garante que apenas uma thread acessa o contador por vez
semaforo = threading.Semaphore(1)


def incrementar():
    global contador

    for _ in range(repeticoes):
        # O bloco 'with' adquire o semáforo automaticamente e o libera ao sair
        with semaforo:
            contador += 1


tempo_inicio = time.perf_counter()

# Cria, registra e inicia todas as threads de uma vez
lista_threads = [threading.Thread(target=incrementar) for _ in range(num_threads)]

for th in lista_threads:
    th.start()

# Aguarda a conclusão de todas as threads antes de prosseguir
for th in lista_threads:
    th.join()

tempo_fim = time.perf_counter()

total_esperado = num_threads * repeticoes
print(f"Valor esperado:  {total_esperado}")
print(f"Valor obtido:    {contador}")
print(f"Tempo de execução: {tempo_fim - tempo_inicio:.4f}s")
