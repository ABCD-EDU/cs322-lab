import pandas as pd

df = pd.read_csv("../../res/churndata_orig.csv")
df["Int'l Plan"] = df["Int'l Plan"].apply(lambda x: 1 if x == 'yes' else 0)
df["VMail Plan"] = df["VMail Plan"].apply(lambda x: 1 if x == 'yes' else 0)
df['Churn?'] = df['Churn?'].apply(lambda x: 1 if x == 'True.' else 0)

df.reset_index(drop=True, inplace=True)
df.to_csv("../../res/churndata.csv", encoding="utf8", index=False)
