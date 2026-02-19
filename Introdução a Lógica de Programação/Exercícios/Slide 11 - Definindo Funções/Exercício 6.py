n = int(input())

if n < 1:
    print('0')
else:
    a = 1
    soma1 = n + 1
    div1 = n/2
    def somatotal(a):
        return soma1 * div1
    
    print(somatotal(a))
