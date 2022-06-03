import random
import string


def generate_password():
    characters = list(string.ascii_lowercase)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']

    length = int(input('How long do you want your password: '))
    add_num = input('Do you want number in your password(Y/N): ')
    add_special_char = input(
        'Do you special character in your password(Y/N): ')

    generated_password = []

    if add_num.lower() == 'y':
        characters.extend(numbers)

    if add_special_char.lower() == 'y':
        characters.extend(special_characters)

    for _ in range(length):
        generated_password.append(random.choice(characters))

    return ''.join(generated_password)


if __name__ == "__main__":
    print(generate_password())
