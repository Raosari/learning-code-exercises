def simple_5(num):
    try:
        if num >= 0:
            return int(num) + 5
        else:
            return 'Enter a number'
    except TypeError as err:
        return err