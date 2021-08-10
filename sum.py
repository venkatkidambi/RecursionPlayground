# function
def recursive_sum(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        return input_list[0] + recursive_sum(input_list[1:])

# input formatting and printing
l = [int(i) for i in input("Enter list here: ")]
print(f"The sum of {l} is {recursive_sum(l)}")