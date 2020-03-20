'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    find = 'th'
    # TBC
    if len(word) < 1:
        return 0

    if find in word:
        return 1 + count_th(word.split(find, 1)[1])
    else:
        return 0
    
