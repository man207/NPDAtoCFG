from PDAv1 import pushdownautomata
import sys, json

def read_in():
    lines = sys.stdin.readlines()
    x=[]
    for i in range(6):
        x.append([])
    x[0] = json.loads(lines[0])
    x[1] = json.loads(lines[1])
    x[2] = json.loads(lines[2])
    x[3] = json.loads(lines[3])
    x[4] = json.loads(lines[4])
    x[5] = json.loads(lines[5])
    
    return x

def main():
    
    lines = read_in()

    
    pa = pushdownautomata()
    yt = str
    for i in lines[0]:
        pa.addstate(i)
    for i in lines[1]:
        x,y,z = i.split("|")
        y1 , yt = y.split(",")
        y2 , y3 = yt.split(lines[4])
        if y1 == lines[5]:
            y1 = "λ"
        if y2 == lines[5]:
            y2 = "λ"
        if y3 == lines[5]:
            y3 = "λ"
        pa.addtransition([x,y1,y2,z,y3])
    for i in lines[2]:
        pa.addfinalstate(i)
    pa.setinitialstate(lines[3][0])

    temp = pa.toCFG()
    rules = []
    for i in temp:
        i.insert(1,lines[4])
        temp1 = ' '.join(map(str, i))
        temp1 = temp1.replace("\'","")
        temp1 = temp1.replace("(","&lt;")
        temp1 = temp1.replace(")","&gt;")
        temp1 = temp1.replace("λ",lines[5])
        rules.append(temp1)
    sended = ""
    
    for i in rules:
        sended = sended + "<p>" + i + "</p>"
    print(sended)

# Start process
if __name__ == "__main__":
    main()
