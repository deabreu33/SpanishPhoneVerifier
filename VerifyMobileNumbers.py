import pandas as pd
import zipfile

# -----------------------------
# 1) Load 'moviles.txt' from ZIP
# -----------------------------
zip_path = r"C:\Users\YourName\Desktop\bd-num.zip"

with zipfile.ZipFile(zip_path) as z:
    with z.open('moviles.txt') as f:
        df_prefixes = pd.read_csv(f, dtype=str, encoding='latin-1', sep='#', header=None)

df_prefixes.columns = ['prefix', 'unknown1', 'unknown2', 'status', 'operator', 'date']

# -----------------------------
# 2) Load Excel file
# -----------------------------
excel_path = r"C:\Users\YourName\Desktop\numbers.xlsx"  # update path
df_numbers = pd.read_excel(excel_path, dtype=str)
phone_col = 'numbers'

# -----------------------------
# 3) Normalize phone numbers
# -----------------------------
def clean_num(s):
    if pd.isna(s):
        return ""
    s = str(s).replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if s.startswith("+34"):
        s = s[3:]
    if s.startswith("0034"):
        s = s[4:]
    return s

df_numbers['num_norm'] = df_numbers[phone_col].map(clean_num)

# -----------------------------
# 4) Assign operator
# -----------------------------
df_prefixes['pref_len'] = df_prefixes['prefix'].str.len()
df_prefixes_sorted = df_prefixes.sort_values('pref_len', ascending=False)

def assign_operator(num):
    for _, row in df_prefixes_sorted.iterrows():
        if num.startswith(str(row['prefix'])):
            return row['operator']
    return 'Unknown'

df_numbers['operator'] = df_numbers['num_norm'].map(assign_operator)

# -----------------------------
# 5) Save results
# -----------------------------
output_path = r"C:\Users\YourName\Desktop\my_mobile_numbers_with_operator.xlsx"
df_numbers.to_excel(output_path, index=False)

print(f"✅ Process completed. File saved to: {output_path}")
