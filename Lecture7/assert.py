def square(x):
    return x*x

#stampa la potenza di 10
print(square(10))

#stampa true se la potenza di 10 è 100, altrimenti stampa false
print(square(10) == 100)

#Se la potenza di 10 è 100 non stampa nulla, altrimenti da AssertionError
assert square(10) == 100