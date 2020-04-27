file = open("text.txt", "r")
text = file.read()

result = 0
i = 0
string_to_find = 'apple'
symbols = ''

for i in range(len(text)):
    symbol = text[i]
    symbols += symbol
    if len(string_to_find) == len(symbols):
        if string_to_find == symbols:
            result += 1
            symbols = ''
            print(result)
        else:
            symbols = ''
print(result)