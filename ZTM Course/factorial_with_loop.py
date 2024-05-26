def factorial_loop(num):
    answer = 1
    if num == 2:
       answer = 2
    else:   
        for i in range(2,num+1):
            answer = answer * i
    return answer
