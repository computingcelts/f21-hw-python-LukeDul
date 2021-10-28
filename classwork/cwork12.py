# In class work
# Date: 10/28/21
import pyttsx3


def my_function(number_1, number_2, number_type='even'):
    if number_1 % 2 == 0 and number_2 % 2 == 0:  # compound boolean expression
        print('even')
        return number_1 * number_2
    elif number_1 % 2 == 1 and number_2 % 2 == 1:  # compound boolean expression
        print('odd')
        return number_1 + number_2


engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()


print(my_function(2, 2))
print(my_function(1, 1))

