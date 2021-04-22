
numbers=range(1,101)
my_list =[num and ("Fizz"*(not(num%3))+"Buzz"*(not(num%5))or num) for num in numbers]
print(my_list)
