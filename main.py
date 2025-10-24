def isOdd(param):
    # 判断参数是否为整数
    if isinstance(param, int):
        # 整数对 2 取余为 1 则是奇数，返回 True
        return param % 2 == 1
    # 非整数情况，返回 False
    return False
