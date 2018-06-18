def reverseWords(str):
    word = ''
    words = []
    for i in range(len(str)):
        if (str[i] != ' '):
            word += str[i]
        elif (word != ''):
            words.append(word)
            word = ''

        if (i == len(str) and word != ''):
            words.append(word)

    answer = ''
    for i in range(len(words) - 1, -1, -1):
        answer += words[i]
        if (i != 0):
            answer += ' '

    return answer


# This wont work because python strings are immutable
def reverse(str):
    i = 0
    j = len(str) - 1
    while (i < j):
        temp = str[i]
        str[i] = str[j]
        str[j] = temp
        i++
        j--


def reverseWordsII(str):
    reversedStr = reverse(str)

    i = 0
    j = 0
    while (j <= len(str)):
        if (reversedStr[j] == ' ' or j == len(str)):
            reverse(len[i:j])
            i = j + 1
        j++



# assert reverseWords('') == ''
print(reverseWords('hi'))
print(reverseWords('   hi   '))
print(reverseWords('the sky is blue'))
print(reverseWords('    the sky is blue'))
print(reverseWords('    the sky is blue     '))
print(reverseWords('the sky is blue     '))
print(reverseWords('the     sky is blue     '))
print(reverseWords('the    ,. sky is blue     '))
