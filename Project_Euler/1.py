# Problem 1: Multiples of 3 and 5:-
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# a=sum(range(3,1000,3))
# b=sum(range(5,1000,5))
# c=sum(range(15,1000,15))
# d=sum(range(3,1000,3))+sum(range(5,1000,5))-sum(range(15,1000,15))
print(sum(range(3,1000,3)) + sum(range(5,1000,5)) - sum(range(15,1000,15)))#Best Solution
# a=(333/2)*(3+999)
# b=(199/2)*(5+995)
# c=(66/2)*(15+990)
# d=a+b-c
# print(d)