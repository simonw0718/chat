
#讀取檔案轉成list
def readfile(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        #沒有-sig會有\ufeff 這是關於編碼的資訊
        #”utf-8“ 是以字节为编码单元,它的字节顺序在所有系统中
        #都是一样的,没有字节序问题,因此它不需要BOM(byte-order)
        #所以要使用utf-8-sig
        for line in f:
            line = line.strip()
            chat.append(line)
            # 也可以寫chat.append(line.strip())
        return chat
#改成OUT形式
def translate(chat):
    out = []
    man = None #同樣宣告，但沒有質
    for word in chat:
        if word == 'Allen':
            man = 'Allen'
            continue
        elif word == 'Tom':
            man = 'Tome'
        if man: # 如果man有質才執行
            out.append(man + ': ' + word)
    return out
#寫入
def writein(filename, out):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for word in out:
            f.write(word + '\n')
#main function
def main(filename):
    chat = readfile(filename)
    out = translate(chat)
    writein('output2.txt', out)

main('input.txt')



        