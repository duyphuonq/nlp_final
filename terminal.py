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
def write_data(sen, label):
    with open("data.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    data[sen] = int(label)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
with open("data.json", "r") as file:
    data = json.load(file)

def backup():
    os.system("cp data.json data_terminal_backup.json")

def intro():
    string = \
"""
Chào mừng bạn đã đến với script dán label.
Bạn là ai?
1.Phương    4.Minh Tròn
2.Hiếu      5.Thánh Minh 
3.Long      6.Exit
"""
    print(string)

def exit():
    sys.exit()

def error(index):
    with open("error.txt", "a") as file:
        file.write(str(index))

def add(num):
    if num == '1':
        start = 0
        end = 5229
        name = "Phương"
    elif num == '2':
        start = 5229#5230 - 10458
        end = 10458
        name = "Hiếu"
    elif num == '3':
        start = 10458
        end = 15687
        name = "Long"
    elif num == '4':
        start = 15687
        end = 20916
        name = "Minh Tròn"
    elif num == '5':
        start = 20916
        end = 26143
        name = "Thánh Minh"
    for index, (key, value) in enumerate(data.items()):
        if index >= start  and index < end:
            if value == 0:
                string =  \
"""
|------------------------------------------|
|{} <{}/{}>                                |
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
|___________
""".format(name, index+1, end, key)
                print(string)
                inp = input("(1-5)>>> ")
                if inp.lower() == 'q':
                    exit()
                if inp.lower() == 'e':
                    error(index-1)
                    inp = input("(1-5)>>> ")
                    if inp.lower() == 'q':
                        exit()
                while not inp.isdigit():
                    print("Please enter numerical number")
                    inp = input("(1-5)>>> ")
                while int(inp) < 0 or int(inp) > 5:
                    print("Please enter a number in range(1,5)")
                    inp = input("(1-5)>>> ")
                write_data(key, int(inp))



while True:
    intro()
    option = input(">>> ")
    if not option.isdigit() or len(option) > 1 or int(option) < 1 or int(option) > 6:
        continue
    if option == '6':
        break
    backup()
    add(option)
    