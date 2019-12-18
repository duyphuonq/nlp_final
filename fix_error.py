import json
import sys
import os

#Phuong 0-5229
#Hieu 5230 - 10458
#Long 10459 - 15687
#Minh Tron 15688 - 20916
#Thanh Minh 20917 - 
if sys.version[0] != '3':
    raise BaseException("Cai nay dung python3 moi duoc")
if "error.txt" not in os.listdir():
    raise BaseException("You have no error")
def write_data(sen, label):
    with open("data.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    data[sen] = int(label)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
with open("data.json", "r") as file:
    data = json.load(file)
with open("error.txt", "r") as file:
    err = set()
    for line in file:
        err.add(int(line.rstrip("\n")))
err = list(err)

def backup():
    os.system("cp data.json data_terminal_backup.json")

def error(index):
    with open("error.txt", "a") as file:
        file.write(str(index))

def handled(err):
    if len(err) == 0:
        os.remove("error.txt")
    else:
        with open("error.txt", "w") as file:
            for e in err:
                file.write(str(e))
                file.write("\n")

def fix():
    for index, (key, value) in enumerate(data.items()):
        it = 1
        if index in err:
            if value != 0:
                string =  \
"""
|------------------------------------------|
|index {}, <{}/{}> errors                  |
|----                                      |
|Chứa từ tục tĩu, tiêu cực: 1              |
|Chứa từ cảm thán, ko tục tĩu, tiêu cực: 2 |
|"Không" chứa từ cảm thán, tích cực: 4     |
|Chứa từ cảm thán, tích cực: 5             |
|"Không" có cảm xúc: 3                     |
|Nếu câu trước nhập nhầm: e                |
|Thoát: q                                  |
|------------------------------------------|
|Sentence: "{}"
|Old label: {}
|___________
""".format(index+1, it, len(err), key, value)
                print(string)
                inp = input("(1-5)>>> ")
                if inp.lower() == 'q':
                    sys.exit(0)
                if inp.lower() == 'e':
                    error(index)
                    inp = input("(1-5)>>> ")
                while not inp.isdigit():
                    print("Please enter numerical number")
                    inp = input("(1-5)>>> ")
                while int(inp) < 0 or int(inp) > 5:
                    print("Please enter a number in range(1,5)")
                    inp = input("(1-5)>>> ")
                    if inp.lower() == 'q':
                        sys.exit(0)
                write_data(key, int(inp))
                it +=1
                err.remove(index)
                handled(err)

if __name__ == "__main__":
    fix()