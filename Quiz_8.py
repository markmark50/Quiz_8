import random

def 랜덤_번호_생성():
    number_list = []

    while len(number_list) < 6:
        number = random.randint(1, 45)

        if number not in number_list:
            number_list.append(number)

    number_list.sort()
    return number_list

def main():
    번호_생성 = 랜덤_번호_생성()
    numbers_string = ', '.join(map(str, 번호_생성))

    print(f"생성된 로또 번호는 {numbers_string} 입니다.")

if __name__ == "__main__":
    main()
