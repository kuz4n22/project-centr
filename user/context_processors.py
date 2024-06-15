
#передача данныех контракта, для авторизированного юзера
def user_contracts(request):
    '''
    Если юзер зарегестрирован, то в шаблон передается список "user_contracts",
    который содержит все контракты юзера, отсортированные по дате заключения
    контракта
    '''
    if request.user.is_authenticated:
        return {
            'user_contracts': request.user.contracts.all().order_by('-contract_date')
        }
    return {}