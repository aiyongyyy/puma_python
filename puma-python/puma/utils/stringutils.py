
def formatString(text):
    if text:
        text = text.replace("\u200c", "")
        return ToDBC(text).lower().strip()
    else:
        return text


def ToDBC(input):

    for i in range(len(input)):
        if input[i] == 12288:
            input[i] = ' '
        elif input[i] > '\uff00' and input[i] < '｟':
            input[i] -= 'ﻠ'

    return input
