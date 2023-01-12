import csv
from bot_config import dp,bot

async def search(mess,bd: str, field: str, value: str, type_output: int):
    """Принимает: базу данных, поле, по которому будет производиться поиск, 
    значение, по которому будет произовдиться поиск,
    тип вывода: 1 - вывести все строки, 2 - вывести идентификаторы найденных строк списком
    возвращает список ID найденных строк
    """
    message=mess
    with open(bd) as f:
        reader = csv.DictReader(f, delimiter='|')
        headers = reader.fieldnames
        if type_output == 1:
            await bot.send_message(message.from_user.id, text='Найденные строки:')
            await bot.send_message(message.from_user.id, text=headers)
            for item in reader:
                if item[field] == value:
                     await bot.send_message(message.from_user.id, text=list(item.values()))
        elif type_output == 2:
            await bot.send_message(message.from_user.id, text='Список ID найденных строк:')
            id_list = []
            for item in reader:
                if item[field] == value:
                    id_list += item['id']
            return id_list
        else:
            print('Неизвестный режим работы функции')
