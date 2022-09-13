# 몇 자리 숫자로 할건지 입력을 받는다. 3을 입력할 경우 해당 숫자야구 게임은 3자릿수로 진행 최대 10자리
# 첫 번째 입력을 받은 자릿수 만큼 파이썬으로 중복 없는 랜덤 수 생성
# 사용자가 숫자를 입력했을 때 숫자 야구 게임의 규칙에 맞게 ball/out count를 출력
# 사용자가 정답을 맞춘 경우 아래 항목들을 출력
#   사용자가 정답을 맞추기까지 입력한 횟수
#   사용자가 게임을 시작해서 정답을 맞추기까지 소요된 시간
#   정답을 맞춘 시점의 날짜/시간
#   게임을 진행중 exit을 입력할 경우 프로그램 종료

# 1. 자릿수를 입력받아 저장
# 2. 자릿수 만큼 랜덤한 숫자를 만듬
# 3. while 문을 실행하여 맞출때까지 또는 exit를 입력할때까지 게임을 진행
# 4. 값을 입력받아 생성된 랜덤한 숫자와 비교 (비교시 해당하는 자리수에 맞는 값이 있는지 확인하고 없으면 숫자가 있는지 확인)
import random
import time
from datetime import datetime

def MakeNum():

    random_num = []
    input_num = int(input("자리수 입력 : "))
    # 10자리보다 값이 높으면 높다고 반환
    if input_num <= 10:
    # set을 사용해 중복 숫자 제거
        random_num = set(random_num)

    # while을 이용해 입력받은 숫자 자리만큼 숫자 랜덤으로 생성
        while len(random_num) <= input_num-1:
                random_num.add(random.randint(0,9))

    # 리스트로 변환 후 랜덤으로 셔플
        random_num=list(random_num)
        random.shuffle(random_num)
        return random_num

    else:
        print("자리수 최대는 10자리 입니다.")
        return False

def GameStart(list_):
    start_time = time.time()
    end = False
    int_count = 0
    print(f"{len(list_)}개의 숫자를 입력해주세요. 종료 코드:exit")
    def EndMessage(count):
        end_time = time.time()
        now = datetime.now()
        datetime_ = datetime.strftime(now, "%m/%d %H:%M")
        print("야구 게임이 종료되었습니다.")
        print(f"입력 횟수 : {count}번")
        print(f"총 걸린 시간 : {end_time-start_time:.2f}초")
        print(datetime_)
    while end==False:
        s = 0
        b = 0
        out = 0
        input_list = list(input().split())
        if 'exit' not in input_list:
            input_list = list(map(int, input_list))
            int_count += 1
            if len(input_list) == len(list_):
                for i,num in enumerate(list_):
                    #num값과 input_list의 i의 값이 같으면 s++
                    if input_list[i] == num:
                        s +=1
                    elif num in input_list:
                        b += 1
                    else:
                        out += 1
                #길이가 같으면 while 문을 끝내고 아니면 다시 출력
                if s == len(list_):
                    EndMessage(int_count)
                    end = True
                else:
                    print(f"입력 리스트: {input_list} s: {s} b: {b} out: {out} 입력 횟수 :{int_count}")
            else:
                print("길이가 서로 다릅니다.")
        else:
            end = True
            EndMessage(int_count)

random_num = MakeNum()
print(random_num)
if random_num != False:
    GameStart(random_num)





