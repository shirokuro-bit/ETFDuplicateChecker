import pandas
FOLDER_PATH = "stock_information/"
EXCEL_EXTENSION = ".xlsx"
CSV_EXTENSION = ".csv"


def next_funds(filepath):
    stock_list = pandas.read_excel((FOLDER_PATH + filepath + EXCEL_EXTENSION), sheet_name='保有明細', skiprows=2, skipfooter=7, usecols=[1, 2]).to_numpy().tolist()
    return dict(stock_list)


def global_x(filepath):
    stock_list = pandas.read_csv((FOLDER_PATH + filepath + CSV_EXTENSION), skiprows=3, usecols=[0, 1]).to_numpy().tolist()
    return dict(stock_list)
