import mgmt_co
import ref_tse


def initialize(num):
    data = {"company": 0, "path": ""}
    print(num, "つ目の運営会社を該当する数字で入力してください。")
    print("GlobalX or JPX-INDEX:1, NEXT FUNDS:2")
    while True:
        company_num = int(input())
        if company_num > 0:
            break
    data["company"] = company_num
    print("組み込み銘柄情報ファイル名を入力してください")  # フォルダーを調査し、自動で選択できるようにする
    data["path"] = input()
    return data


def separate(data):
    match data["company"]:
        case 1:
            return mgmt_co.global_x(data["path"])

        case 2:
            return mgmt_co.next_funds(data["path"])


dup_stocks = {}

ref_tse.listed_issues_initialize()

stock1 = initialize(1)
stock2 = initialize(2)

stocks1_list = separate(stock1)
stocks2_list = separate(stock2)

intersection_keys = stocks1_list.keys() & stocks2_list.keys()

for value in list(intersection_keys):
    dup_stocks[value] = ref_tse.tse_listed_issues().get(value)


print(dup_stocks)
print(len(dup_stocks))
