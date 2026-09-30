# Проверка на возраст
def ticket_category(age):
    if age < 7:
        return "детский"
    elif 7 <= age <= 17:
        return "льготный"
    elif 18 <= age <= 59:
        return "взрослый"
    else:
        return "льготный"