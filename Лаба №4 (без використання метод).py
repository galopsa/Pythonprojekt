import random #Імпортуємо модуль random, для генерування чисел в матриці;
N = int(input('Введіть к-сть стовпців матриці: ')) #Вводимо розмірність матриці;
matrix = [[random.randint(0,9) for j in range(N)] for i in range(N)] #Створимо генератор списку;
print('Початкова матриця:') #Вивід;
for i in range(N): #Створимо цикл для виводу матриці;
    print(matrix[i]) #Вивід
print()#Вивід
max=0 #Задамо змінні для накопичення суми;
min=0 #Задамо змінні для накопичення суми;
for i in range(N): #Створимо цикл для запам`ятовування першого рядка матриці;
    min=max=max+matrix[0][i] #Сума першого рядка(дві змінні для подальшого визначення найбільшого та найменшого рядка);
#Задамо початкові значення індексам рядків матриці; 
index1=0  
index2=0 
for i in range(1,N): #Створимо цикл для перебору рядків;
    sum1=0 #Початкова змінна для накопичення суми рядка;
    for j in range(N): #Створимо цикл для додавання елементів рядка;
        sum1=sum1+matrix[i][j] #Додаємо елементи рядка та зберігаємо їх в змінну `sum1`; 
    if sum1>max: #Якщо 'sum1' більша за суму першого рядка то переприсвоємо значення рядка, та продовжуємо цикл;
        max=sum1 #Переприсвоємо значення рядка;
        index1=i  #Переприсвоїмо змінну 'index1';
for i in range(1,N): #Створимо цикл для додавання елементів рядка;
    sum2=0  #Початкова зміння для накопичення суми рядка;
    for j in range(N): #Створимо цикл для накопичення суми рядка;
        sum2=sum2+matrix[i][j] #Додаємо елементи рядка та зберігаємо їх в змінну `sum2`;
    if sum2<min: #Якщо змінна 'sum2' менша за суму першого рядка то переприсвоємо значення рядка, та продовжуємо цикл;
        min=sum2 #Переприсвоємо значення рядка;
        index2=i #Переприсвоїмо змінну 'index2';
matrix[index1],matrix[index2]=matrix[index2],matrix[index1] #Міняємо місцями рядок з найбільшою сумою елементів з рядком з найменшою сумою елементів;
print('Поміняємо місцями',index1+1,'та',index2+1) #Вивід;
print('Виведемо змінену матрицю!') #Вивід;
for i in range(N): #Виведемо змінену матрицю;
    print(matrix[i]) #Вивід.

