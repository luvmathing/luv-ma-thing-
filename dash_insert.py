def dash_insert(number):
    answer = ""
    for i in range(len(number)):
        if i > 0:
            if int(number[i-1]) % 2 == 0 and int(number[i]) % 2 == 0:
                answer += "*"
            if int(number[i-1]) % 2 == 1 and int(number[i]) % 2 == 1:
                answer += "-"
        answer += number[i]
    print(answer)

dash_insert("4546793")