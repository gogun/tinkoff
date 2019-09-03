import random

def fit(input):
    input = input.split(' ')
    for i in range(len(input)-3):
        data.append(input[i:i+2])

def generation(n):
    for i in range(n):
        
        tmp = random.choice(data)
        print(tmp[0], tmp[1], end = ' ')
        for j in range(len(data)):
            if tmp[1] == data[j][0]:
                print(data[j][1], end = ' ')
                break
    print()

  
g = int(input()) #длинна сгенерированной строки (результат будет в 3 раза больше введенного(фича))

data = []
f = open('Tolstoy.txt')   
fit(f.read())             
generation(g)