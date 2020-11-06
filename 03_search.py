
import os
import csv

### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# ソースチェック（戻り：0:リストに存在しない　1:リストに存在する）
def chkSource(str):
    source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
    index=0
    while index < len(source):
        if str == source[index]:
            return 1
        index = index + 1
    return 0

### 検索ツール
def search():
    ### ここに検索ロジックを書く
    csvFile =input("CSVファイルを指定してください（フルパス） >>> ")
    if os.path.exists(csvFile):
        with open(csvFile) as f:
            index = 0
            for line in f:
                listWork = line.split(',')
                lenList = len(listWork)
                while index < lenList:
                    if chkSource(listWork[index]):
                        index = index + 1
                        continue
                    else:
                        source.append(listWork[index])  
                    index = index + 1
    else:
        print('指定したファイルは存在しません')
        return
    
    print('リスト（更新後）：')
    print(source)

if __name__ == "__main__":
    search()
