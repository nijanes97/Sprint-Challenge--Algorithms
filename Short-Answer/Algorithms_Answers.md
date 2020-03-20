#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - As n gets bigger the program will run n * n * n times which will reduce down to n
on the inside of the loop the math is n * n which wont take longer as n gets bigger

b) O(log(n)) - As n gets bigger the program will run n * .5n since j is *= 2 which will take it
down from O(n^2)


c) O(n) - As bunnies gets bigger the program will run n times since it's recursive which is basically a loop

## Exercise II

start f at floor 0

drop an egg from that floor and loop through all floors until an egg drops then exit on that floor

the runtime would be O(n) since there is a single loop but if the floor is constant then it would O(1) since we would always take f + 1 number of floors to find the answer
