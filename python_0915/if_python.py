# - 사용자의 시험 점수를 입력받아 등급을 출력하는 코드를 만들어주세요
#     - 등급표
#         - 91~100 : A
#         - 81~90 : B
#         - 71~80 : C
#         - ~71 : F


def get_grade(score):
    # some code
    if score > 90:
        grade = 'A'
    elif score > 80:
        grade = 'B'    
    elif score > 70:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade
    


score = int(input())
grade = get_grade(score)
print(grade) # A ~ F