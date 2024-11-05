def fibo_ate_limite(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite: 
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

def veriffibo(n, sequencia):
    if n in sequencia:
        print(f"{n} está na sequência de Fibonacci!")
    else:
        print(f"{n} não está na sequência de Fibonacci.")

print("Verifica Sequência Fibonacci")
n = int(input("Digite um número: "))
seq = fibo_ate_limite(n) 
veriffibo(n, seq)
