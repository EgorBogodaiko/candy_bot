def check_menu_item(choise:str):
    """Принимает строку со значением
    Возвращает bool - является ли входящая строка опцией меню"""
    check=False
    if choise in ('1','2','3','4','5','6'):
        check = True        
    return check

def checker_field_val(field:str,value:str):
    """Принимает: заголовок поля, значение, которое нужно проверить на соответствие формату поля
    возвращает Булеву функцию ИСТИНА\ЛОЖЬ на соответствие формату"""
    result = False
    if field =='phone_num':
        if len(value)<=11 and value.isdigit():
            result=True
    elif field =='id':
        if value.isdigit()==True:
            result=True
    elif field in ('first_name','last_name'):
        if value.isalpha()==True:
            result = True
    elif any(ch.isdigit() for ch in value)==False and len(value)<=30:
        result=True 
    return result
    
def checker_field(field:str):
    if field in ['id','first_name','last_name','phone_num','comment']:
        return True
    else:
        return False