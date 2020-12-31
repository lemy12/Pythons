import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]


def read_birthday():
    with open("birthday.json", "r") as fRead:
        info = json.load(fRead)
    return info


def check_month():
    info_months = read_birthday()
    for k, v in info_months.items():
        value_split = v.split('/')
        info_months[k] = MONTHS[int(value_split[1]) - 1]
    return info_months


if __name__ == "__main__":
    list_month = []
    dict = check_month()
    for key in dict:
        list_month.append(dict[key])
    list_count = Counter(list_month)
    print(list_count.keys())

    output_file("plot.html")
    p = figure(x_range=MONTHS)

    p.vbar(x=list(list_count.keys()), top=list(list_count.values()), width=0.7)
    show(p)
