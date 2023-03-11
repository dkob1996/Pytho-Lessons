'''
### Задача 34:  
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

*Ввод:* пара-ра-рам рам-пам-папам па-ра-па-да    
    *Вывод:* Парам пам-пам  
'''
main_set = set()
main_set = {'а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я'}

phrase = input('Enter your phrase: ')
#phrase = 'пара-ра-рам рам-пам-папам па-ра-па-да'

def find_count(words, phr):
    count =0
    for i in phr:
        if i in words:
            count +=1
    return count

def answer(count):
    if count %2 ==0:
        print('Парам пам-пам')
        print('ok')
    else:
        print('Пам парам')
        print('not ok')

        
count_of_words = find_count(main_set,phrase)
answer_of_quest = answer(count_of_words)


'''
Задача 36: 
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

*Ввод:* `print_operation_table(lambda x, y: x * y) ` <br>
*Вывод:*
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        answer =[]
        for j in range(1, num_columns+1):
            answer.append(str(operation(i,j)))
        print(''.join(f'{e:<4}' for e in answer))



print_operation_table(lambda x, y: x * y)