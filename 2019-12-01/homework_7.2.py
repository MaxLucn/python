f_name = input('Enter file name:')
file = None
try:
    file = open(f_name, 'r')
except:
    print('请输入正确的文件名')
    quit()

number = 0
count = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        line = (line.replace('X-DSPAM-Confidence:', '')).lstrip()
        number += float(line)
        count += 1

print('Average spam confidence:', number/count)