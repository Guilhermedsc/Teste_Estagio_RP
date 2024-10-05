def is_fibonacci_number(n):
    fib_seq = [0, 1]
    
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
print(is_fibonacci_number(num))
