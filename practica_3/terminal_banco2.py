from collections import deque

def enqueue(q: deque, elemento) -> None:
    q.append(elemento)

def dequeue(q: deque):
    return q.popleft()

def peek(q:deque):
    return q[0]

def is_empty(q: deque) -> bool:
    return not q

def size(q: deque) ->int:
    return len(q)

def aplicar_retiro(saldos: deque[int], monto: int, historial):
    saldo_original = dequeue(saldos)
    if historial is not None:
        enqueue(historial, saldo_original)
    nuevo_saldo = saldo_original - monto
    enqueue(saldos, nuevo_saldo)


def aplicar_deposito(saldos: deque[int], monto: int, historial):
    saldo_original = dequeue(saldos)
    if historial is not None:
        enqueue(historial, saldo_original)
    nuevo_saldo = saldo_original + monto
    enqueue(saldos, nuevo_saldo)

saldos = deque()
historial_saldos = deque()

for i in range(5):
    enqueue(saldos, 1000)

monto_retiro = 500

for i in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_saldos)

monto_deposito = 300
for i in range(5):
    aplicar_deposito(saldos, monto_deposito, historial_saldos)

print("Saldos actuales:", list(saldos))
print("Historial de saldos:", list(historial_saldos))