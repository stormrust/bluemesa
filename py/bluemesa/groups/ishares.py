import json
import os
import sys
import pandas as pd

path_bmtop = os.environ['BMTOP']
#ishares_dir = "/equity-etf/data/ishares/iwv.csv"
ishares_dir = "/equity-etf/data/ishares/"

def get_filename(symbol):
    filename = path_bmtop + ishares_dir + symbol + ".csv"
    return(filename)

# Read the company name and symbol from a csv file
# and write the data out to json
def iwv_to_json():
    filename = path_bmtop + iwv_csv_file
    df = pd.read_csv(filename, sep=',')

    sseries = df['Ticker']
    svalues = sseries.values
    # convert strings in array to lowercase
    svlc = map(str.lower, svalues)
    symbols = tuple(svlc)

    nseries = df['Name']
    nvalues = nseries.values
    names = tuple(nvalues)
    d = {}
    for s, n in zip(symbols, names):
        d[s] = n
    myjson = json.dumps(d)
    print(myjson)

# Read the company name and symbol from a csv file
# and write it out to some other format
def iwv():
    filename = path_bmtop + iwv_csv_file
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values
    nseries = df['Name']
    names = nseries.values
    # convert strings in array to lowercase
    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    #names = map(str.lower,names)
    names = tuple(names)
    for i, name in enumerate(tickers):
        print(tickers[i],names[i])

# Read the symbol from a csv file
# and write it out to a redis set
def iwv_to_redis_set():
    filename = path_bmtop + iwv_csv_file
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values

    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    for i, name in enumerate(tickers):
        print(tickers[i])

def check_args(arg):
    group = {'pff','iwv'}
    return(arg in group)

# py iwv.py > iwvn.json
if __name__ == "__main__":
    arg = sys.argv[1]
    print(arg)
    val = check_args(arg)
    print(val)
    filename = get_filename(arg)
    print(filename)
    #iwv_to_json()
    #iwv()
    #iwv_to_redis_set()