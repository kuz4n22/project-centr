
#передача данныех контракта, для авторизированного юзера
def user_contracts(request):
    # '''
    # Если юзер авторизирован, то в шаблон передается список "user_contracts",
    # который содержит все контракты юзера, отсортированные по дате заключения
    # контракта
    # '''
    # if request.user.is_authenticated:
    #     return {
    #         'user_contracts': request.user.contracts.all().order_by('-contract_date')
    #     }
    # return {}
    '''
    Если юзер авторизирован, то в шаблон передается объект "user_contract",
    который имеет параметры, соответствующие параметрам модели контракт
    '''
    if request.user.is_authenticated:
        return {
            'user_contract': request.user.contracts.last()
        }
    return {}
    


def current_url(request):
    return {'current_url': request.path}