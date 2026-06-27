t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if 'B' not in s:
        print(0)
    else:
        last_b = s.rfind('B')
        ans = 0
        for i in range(last_b):
            if s[i] == 'A':
                ans += 1
        print(ans)