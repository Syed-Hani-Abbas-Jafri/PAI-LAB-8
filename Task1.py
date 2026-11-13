import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", keep_default_na=False)
d1 = df[df["scenario"] == "01_StudyVsScore"].copy()
d1["study_hours"] = d1["study_hours"].astype(float)

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=d1,
    x="study_hours",
    y="exam_score",
    hue="prep_course",
    style="prep_course",
    s=100
)
plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.tight_layout()
plt.show()