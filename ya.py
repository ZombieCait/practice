"""
Дана строка AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE, ее нужно преобразовать в 6A1F2D7C1A17E (RLE)
"""
def squeeze_str(s):
    result = ''
    
    if s != '':
        symbol = s[0]
        index = 0

        for i in range(len(s)):
            if s[i] != symbol:
                result = result + symbol + str(i-index)
                index = i
                symbol = s[i]

        result = result + s[i] + str(len(s)- index)
            
    return result
        
print(squeeze_str('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'))
print(squeeze_str('AAAAAA'))
print(squeeze_str('AAAAAAF'))
print(squeeze_str('AF'))
print(squeeze_str(''))




"""
Посетитель кинотеатра заходит в зал и выбирает себе место, при этом он хочет сесть как можно дальше от соседей. В ряду есть как минимум 1 сосед. Найти место с максимальным расстоянием до ближайшего соседа. На вход подается список [1, 0, 0, 0, 1, 1, 0, 1], 1 - занятые места, 0 - свободные
"""

def get_introvert_seat(seats):
    prev = None
    res = -1

    for i in range(len(seats)):
        if seats[i] == 1:
            if prev == None:
                res = i
            else:
                res = max(res, (i-prev) // 2)
            prev = i
    res = max(res, len(seats)-1-prev)
    return res



print(get_introvert_seat([1, 0, 0, 0, 1, 1, 0, 1]))
print(get_introvert_seat([0, 0, 0, 1, 1, 0, 1]))
print(get_introvert_seat([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0])) 
print(get_introvert_seat([1, 0, 1, 1, 1, 1, 0, 1]))