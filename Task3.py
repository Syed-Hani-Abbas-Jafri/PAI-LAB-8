import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", keep_default_na=False)
d3 = df[df["scenario"] == "03_SalaryDiff"].copy()

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=d3,
    x="prep_course",
    y="exam_score",
    order=["Entry", "Mid", "Senior"],
    hue="prep_course",
    palette="Set2",
    legend=False
)
plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.show()