
count = 0
while count < 5:
    num = input()
    if num == 'exit':
        break

    try:
        print(int(num)*2)
        count += 1

    except ValueError:
        print(f"입력한 문자는 {num} 입니다")

    
   


