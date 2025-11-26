import datetime

# 1. Создайте словарь email, содержащий следующие поля
email1 = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}
# 2. Добавьте дату отправки: создайте переменную
# send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email1["date"] = send_date
# 3.Нормализуйте e-mail адреса отправителя и получателя:
# приведите к нижнему регистру и уберите пробелы по краям.
email1["from"] = email1["from"].strip().lower()
email1["to"] = email1["to"].strip().lower()
# 4.Извлеките логин и домен отправителя в две переменные login и domain.
login = email1["from"].split("@")[0]
domain = email1["from"].split("@")[1]
# 5.Создайте сокращённую версию текста: возьмите первые 10 символов email["body"]
# и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].
email1["short_body"] = email1["body"][:10] + "..."
# 6.  Списки доменов: создайте список личных доменов с учетом того что там должны быть только уникальные значение
personal = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru', 'mail.ru',
    'list.ru', 'bk.ru', 'inbox.ru']
corporate = ['company.ru', 'corporation.com', 'university.edu',
             'organization.org', 'company.ru', 'business.net']
personal_domens = list(set(personal))
corporate_domens = list(set(corporate))
# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
intersection = set(personal_domens) & set(corporate_domens)
# 8.Проверьте «корпоративность» отправителя:
# создайте булеву переменную is_corporate, равную результату проверки
# вхождения домена отправителя в список корпоративных доменов.
is_corporate = domain in corporate_domens
# 9.Соберите «чистый» текст сообщения без табов и переводов строк:
# замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].
email1["clean_body"] = email1["body"].replace("\t", " ").replace("\n", " ")
# 10.Сформируйте текст отправленного письма многострочной
# f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель}
# Тема: {тема письма}, дата {дата} {чистый текст сообщения}
email1["sent_text"] = f'Кому: {email1["to"]}, от {email1["from"]}\nТема: {email1["subject"]}, \nдата {send_date} \n{email1["clean_body"]}'
# 11Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.
pages = (len(email1["sent_text"])+499)//500
# 12.Проверьте пустоту темы и тела письма:
# создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.
is_subject_empty = not email1["subject"].strip()
is_body_empty = not email1["body"].strip()
# 13.Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].
email1["masked_from"] = login[:2] + "***@" + domain
# 14 Удалите из списка личных доменов значения "list.ru" и "bk.ru".
personal_domens.remove("list.ru")
personal_domens.remove("bk.ru")
#Итог
print(f'1.{email1}, \n'
      f'2.{email1["date"]}, \n'
      f'3.{email1["from"]},{email1["to"]}, \n'
      f'4.{login}, {domain}, \n'
      f'5.{email1["short_body"]}, \n'
      f'6.{personal_domens}, {corporate_domens}, \n'
      f'7.{intersection}, \n'
      f'8.{is_corporate}, \n'
      f'9.{email1["clean_body"]}, \n'
      f'10.{email1["sent_text"]}, \n'
      f'11.{pages}, \n'
      f'12.{is_subject_empty},{is_body_empty}, \n'
      f'13.{email1["masked_from"]}, \n'
      f'14.{personal_domens}.'
      )


