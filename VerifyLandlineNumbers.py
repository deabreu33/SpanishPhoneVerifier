import pandas as pd
import zipfile

# -----------------------------
# 1) Load 'geograficos.txt' from ZIP
# -----------------------------
zip_path = r"C:\Users\YourName\Desktop\bd-num.zip"

with zipfile.ZipFile(zip_path) as z:
    with z.open('geograficos.txt') as f:
        df_prefixes = pd.read_csv(f, dtype=str, encoding='latin-1', sep='#', header=None)

df_prefixes.columns = ['prefix', 'subrange', 'province', 'status', 'operator', 'date']

# Create full prefix (e.g., "81500")
df_prefixes['full_prefix'] = df_prefixes['prefix'] + df_prefixes['subrange'].str.zfill(2)

# -----------------------------
# 2) Load Excel file
# -----------------------------
excel_path = r"C:\Users\YourName\Desktop\numbers.xlsx"
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
# 4) Assign operator & province
# -----------------------------
df_prefixes = df_prefixes.sort_values('full_prefix', ascending=False)
df_numbers['operator'] = 'Unknown'
df_numbers['province'] = 'Unknown'

for _, row in df_prefixes.iterrows():
    mask = df_numbers['num_norm'].str.startswith(row['full_prefix'])
    df_numbers.loc[mask, ['operator', 'province']] = row['operator'], row['province']

# -----------------------------
# 5) Save results
# -----------------------------
output_path = r"C:\Users\YourName\Desktop\my_landline_numbers_with_operator.xlsx"
df_numbers.to_excel(output_path, index=False)

print(f"✅ Process completed. File saved to: {output_path}")
