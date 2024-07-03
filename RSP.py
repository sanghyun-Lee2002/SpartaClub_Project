import random

record = [] #게임 전적 공간
win = []
lose = []
draw = []

while 1:    # 무한반복
    random_answer = random.choice(['가위','바위','보']) #컴퓨터 선택
    print("가위! 바위! 보!")
    HumanInput = input() 
    # 오타 방지 및 수정 편의용
    a = "Win!"
    b = "Lose..."
    c = "Draw!"
    if HumanInput == "가위": #player 가위
        if random_answer == "가위": #pc 가위
            draw.append("가위 vs 가위")
            print(c)
        elif random_answer == "바위": #pc 바위
            draw.append("바위 vs 가위")
            print(b)
        elif random_answer == "보": #pc 보
            draw.append("보 vs 가위")
            print(a)
    elif HumanInput == "바위": #player 바위
        if random_answer == "가위": #pc 가위
            draw.append("가위 vs 바위")
            print(a)
        elif random_answer == "바위": #pc 바위
            draw.append("바위 vs 바위")
            print(c)
        elif random_answer == "보": #pc 보
            draw.append("보 vs 바위")
            print(b)
    elif HumanInput == "보": #player 보
        if random_answer == "가위": #pc 가위
            draw.append("가위 vs 보")
            print(b)
        elif random_answer == "바위": #pc 바위
            draw.append("바위 vs 보")
            print(a)
        elif random_answer == "보": #pc 보
            draw.append("보 vs 보")
            print(c)
    else:
        print("가위, 바위, 보 중에서 골라주세요\n")
        continue

    print(" - 다시 하시겠습니까? ( Y / N ) - ")
    retry = input().upper() #player 재시작 답변. // 대문자로만 입력됨.
    if retry == "Y":
        print("게임을 재시작합니다.\n")
        continue
    else:
        print(" - 게임을 끝마쳤습니다. - \n")
        print("승리 전적\n",win,"\n패배 전적\n",lose, "\n무승부 전적\n",draw)
        print(f" {len(win)}회 / {len(lose)}회 / {len(draw)}회 \n")
        break