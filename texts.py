A = {}
def readd(name_file):
    with open(name_file, encoding='utf-8') as f:
     lines = f.readlines() 
     len_lin = len([l for l in lines if l.strip(' \n') != ''])
     A[name_file] = len_lin 
   
readd("1.txt")
readd("2.txt")
readd("3.txt")
#print(A)

sorted_tuple = sorted(A.items(), key=lambda x: x[1])
sorted_tuple = dict(sorted_tuple)
#print(sorted_tuple)

for key, value in sorted_tuple.items(): 
    nl = '\n'
    opened = open(key, "r", encoding='utf-8')
    content = opened.read()
    print(f'{key}{nl}{value}{nl}{content}')

#вышло очень странно, но я правда старалась
#потратила на понимание оооочень много времени
#не хотела сравнивать каждый файл по порядку