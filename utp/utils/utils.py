import jsonpath

def get_value(dic, key):
    '''
    这个函数是从一个字典里面，根据key获取vlaue
    :param dic:传一个字典
    :param key:传一个
    :return:如果有，返回key取到value，如果key没有，返回空字符串
    '''
    result = jsonpath.jsonpath(dic, '$..%s' % key)
    if result:
        return result[0]
    return ''






