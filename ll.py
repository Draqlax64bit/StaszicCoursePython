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


#print(is_palindrom('Atak kata'))

l = [1,2,3,8,5,6]
t=(1,2,3)
d={1:'a',2:'b',3:'c'}

# print(d[1])
# d.update({1:'gg'})
# print(d[1])
# print(l[0])
#
# print(l[0])
# del d[1]
# l.append([1,2,3])
# l[3].append([1,2,3])
# l[3][3].append([1,2,3])
# print(2*(l+l))

print(sorted(l))