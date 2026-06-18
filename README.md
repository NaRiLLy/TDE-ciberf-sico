# TDE-ciberf-sico
Grupo 5
Feito por: Juliana Stonaga, Pierre Savelli e Matheus Fuchs

Línguagem utilizada: Python 3.13

Como executar: 
  instalar python 3.13;
  Abrir o terminal na pasta do projeto;
  Executar python nome do projeto.py


parte 1 - jantar dos filósofos:
  sem a sincronização adequada no código, todos os filósofos podem pegar o garfo esquerdo simultaneamente, resultando neles ficarem esperando para sempre o garfo direito.

Resultado:
  Versão Sincronizada:
    <img width="292" height="595" alt="image" src="https://github.com/user-attachments/assets/6d4d8ec5-0c20-4d43-baa9-972f438fe6aa" />

  Versão dessincronizada:
    <img width="242" height="264" alt="image" src="https://github.com/user-attachments/assets/af406268-42b1-49d9-93d0-5e86e86fa115" />

parte 2 - Semaforo:
  Na parte onde não possui sincronização e possui erros de indentação fora do "for" iniciando apenas a última thread, enquanto na parte em que possui sincronização não possui esse erro de indentação e garantindo que apenas uma thread seja executada por vez

Resultado:
  Versão sincronizada:
    <img width="194" height="50" alt="image" src="https://github.com/user-attachments/assets/66a0c0e0-2b84-4419-86d5-e73cec44a816" />

versão dessincronizada:
  <img width="242" height="48" alt="image" src="https://github.com/user-attachments/assets/06db7d15-9f32-4c6d-996b-150b05f1ab7a" />


Parte 3 - Deadlock:
  Foi adicionado o LOCK_A e LOCK_B para poder ser váriaveis acessiveis nas threads1 e threads2, além de ser incrementado mensagens para podermos identificar o que estava acontecendo no código e sabermos o resultado final.

Resultado:

Versão corrigida:
  <img width="257" height="191" alt="image" src="https://github.com/user-attachments/assets/04fd49f2-8a38-4046-b9d5-2142f37521a5" />

Versão que trava:
  <img width="259" height="125" alt="image" src="https://github.com/user-attachments/assets/34ee7c92-57e0-4ecf-877b-bab1b524c83b" />


Link do vídeo: https://youtu.be/2TCN1iGad1w
