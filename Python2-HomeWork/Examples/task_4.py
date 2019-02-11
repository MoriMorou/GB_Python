import hashlib

def rabin_karpa(s, subs):
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                return i

    return -1


s1 = input('Введите строку: ')
s2 = input('Введите подстроку: ')
print(rabin_karpa(s1, s2))
