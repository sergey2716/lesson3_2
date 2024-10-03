
def send_email(message,recipient,sender='university.help@gmail.com'):
    if '@' not in recipient and sender  or  not recipient.endswith(('.com', '.ru', '.net')) and not sender.endswith(('.com', '.ru', '.net')):



        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif recipient == sender:
        print('нельзя отправить письмо самому себе')
    elif sender =='university.help@gmail.com':
        print(f'письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ письмо отправлено с адреса {sender} на адрес {recipient}.')




send_email('ooo','nik.@mail.comс')
send_email('ooo','university.help@gmail.com')
send_email('ooo','nik.@mail.com')
send_email('ooo','nik.@mail.com','university.help@gmail.uk')

