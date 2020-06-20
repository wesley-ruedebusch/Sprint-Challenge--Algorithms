#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is time complexity of O(n). The while loop looks like it could be n^3, but since a is updated with a+ n^2, some of that cancels it out.

b) Time complexity of O(n log n). Normally I'd assume nested loops are O(n^2), but since the inner loop increments with j*=2 it is O(log n). Ultimately giving this time complexity of O(n) * O(log n) = O(n log n).

c) This has a runtime complexity of O(n). As n increases, the number of recursion cycles increases linearly.

## Exercise II

# Binary search method approach
1.  Drop an egg from the middle floor of the floors being considered.

2.  Did it break? Yes or no.

3A. If yes, eliminate the upper floors from our consideration and proceed to step 4.

3B. If no, eliminate the lower floors form our consideration and proceed to step 4.

4. Restart the process with step 1 until we reach our answer.

Runtime complexity of this solution is O(log n)
