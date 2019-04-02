# Between Two Sets Solution

## [Problem](https://www.hackerrank.com/challenges/between-two-sets/problem?h_r=internal-search)

## [Solution](./between-two-sets.js)

## Explanation
### Essentially this is a problem of reduction. We want to reduce the number of elements we iterate through in order to maximize efficiency.

1. #### Find the LCM of all elements in A: 
This is the rate at which you iterate through the possible shared elements.

2. #### Find the GCD of all elements in B:
This is the max bound of the shared elements loop.

3. #### Loop from LCM of A to GCD of B, iterating by LCM of A each time. 
Check if the GCD of B is divisible by the counter, if so, it is a shared element. 

