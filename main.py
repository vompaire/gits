#КРЕСТЫ НУЛИ
#Если в 00 вводится крест или нуль то вывести всю хуиту
#если в 00 есть крест или нуль то послать нахуй и продолжить игру
#если после этого хода есть три подряд одиннаковых символа(диаганаль, столбец или строка) то написать победа символа
#если ввелся крест то след ходит нуль
#если это прошел 9 ход писать ничья
def simbol(k):
    if k%2==0:
        return perviy_simbol
    else:
        return vtoroy_simbol
def pole(s):
    print(" ", "0", "1", "2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(s[i][j], end=" ")
        print()
print("Сначала страка потом столбец, без запятой, пример 00 или 12")
t=0 # колво ходов


perviy_simbol=input("кто ходит первым, введите Х или О")
if perviy_simbol.lower() in ["x","х"]:
    vtoroy_simbol="o"
elif perviy_simbol.lower() in ["o","о"]:
    vtoroy_simbol="x"
else:
    print("Сложно ввести то что просят, увалень?")
    exit()

print("Первый игрок играет за",perviy_simbol, ". Второй игрок играет за",vtoroy_simbol)
s = [["-" for j in range(3)] for i in range(3)] # Создаем пустую тройную матрцу
pole(s)
k=0

while k!=9:
    t=input("куда ходить?")
    t=list(t)
    if (t[0] not in ["0","1","2"]) or (t[1] not in ["0","1","2"]):
        print("Ну и пидр же ты, пробуй еще")
        continue
    t1=int(t[0])
    t2=int(t[1])
    if s[t1][t2] == "-" and ((s[t1][t2]) != perviy_simbol or s[t1][t2] != vtoroy_simbol):
        s[t1][t2] = simbol(k)
        k += 1
        pole(s)
    else:
        print("Ебанько хули ходишь где уже походили, перехаживай")
        continue
    if s[0][0]==s[0][1]==s[0][2]!="-": #страка 1
        break
    if s[1][0]==s[1][1]==s[1][2]!="-": #страка 2
        break
    if s[2][0]==s[2][1]==s[2][2]!="-": #страка 3
        break
    if s[0][0]==s[1][0]==s[2][0]!="-": #столбик 1
        break
    if s[0][1]==s[1][1]==s[2][1]!="-": #столбик 2
        break
    if s[0][2]==s[1][2]==s[2][2]!="-": #столбик 3
        break
    if s[2][0]==s[1][1]==s[0][2]!="-": #диаганаль 1
        break
    if s[0][0]==s[1][1]==s[2][2]!="-": #диаганаль 2
        break

if k==9:
    print("НИЧЬЯ")
else:
    print(simbol(k-1), "ПОБЕДИЛ")