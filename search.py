source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

def search():
    input_name = input("鬼滅の登場人物の名前を入力してください >>> ")
    if input_name in source:
        print("{}が見つかりました".format(input_name))
    else:
        print("{}は見つかりませんでした".format(input_name))

if __name__ == "__main__":
    search()