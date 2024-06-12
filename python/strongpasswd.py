numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
casos = [0,0,0,0]

def minimumNumber(n, password):
  
    if len(password) < 6:
        return 6-n
    for x in password:
        if x in numbers:
            casos[0] = 1
        elif x in lower_case:
            casos[1] = 1
        elif x in upper_case:
            casos[2] = 1
        elif x in special_characters:
            casos[3] = 1
    return  max(4 - sum(casos), 6 - n)

print(minimumNumber(10, "hackerrans"))