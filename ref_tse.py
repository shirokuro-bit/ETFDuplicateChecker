from os import path

import pandas
import requests

URL = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"
FILE_DIR = "stock_information/"
FILE_NAME = "JPXListedIssues.xls"


def listed_issues_initialize():
    is_file = path.isfile(path.join(FILE_DIR, FILE_NAME))
    if is_file:
        print("東証上場銘柄一覧データを更新しますか? Yes:y or No:n")
        while True:
            update = input()
            if update == "y":
                download_listed_issues()
                break
            elif update == "n":
                break
    else:
        # パスが存在しないかファイルではない
        download_listed_issues()


def download_listed_issues():
    # Web上のファイルデータをダウンロード
    response = requests.get(URL)

    # HTTP Responseのエラーチェック
    try:
        response_status = response.raise_for_status()
    except Exception as exc:
        print("Error:{}".format(exc))

    # HTTP Responseが正常な場合は下記実行
    if response_status == None:
        # open()関数にwbを渡し、バイナリ書き込みモードで新規ファイル生成
        file = open(path.join(FILE_DIR, FILE_NAME), "wb")

    # iter_content()メソッドでWebファイルのデータを渡す
    for chunk in response.iter_content(100000):
        file.write(chunk)

    file.close()


def tse_listed_issues():
    stock_list = pandas.read_excel((FILE_DIR + FILE_NAME), sheet_name="Sheet1", usecols=[1, 2]).to_numpy().tolist()
    return dict(stock_list)
