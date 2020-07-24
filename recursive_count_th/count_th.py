'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    target = "th"
    # check to make sure work is long enough to include the target string
    # also the base case for when our function is done
    if len(word) < len(target):
        return 0
     # check first 2 letters for target string
    # if first 2 aren't the target
    elif word[:2] != target:
        # slice off the first letter
        # and do the recursion dance
        return count_th(word[1:])
        # check first letter see target string
    else:
        return count_th(word[2:]) + 1  