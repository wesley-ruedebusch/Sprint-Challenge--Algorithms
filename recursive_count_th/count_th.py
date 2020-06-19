'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # "case matters"
    target = "th"
    
    # check to make sure work is long enough to include the target string
    # also the base case for when our function is done
    if len(word) < len(target):
        return 0