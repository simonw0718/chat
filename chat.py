chat = []
man = []
out = []
with open('input.txt', 'r', encoding='utf-8-sig') as f:
    #”utf-8“ 是以字节为编码单元,它的字节顺序在所有系统中
    #都是一样的,没有字节序问题,因此它不需要BOM(byte-order)
    #所以要使用utf-8-sig
    for line in f:
        line = line.strip()
        chat.append(line)
for word in chat:
    if 'Allen' in word:
        man.append(word + ':')
    elif 'Tom' in word:
        man.append(word + ':')
    else:
        out.append(man[-1] + word)


with open('output2.txt', 'w', encoding = 'utf-8-sig') as f:
	for word in out:
	    f.write(word + '\n')





        