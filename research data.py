import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 解决中文乱码
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ===================== 1. 读取数据 =====================
FILE_PATH = r"C:\Users\邹思琪\Desktop\111.xlsx"
df = pd.read_excel(FILE_PATH, engine="openpyxl")

# 定义列名和选项
COL1 = "How would you describe your overall social well-being this semester?"
COL2 = "How would you rate your overall sleep quality this semester?"
OPTIONS = ["Very poor", "Poor", "Good", "Very good"]

# ===================== 2. 数据清洗&数值映射 =====================
# 过滤掉空值，确保计算有效
df = df.dropna(subset=[COL1, COL2])

# 选项映射为数值（1-4分，越好分数越高）
score_map = {"Very poor": 1, "Poor": 2, "Good": 3, "Very good": 4}
df["social_score"] = df[COL1].map(score_map)
df["sleep_score"] = df[COL2].map(score_map)

# ===================== 3. 计算Pearson相关系数 =====================
r, p = pearsonr(df["social_score"], df["sleep_score"])
print(f"✅ Pearson相关系数：r = {r:.4f}")
print(f"✅ 显著性p值：p = {p:.4f}")

# ===================== 4. 绘制正确的柱状图 =====================
plt.figure(figsize=(14, 6))

# 子图1：社交幸福感分布
plt.subplot(1, 2, 1)
social_counts = df[COL1].value_counts().reindex(OPTIONS, fill_value=0)
social_counts.plot(kind="bar", color="#1E88E5", edgecolor="white")
plt.title("Social Well-being Distribution", fontsize=14)
plt.ylabel("Number of Respondents", fontsize=12)
plt.xticks(rotation=0)
# 标注数值
for i, v in enumerate(social_counts):
    plt.text(i, v + 1, str(v), ha="center", fontsize=10)

# 子图2：睡眠质量分布
plt.subplot(1, 2, 2)
sleep_counts = df[COL2].value_counts().reindex(OPTIONS, fill_value=0)
sleep_counts.plot(kind="bar", color="#F44336", edgecolor="white")
plt.title("Sleep Quality Distribution", fontsize=14)
plt.ylabel("Number of Respondents", fontsize=12)
plt.xticks(rotation=0)
# 标注数值
for i, v in enumerate(sleep_counts):
    plt.text(i, v + 1, str(v), ha="center", fontsize=10)

plt.tight_layout()
plt.show()

# ===================== 5. 绘制正确的散点图 =====================
plt.figure(figsize=(10, 8))

# 按原始数据绘制散点，按社交幸福感分组着色
colors = {"Very poor": "#F44336", "Poor": "#FF9800", "Good": "#4CAF50", "Very good": "#2196F3"}
for opt in OPTIONS:
    subset = df[df[COL1] == opt]
    plt.scatter(subset["social_score"], subset["sleep_score"], 
                c=colors[opt], label=opt, s=80, alpha=0.7)

# 设置坐标轴
plt.xticks([1, 2, 3, 4], OPTIONS, fontsize=12)
plt.yticks([1, 2, 3, 4], OPTIONS, fontsize=12)
plt.xlabel("Social Well-being", fontsize=14, labelpad=15)
plt.ylabel("Sleep Quality", fontsize=14, labelpad=15)

# 标注正确的相关系数
plt.text(1.1, 3.7, f"Pearson Correlation\nr = {r:.3f}\np = {p:.4f}", 
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.9), fontsize=12)

plt.grid(True, alpha=0.3, linestyle="--")
plt.legend(title="Social Well-being", loc="upper left", fontsize=10)
plt.title("Social Well-being vs Sleep Quality Scatter Plot", fontsize=16, pad=20)

plt.tight_layout()
plt.show()

print("\n🎉 分析完成！图表已正确生成")