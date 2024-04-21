cristian = ["ver", "per", "sai", "lec", "ham", "alo", "rus", "nor", "str", "pia", "tsu", "zho", "alb", "hul", "bot", "gas", "mag", "ric", "oco", "sar"]
jack = ["ver", "per", "sai", "lec", "alo", "ham", "nor", "pia", "rus", "alb", "mag", "hul", "bot", "str", "tsu", "ric", "oco", "gas", "zho", "sar"]
res = ["ver", "nor", "per", "lec", "sai", "rus", "alo", "pia", "ham", "hul", "oco", "alb", "gas", "zho", "str", "mag", "sar", "ric", "tsu", "bot"]
d = {0:25, 1:18, 2:15, 3:12, 4:10, 5:8, 6:6, 7:4, 8:2, 9:1}
for i in range(10, 20):
    d[i] = 0

def points(l):
    c = 0
    for i in range(len(l)):
        j = res.index(l[i])
        p = d[abs(i - j)]
        c += p
        print(f"{i+1:2}. {l[i].upper()} {i+1:2} -> {j+1:2}  {p:2} points")
    return c

print("Cristian points:")
c = points(cristian)
print(f"Cristian has {c} points\n")

print("Jack points:")
j = points(jack)
print(f"Jack has {j} points\n")

print(f"Cristian {c} - {j} Jack")