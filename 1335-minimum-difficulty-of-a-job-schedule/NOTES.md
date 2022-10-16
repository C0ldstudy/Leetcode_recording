This is the first problem I use dynamic programing to solve. The key part is using the all the previous result to calculate the new optimal result.
​
`dp[day][diff]` needs the results of `dp[day-1]`from the first item in difficulty to the current one.