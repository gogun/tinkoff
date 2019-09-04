import random
class Model():

    data = [] #массив с биграммной языковой моделью 
    
    def fit(self, input):
        string = "" #обработанный текст
        for char in input:
            if ((char != '.') and (char != ',') and (char != '!') and (char != '?') and (char != '-')):
                string += char
        string = string.lower()
        
        string = string.split(' ')
        for i in range(len(string)-3):
            Model.data.append(string[i:i+2])

    def generation(self, n):
        for _ in range(n):
            tmp = random.choice(Model.data)
            print(tmp[0], tmp[1], end = ' ')
            for j in range(len(Model.data)):
                if tmp[1] == Model.data[j][0]:
                    print(Model.data[j][1], end = ' ')
                    break
        print()

g = int(input()) #длина сгенерированной строки (результат будет в 3 раза длиннее желаемого (фича))
f = open('Tolstoy.txt')

lang_model = Model()
lang_model.fit(f.read())
lang_model.generation(g)