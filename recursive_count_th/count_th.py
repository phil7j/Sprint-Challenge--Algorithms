'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Idea 1
# pointer = 0
# count = 0


# def count_th(word):
#     global pointer
#     global count
#     if pointer >= len(word)-1:
#         return count
#     if word[pointer] + word[pointer + 1] == "th":

#         count = count + 1
#         pointer = pointer + 2
#     else:

#         pointer = pointer + 1
#     count_th(word)
#     return count


# Idea 2

def count_th(word):
    # word length less then 1 then return
    # check if first two letters are th
    # recursion with word[advance 2 characters because "th" is 2 characters]
    count = 0
    if len(word) == 0:
        return 0
    if word.find("th") != -1:
        loc = word.find("th")
        count = 1
        return count + count_th(word[loc+2:])
    else:
        return 0
