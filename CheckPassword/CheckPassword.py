# Проверка длины пароля по длине
def password_strength(password):
    if (len(password)<8):
        return ("слабый")
    elif (8<=len(password)<=11):
        return ("средний")
    else:
        return ("сильный")