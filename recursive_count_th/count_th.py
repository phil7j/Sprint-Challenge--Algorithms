'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

pointer = 0
count = 0


def count_th(word):
    global pointer
    global count
    if pointer >= len(word)-1:
        return count
    if word[pointer] + word[pointer + 1] == "th":

        count = count + 1
        pointer = pointer + 2
    else:

        pointer = pointer + 1
    count_th(word)
    return count


print(count_th("THtHThth"))
