# for each value - field value in row
# define required format -->
# check length --> to split
# check if there isn't leading zeros --> to add
import xlrd
import re, csv
path = "C:\\Users\\Administrator\\Documents\\Data\\منظم\\Sodic October.xlsx"
location = (path)
wb = xlrd.open_workbook(location)  # workbook object
wi = wb.sheet_by_index(0)
# required_cell = wi.cell_value()
# print(wi.nrows) nrow = 555
v = wi.col_values(5)

# get numbers
v2 = []
for i in v:
    s = str(i)
    x = re.findall("\d+",s)
    v2.append(x)

# remove empty values
v3 = [x for x in v2 if x != []]

# flat your list
flatlist = [item for sublist in v3 for item in sublist]

# remove zeros
for it in flatlist:
    if it == '0':
        flatlist.remove(it)

# edited list (leading zeros)
v4 = []
for i in flatlist:
    if i[0] == '9':
        v4.append("{}{}{}".format('0', '0', i))
    elif i[0] == '0':
        v4.append(i)
    else:
        v4.append("{}{}".format('0', i))
print(v4)

with open('C:\\Users\\Administrator\\Documents\\Data\\m.csv', 'w') as f2:

    writer = csv.writer(f2)
    for val in v4:
        writer.writerow([val])
