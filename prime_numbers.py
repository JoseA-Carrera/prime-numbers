def prime(number):
    contador = 0

    if number <= 1:
        return False

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            contador += 1
            break
    if contador == 0:
        return True
    else:
        return False


def run():
    number = int(input('choose a number: '))
    if prime(number):
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')


if __name__ == '__main__':
    run()
