def h(n, source, target, helping):
    if n > 0:
        h(n - 1, source, helping, target)
        print('przenosze kolcek rozmiaru', n, 'z', source, 'na', target)
        h(n - 1, helping, target, source)


# h(4, 'A', 'B', 'C')

def is_palindrom(text):
    if len(text) in [0, 1]:
        return True
    if text[0]==' ':
        return is_palindrom(text[1:]) #usuwanie pierwszego znaku
    if text[-1]==' ':
        return is_palindrom(text[:-1]) #usuwanie ostantiego znaku
    if text[0].capitalize() == text[-1].capitalize():
        return is_palindrom(text[1:-1])
    return False


print(is_palindrom('Atak kata'))
