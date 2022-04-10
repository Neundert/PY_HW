import json
str = []
pr = []
f = []
avg = 0
q = 0
with open("text_7.txt", 'r', encoding = 'utf-8') as firm:
    for i in firm:
        str.append(i.split())
    for j in range(len(str)):
        pr.append(int(str[j][2]) - int(str[j][3]))
        f.append(str[j][0])
    my_dict = dict(zip(f, pr))
    for n in range(len(pr)):
        if pr[n] >= 0:
            avg += pr[n]
            q += 1
avg_total = avg / q
my_dict_2 = dict(average_profit = avg_total)
total_list = []
total_list.append(my_dict)
total_list.append(my_dict_2)

print(total_list)

with open("text_777.json", "w", encoding = 'utf-8') as write_f:
    json.dump(total_list, write_f, ensure_ascii=False,  indent=2)
