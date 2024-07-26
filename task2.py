import re

def generator_numbers(text):
    #Iterate all real numbers in "text"
    for number in re.findall(r" \d*\.?\d* ", text):
        #Cast found text numbers to float and yield return
        yield float(number)

def sum_profit(text, func):
    total = 0
    #Iterate through all numbers fund by function "func"
    for number in func(text):
        #Sum all numbers
        total += number

    return total

#Example of usage
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
