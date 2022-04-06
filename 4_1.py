from sys import argv

script_name, yeld, rate, premium = argv

print("Размер з/п: ", int(yeld) * int(rate) + int(premium))
