"""
Create OHLC - groups data to X minutes

JonV / May 16 2015
"""

import sys
import pandas

def main(filename):
    df = pandas.read_csv(filename, parse_dates={'DateTime'}, index_col='DateTime', names=['Tid', 'Dealable', 'Pair', 'DateTime', 'Buy', 'Sell'], 
                         date_parser=parse)
    
    #del df['Tid']
    #del df['Dealable']
    #del df['Pair']
    
    # group every 15 minutes and create OHLC
    grouped_data = df.resample('15Min', how='ohlc')
    #grouped_data = df.resample('24H', how='ohlc')

    # save to file
    grouped_data.to_pickle(filename+'-OHLC.pkl')

"""
Some datetimes don't have nanoseconds that's why I need to parse like this
"""
def parse(timestamps):
    clean = timestamps.split(".")[0] if '.' in timestamps else timestamps
    return pandas.datetime.strptime(clean,"%Y-%m-%d %H:%M:%S")
    
if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print 'create_OHLC.py <inputfile.csv>'
        sys.exit(2)
    main(sys.argv[1])

