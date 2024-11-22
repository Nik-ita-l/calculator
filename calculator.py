words_to_numbers = { #создал словарь для преобразования слова в цифру 
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
}
operations = ['плюс','минус','умножить'] #задал список операций которые мы можем использовать 
print('Привет. напиши свой пример!')
s = input()

list_of_words = s.split() #делим введенную строку на слова 
# преобразуем слова и ищем индекс операции 
for i,v in enumerate(list_of_words):
    if v in operations:
        operation_index = i
#выполняем операцию взависимости от найденного слова 
if list_of_words[operation_index] == 'плюс':
    result = words_to_numbers[list_of_words[:operation_index][0]] + words_to_numbers[list_of_words[operation_index+1 :][0]]

if list_of_words[operation_index] == 'минус':
    result = words_to_numbers[list_of_words[:operation_index][0]] - words_to_numbers[list_of_words[operation_index+1 :][0]]
    
if list_of_words[operation_index] == 'умножить':
    result = words_to_numbers[list_of_words[:operation_index][0]] * words_to_numbers[list_of_words[operation_index+1 :][0]]
# преобразование чисел в буквы 


def number_to_words(num):
    if num == 0:
        return "ноль"

    words = []
    if num >= 100:
        words.append("сто")
        num -= 100

    if 10 <= num < 20:
        tens = ["", "", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
                "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
        words.append(tens[num - 10])
        num = 0
    else:
        if num >= 20:
            tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", 
                    "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
            words.append(tens[num // 10])
            num %= 10

        if num > 0:
            units = ["", "один", "два", "три", "четыре", "пять", 
                     "шесть", "семь", "восемь", "девять"]
            words.append(units[num])

    return ' '.join(words).strip()

result_in_words = number_to_words(result) #делаем результат в слова 
print(result_in_words) 
