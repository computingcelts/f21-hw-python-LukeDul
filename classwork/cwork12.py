# In class work
# Date: 10/28/21
import pyttsx3


def my_function(number_1, number_2, numbers_type='even'):
    if number_1 % 2 == 0 and number_2 % 2 == 0:  # compound boolean expression
        return number_1 * number_2
    else:
        return number_1 + number_2


engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()


print(my_function(1, 3))
print(my_function(4, 8))
print(my_function(1, 3, numbers_type='even'))
print(my_function(1, 3, numbers_type='odd'))

