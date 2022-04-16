# Solution to Task 14

def input_taker():
    try:
        sentence = input("Sir, please enter a sentence: ")
        position = int(input("Kindly enter your desired number: "))
        print(function_name(sentence, position))
    except:
        print('============================================')
        print('Invalid Input Please try again')
        input_taker()


def function_name(sentence, position):
    result = sentence[0]
    for i in range(len(sentence)):
        if i % position != 0:
            result += sentence[i]
    return result


if __name__ == '__main__':
    input_taker()
