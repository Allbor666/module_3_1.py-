
Function = 'send_email'

def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Hello", "student@example.com")
send_email("Hello", "student@example.com", "custom.sender@example.net")
send_email("Hello", "university.help@gmail.com")
send_email("Hello", "invalid_recipient")
send_email("Hello", "student@example.com", "invalid_sender")