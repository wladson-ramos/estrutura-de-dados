sal = float(input())

if sal <= 1000:
    new_sal = sal + sal * 0.20
elif sal <= 1500:
    new_sal = sal + sal * 0.15
elif sal <= 2000:
    new_sal = sal + sal * 0.10
elif sal > 2000:
    new_sal = sal + sal * 0.05

print("%.2f" % new_sal)