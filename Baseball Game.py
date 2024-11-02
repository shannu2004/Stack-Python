def calPoints(operations):
    scores = []
    for operation in operations:
        match operation:
            case '+':
                scores.append(scores[-1] + scores[-2])
            case 'D':
                scores.append(scores[-1] * 2)
            case 'C':
                scores.pop()
            case default:
                scores.append(int(operation))

    return sum(scores)
operations = ["5","2","C","D","+"]
print(calPoints(operations))
