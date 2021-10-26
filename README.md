# Amazon-Tracking-Number
Fetch tracking numbers of Amazon orders, for the ease of the logistics.

Read Me First (How to use this code):
1. Get Amazon "Items" report from https://www.amazon.com/gp/b2b/reports . For example, 23-Oct-2021_to_26-Oct-2021-items.csv as the first attached csv file.
2. Put this items.csv file together with Extract_Track_Num.py in the same folder. For example, "/Users/tonypositive/Desktop/Resources/Amazon_Orders"
3. Open your Terminal app (e.g. ITerm) and type "cd /Users/tonypositive/Desktop/Resources/Amazon_Orders"
4. Type "python3 Extract_Track_Num.py --path_to_order_csv 23-Oct-2021_to_26-Oct-2021-items.csv --path_to_tracknum_csv 23-Oct-2021_to_26-Oct-2021-tracknum.csv" in your Terminal app.
5. You will get a filtered version of Amazon "Items" report, named as 23-Oct-2021_to_26-Oct-2021-tracknum.csv. You can change the csv file name following the argument --path_to_tracknum_csv in the step 4 to your desired tracking number csv file name.

## Amazon order tracker v0.0.1
![image](https://user-images.githubusercontent.com/25763546/138804040-786524b0-ae9d-406e-9f0d-64d208b7b50f.png)
