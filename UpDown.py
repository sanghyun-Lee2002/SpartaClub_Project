import random

while 1:  # 다시시작 시, 반복하기 위함.
    random_number = random.randint(1, 100)  # 랜덤 정답
    record = []  # 전적 기록지
    retry = 0

    print("1~100까지 중 정해진 하나의 숫자를 맞춰보세요~")
    while 1:  # 정답을 맞출 때까지 무한히 반복
        print("숫자를 맞춰보세요~")
        try:
            input_value = int(input())  # 정답 입력 코드
            if (random_number == input_value):
                record.append(input_value)  # 입력한 값들을 기록함.
                print("정답입니다~!")
                break
            elif (input_value > 100):
                print("범위를 벗어 났어요!! 이번은 봐줄게요. 다시!!")
            elif (input_value < random_number):
                record.append(input_value)  # 입력한 값들을 기록함.
                print("더 커요! UP!!")
            else: #(input_value > random_number):
                record.append(input_value)  # 입력한 값들을 기록함.
                print("더 작아요... Down!")
        except:
            print("정수만 입력 할 수 있습니다.")   # 입력 란에서 에러 발생 시
            # 동작 과정 중 에러가 날 수 있는 곳이 input 뿐이고
            # input 값을 정수만 되도록 지정 했기 때문

    # EndPage
    # 회차 별 입력한 전적 갈끔하게 보기D
    for i in range(1, 1+len(record)):
        print(i, "회차: ", record[i-1])
    print(f"( 입력 횟수: {i}회 )")

    print(" - 다시 하시겠습니까? ( Y / N ) - ")
    retry = input().upper()

    if retry == "Y":
        print("다시 시작합니다.")
        continue
    else:
        print("게임을 끝마칩니다.")
        break