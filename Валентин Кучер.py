# Функція пошуку найбільших елементів
# головної та побічної діагоналі

n = 5 #Розмірність матриці;
def diagonalsMax(mat):	
#Задамо початкові значення елементів діагоналей;
	principalMax = mat[0][0]
	secondaryMax = mat[n - 1][0]
#Створимо цикл для знаходження найбільшого та найменшого елемента матриці;
	for i in range(n):

#Знайдемо найбільший елемент головної діагоналі;
		if (mat[i][i] > principalMax):
			principalMax = mat[i][i]

#Знайдемо найбільший елемент побічної діагоналі;
		if (mat[n - 1 - i][i] > secondaryMax):
			secondaryMax = mat[n - 1 - i][i]
#Якщо найбільший елемент побічної діагоналі
#дорівнює найбільшому елементу головної діагоналі 
#то виведемо найбільший елемент головної діагоналі,
#а якщо ні то виведемо їх добуток.

	if principalMax==secondaryMax:
		print(principalMax)
	else:
		print('Добуток найбільший елементів:',principalMax*secondaryMax)

matrix= [[ 1, 2, 3, 4, -10 ],
		[ 5, 10, 7, 11, 6 ],
		[ 1, 2, 10, 3, 4 ],
		[ 5, 6, 70, 5, 8 ],
		[ 4, 9, 7, 1, -5 ]]
diagonalsMax(matrix)


