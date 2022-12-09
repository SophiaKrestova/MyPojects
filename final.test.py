ourtask = open("test.txt", "r")
text = ourtask.read().split("\n")
a = int(input("Введіть результат від 1 до 1000 : "))
if a <= 0 or a > 1000 : 
    print("Щось не те.Введіть правильно дані від 1 до 1000")
for x in text:
    y = x.split(" ")
    if(int(y[1]) > a):
        print(x)
