def get_mask_card_number(card_info):
    """
    Принимает на вход строку с типом и номером карты и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    parts = card_info.split()
    card_number = parts[-1]
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return ' '.join(parts[:-1]) + ' ' + masked_number


def get_mask_account(account_info):
    """
    Принимает на вход строку с типом и номером счета и возвращает маску номера по правилу **XXXX
    """
    parts = account_info.split()
    account_number = parts[-1]
    if len(account_number) < 6:
        raise ValueError("Номeр счета должен содержать не менее 6 цифр.")
    masked_number = f"**{account_number[-4:]}"
    return ' '.join(parts[:-1]) + ' ' + masked_number


def mask_account_card(card_info):
    """
    Принимает на вход строку формата "Visa Platinum 7000792289606361" и "Счет 73654108430135874305"
    """
    if "Счет" in card_info:
        return get_mask_account(card_info)
    else:
        return get_mask_card_number(card_info)


def get_date(date_str):
    """
    Принимает на вход в формате "2024-03-11T02:26:18.671407" возвращает в формате "ДД.ММ.ГГГГ"
    """
    try:
        date_part = date_str.split('T')[0]
        year, month, day = date_part.split('-')
        return f"{day}.{month}.{year}"
    except ValueError:
        raise ValueError("Неверный формат даты")


if __name__ == "__main__":
    card_info = input("enter card number:")
    account_info = input("enter account number:")
    date_str = input("enter date:")

    print(mask_account_card(card_info))
    print(mask_account_card(account_info))
    print(get_date(date_str))
