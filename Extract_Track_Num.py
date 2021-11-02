from numpy import NaN
import pandas as pd
import argparse

# The argument parser for the input csv file path and the output csv file path. 
# There could be more arguments in the future, e.g., the path of a directory that includes many history order csvs.
parser = argparse.ArgumentParser(description='Process Amazon orders.')
parser.add_argument('--path_to_order_csv', default='23-Oct-2021_to_26-Oct-2021-items.csv', type=str, \
    help='The path to Amazon "Items" report. You can get it through https://www.amazon.com/gp/b2b/reports \
         Once you get it, you can save it in the same directory with this python file.')
parser.add_argument('--path_to_tracknum_csv', default='23-Oct-2021_to_26-Oct-2021-tracknum.csv', type=str, \
    help='The output path for Amazon "Tracking Numbers" report.  \
         The output csv is a filtered version of Amazon "Items" report.')
args = parser.parse_args()

# Filter AMZN_US(...) for each of tracking number.
# TODO: Current parser is very dumb and hard-coded.
# Further modification might be needed if different carrier formating come out.
def filter_Track_Num(CarrierName_TrackNum):
    if CarrierName_TrackNum is NaN:
        return NaN
    else:
        return CarrierName_TrackNum.split('(')[-1][:-1]

def main():
    # Use pandas for data processing.
    Orders = pd.read_csv(args.path_to_order_csv) 

    # Filter column headers for tracking number csv file to output.
    Orders = Orders[['Title','Carrier Name & Tracking Number',  \
         'Purchase Price Per Unit', 'Quantity','Item Total']]

    # Sparse tracking numbers out of "Carrier Name & Tracking Number"
    Orders['Carrier Name & Tracking Number'] = Orders['Carrier Name & Tracking Number'].apply(filter_Track_Num)

    # Rename the column name to denote tracking numbers
    Orders = Orders.rename(columns={'Carrier Name & Tracking Number': 'Track Num'})

    # Save the output tracking number csv file to the path you have set in the arguments when you run this .py file.
    print(Orders)
    Orders.to_csv(args.path_to_tracknum_csv,index=False)

if __name__ == "__main__":
    main()