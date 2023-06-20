
def func(c):
    if c == c[::-1]: # -1 здесь шаг строки: от конца к началу
        return True
    else:
        return False

print(func('шалаш'))