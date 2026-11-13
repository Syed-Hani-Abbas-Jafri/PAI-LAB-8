import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", keep_default_na=False)
d5 = df[df["scenario"] == "05_AdVsRevenue"].copy()
d5["ad_spend"] = d5["study_hours"].astype(float)
d5["revenue"] = d5["prep_course"].astype(float)

plt.figure(figsize=(8, 5))
sns.regplot(
    data=d5,
    x="ad_spend",
    y="revenue",
    marker="+",
    scatter_kws={"color": "darkgreen"}
)
plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()