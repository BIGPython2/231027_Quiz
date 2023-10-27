# 주민등록번호 유효성 검사

def validate_id_number(id_number):
    if len(id_number) != 13 or not id_number.isdigit():
        return False

    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    a = [int(digit) * number for digit, number in zip(id_number[:-1], numbers)]
    plus_number = sum(a)
    remainder = plus_number % 11
    check_number = 11 - remainder if remainder != 0 else 1
    return check_number == int(id_number[-1])

id_number = input("주민번호를 입력하세요 (예: 123456-1234567): ")
if validate_id_number(id_number):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")
