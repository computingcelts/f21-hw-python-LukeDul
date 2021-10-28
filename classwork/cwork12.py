# In class work
# Date: 10/28/21
import pyttsx3


def my_function(number_1, number_2, say_result='yes'):
    if number_1 % 2 == 0 and number_2 % 2 == 0:  # compound boolean expression
        result = number_1 * number_2
        if say_result == 'yes':
            engine = pyttsx3.init()
            engine.say('result')
            engine.runAndWait()
        return result
    else:
        result = number_1 + number_2
        if say_result == 'yes':
            engine = pyttsx3.init()
            engine.say('result')
            engine.runAndWait()
        return result


print(my_function(1, 3))
print(my_function(4, 8))
print(my_function(1, 3, say_result='yes'))
print(my_function(1, 3, say_result='no'))

