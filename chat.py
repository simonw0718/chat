
#讀取檔案轉成list
def readfile(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        #”utf-8“ 是以字节为编码单元,它的字节顺序在所有系统中
        #都是一样的,没有字节序问题,因此它不需要BOM(byte-order)
        #所以要使用utf-8-sig
        for line in f:
            line = line.strip()
            chat.append(line)
        return chat

#改成OUT形式
def translate(chat):
    man = []
    out = []
    for word in chat:
        if 'Allen' in word:
            man.append(word + ':')
        elif 'Tom' in word:
            man.append(word + ':')
        else:
            out.append(man[-1] + word)
    return out

#寫入
def writein(out):
    with open('output2.txt', 'w', encoding = 'utf-8-sig') as f:
        for word in out:
            f.write(word + '\n')

def main(filename):
    chat = readfile(filename)
    out = translate(chat)
    writein(out)

main('input.txt')



        