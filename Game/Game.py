import random


def winner(player, computer):
    if player != "камень" and player != "ножницы" and player != "бумага":
        return "ошибка"
    if player == computer:
        return "ничья"
    if player == "камень" and computer == "ножницы":
        return "ты"
    if player == "ножницы" and computer == "бумага":
        return "ты"
    if player == "бумага" and computer == "камень":
        return "ты"
    return "компьютер"


print("Твой ход: камень, ножницы или бумага?")
player = input()
computer = random.choice(["камень", "ножницы", "бумага"])
result = winner(player, computer)

if result == "ошибка":
    print("Такого хода нет.")
elif result == "ничья":
    print(f"Компьютер выбрал: {computer}. Ничья")
elif result == "ты":
    print(f"Компьютер выбрал: {computer}. Победа за тобой!")
else:
    print(f"Компьютер выбрал: {computer}. Победил компьютер.")

    # Создание новой папки