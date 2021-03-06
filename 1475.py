'''
백준 알고리즘 1475 문제 풀이
작성자 ESENS
작성일 180409

한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최소값을 출력하시오.
(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

입력:
9999
------------------------------------------------------------------------------------
출력:
2
'''

#각 배열의 인덱스값의 max값을 출력해주면 최대 몇세트가 필요한지 알 수 있음

def count(var):
    value = str(var)
    data = [0] * 10
    for i in value:
        #print(i)
        data[int(i)] += 1
    #6과 9는 뒤집어서 쓸 수 있으므로 하나의 인덱스로 본다
    data[9] += data[6]
    data[6] = 0
    #짝수로 나뉘어지면 그냥 나누면 되고 아닐경우 +1 해줘야 한다
    if data[9] % 2 == 0:
        data[9] = int(data[9] / 2)
    else:
        data[9] = int(data[9] / 2) + 1
    print(max(data))
    return 0

count(input())