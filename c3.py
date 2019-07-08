
lines = []
with open('3.txt','r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split(' ')
	time = s[0][:5] #第0個前5
	name = s[0][5:] #第0個5之後
	print(time)
	print(name)
	print(s)

# string can be used as list, can use range and 清單分割法
