import csv

with open('./source.csv', "r", encoding="utf-8") as f:
    source = csv.reader(f, delimiter="\n")
    # 多次元リストの一次元化
    source_list = sum(list(source), [])


def search():
    input_name = input("鬼滅の登場人物の名前を入力してください >>> ")
    if input_name in source_list:
        print("{}が見つかりました".format(input_name))
    else:
        print("{}は見つかりませんでした".format(input_name))
        with open('./source.csv', 'a', encoding='utf-8') as f:
            source = csv.writer(f, lineterminator='\n')
            source.writerow([input_name])
        print("{}を追加しました".format(input_name))

if __name__ == "__main__":
    search()