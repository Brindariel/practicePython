import array

my_array = array.array('i',[1,2,3,4,5,6,7,8,9,10])

even_number = [num for num in my_array if num% 2 ==0]

sum_of_evens = sum(even_number)

if len(even_number) > 0:
    average_of_evens = sum_of_evens / len(even_number)
else:
    average_of_evens = 0

print("Even numbers:", even_number)
print("Sum of even numbers:", sum_of_evens)
print("Average of even numbers:", average_of_evens)
