
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    index=0
    while index < len(source):
        if word == source[index]:
            print("{}が見つかりました".format(word))
            return
        index = index + 1
    print("{}が見つかりませんでした".format(word))

if __name__ == "__main__":
    search()
