import csv
import os

### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
source_b=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### リスト更新
def updateSource(listCSV, source):    
    ### ここに検索ロジックを書く
    index = 0
    # print(len(listCSV))
    while index < len(listCSV):
        if not(listCSV[index] in source):
            source.append(listCSV[index])
        index = index + 1
    return source

### csv読込み
def readCSV(listCSV):
    csvFile =input("CSVファイルを指定してください（フルパス） >>> ")
    if os.path.exists(csvFile):
        with open(csvFile) as f:
            listCSV = f.read()
            f.close()
            print(listCSV)
            return listCSV

if __name__ == "__main__":
    listCSV = []
    readCSV(listCSV)
    print(listCSV)
    updateSource(listCSV, source)
    print("鬼滅の登場人物の（更新前）⇒",source_b)
    print("鬼滅の登場人物の（更新後）⇒",source)
