#讀取字典
a={
    "a": {
        "a1": "a-1",
        "a2": "a-1"
    },
    "b": {
        "b1": "b-1",
        "a2": "b-1"
    }
}
b=list(a.keys())
for i in range(len(b)):
    print(a[b[i]])
    print(b[i])
########## 輸出 ##########
# {'a1': 'a-1', 'a2': 'a-1'}
# a
# {'b1': 'b-1', 'a2': 'b-1'}
# b


#////////////////////////
#寫入字典(JSON版
"""需新增 XXX.json 並加入{}，例:
{

}
"""
import json
while True:
    with open('XXX.json', mode='r', encoding='UTF8') as jfile:
        XYZ = json.load(jfile)
    i = len(XYZ)+1
    x=""
    while str(x) == "":
        x = input("請輸入x:")
        if str(x) == "":
            print("請輸入數值")
    new_list = f"資料 {i}"
    a = XYZ[new_list] = {}
    a.setdefault("x", str(x))
    print(XYZ)
    with open('XXX.json', mode='w', encoding='UTF8') as jfile:
        json.dump(XYZ, jfile, ensure_ascii=False, indent=4)

########## 輸出 ##########
#將更改 XXX.json
#{
#   "1":{
#       "X": "你輸入的資料"
#   },
#   "2":{
#       "X": "你輸入的資料2"
#   }
# }
