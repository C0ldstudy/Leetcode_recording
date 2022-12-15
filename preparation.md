## Interview Preparation



### Mistakes
In the part, I would like to summarize the mistakes I commit during coding.


#### 1. The correct way to build a new array in python
`dp = [[None for x in range(length1)] for y in range(length2)]`
This is wrong: `dp = [[None]* length1 ]* length2` since the second element in the array used the same address which means the values of them are exactly the same.




