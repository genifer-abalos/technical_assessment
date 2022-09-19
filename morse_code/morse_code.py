
MORSE_CODES = {
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z"
}


sample_code = '-..---'

len_code = len(sample_code)

holder = []
holder0 = []
# for i, char in enumerate(sample_code):
#     print(i, char)
#     if i in MORSE_CODES:
#         print('exist')
#     else:
#         holder.append(char)
#         print(holder)
str = ""
possibilities = []
for diff in range(0, len_code+1):
    print(f"diff: {diff}")
    for i in range(len(sample_code)):
        div0 = sample_code[0:i]
        print(div0)
        if div0 in MORSE_CODES:
            holder0.append(MORSE_CODES[div0])
            print(holder0)
        print(str.join(holder0))
        possibilities.append(str.join(holder0))
        div = sample_code[i:i+diff]
        if div in MORSE_CODES:  # by 1
            # print(MORSE_CODES[div])
            holder.append(MORSE_CODES[div])
            # print(holder)
        # print(holder)
        print(str.join(holder))
        possibilities.append(str.join(holder))
    holder.clear()
    holder0.clear()

print(possibilities)


# for i in range(len(sample_code)):
#     div0 = sample_code[0:i+1]
#     div1 = sample_code[i+1:i+2]
#     div2 = sample_code[i+2:i+3]
#     divs = sample_code[i:i+1]
#     if divs in MORSE_CODES:  # by 1
#         # print(MORSE_CODES[div])
#         holder.append(MORSE_CODES[divs])
#         print(str.join(holder))
#     holder.clear()

# for i in range(len(sample_code)):
#     div0 = sample_code[0:i + 2]
#     div1 = sample_code[i + 1:i + 2]
#     div2 = sample_code[i + 2:i + 3]
#     divs = sample_code[i:i + 2]
#     if divs in MORSE_CODES:  # by 2
#         # print(MORSE_CODES[div])
#         holder.append(MORSE_CODES[divs])
#         print(str.join(holder))
#     holder.clear()


print(possibilities)

