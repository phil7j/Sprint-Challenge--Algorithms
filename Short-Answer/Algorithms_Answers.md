#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The running time for this function is logarithmic time, O(log n). Because the input and the and number of operations are not the same.

b) The running time is O(n^2). It works for smaller inputs, but it doesn't scale with larger inputs. It has nested loops both using the input.

c) Runtime is exponential O(c^n). As the input will increase, the runtime will grow at a really fast rate. This is because it has to call itself over and over as it counts down to zero.

## Exercise II

Input is N (Amount of stories in the building)
and f = some number below N

for storie in N:
if storie > f:
Do nothing

if storie < f:
Drop Egg

This has a linear runtime complexity, because it is just iterating through the input, and as the input increases, the space used increases at the same rate.
