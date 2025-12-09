
# Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.
import sys
import pandas as pd
if len(sys.argv)!=3:
    print("python csv2xls.py <input_csv_file> <output_excel_file>")
    sys.exit(1)
csv_file=sys.argv[1]
excel_file=sys.argv[2]
try:
    df=pd.read_csv(csv_file)
    df.to_excel(excel_file,index=False)
    print(f"Successfully converted {csv_file} to {excel_file}")
except Exception as e:
    print("Error" ,{e})