# ------------- 1. https://codeforces.com/problemset/problem/4/A ------------- #
n = int(input())
if n == 0 or n == 2:
    print("NO")
else:
    if n % 2 == 0:
        print("YES")
    else:
        print("NO")

# ------------- 2. https://codeforces.com/problemset/problem/71/A ------------ #
n = int(input())
for i in range(n):
    string = input()
    if len(string) > 10:
        x = len(string)-2
        print("{}{}{}".format(string[0], x, string[-1]))
    else:
        print(string)

# ------------ 3. https://codeforces.com/problemset/problem/118/A ------------ #
string = input()
result = list()
for i in string.lower():
    if i not in ['a', 'e', 'i', 'o', 'u', 'y']:
        result.append(".{}".format(i))
string = ""
print(string.join(result))

# ------------ 4. https://codeforces.com/problemset/problem/112/A ------------ #
string1 = input()
string2 = input()
lexic = True
for i in range(len(string1)):
    if ord(string1[i].lower()) < ord(string2[i].lower()):
        print(-1)
        lexic = False
        break
    elif ord(string1[i].lower()) > ord(string2[i].lower()):
        print(1)
        lexic = False
        break
if lexic == True:
    print(0)

# ------------ 5. https://codeforces.com/problemset/problem/339/A ------------ #
string = list(map(int, input().split('+')))
string = list(map(str, sorted(string)))
print("+".join(string))