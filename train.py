import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder  
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# 1. 读取并修正数据（先校验列数，再适配列名）
df = pd.read_csv("student_data_adjusted_rounded.csv")

# 打印列数，方便排查（运行后可查看CSV实际有多少列）
print(f"CSV文件实际列数：{df.shape[1]}")
print(f"原始列名：{df.columns.tolist()}")

# 适配不同列数的情况（优先匹配CSV实际列数）
if df.shape[1] == 8:
    # 若CSV有8列（包含学号），列名对应：学号、性别、专业、每周学习时长、出勤率、期中、作业完成率、期末
    df.columns = ["学号", "性别", "专业", "每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率", "期末考试分数"]
elif df.shape[1] == 7:
    # 若CSV只有7列（无学号），列名对应：性别、专业、每周学习时长、出勤率、期中、作业完成率、期末
    df.columns = ["性别", "专业", "每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率", "期末考试分数"]
else:
    raise ValueError(f"CSV列数异常！当前列数：{df.shape[1]}，请检查数据文件")

df = df.dropna()  # 删除缺失值
print(f"清洗后数据行数：{df.shape[0]}")

# 2. 定义特征（X）和目标（y）
# 特征排除学号（无预测价值），仅选：性别、专业、每周学习时长、出勤率、期中分数、作业完成率
X = df[["性别", "专业", "每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率"]]
y = df["期末考试分数"]

# 3. 特征预处理流水线（分类特征编码+数值特征保留）
preprocessor = ColumnTransformer(
    transformers=[
        # 性别、专业用OneHotEncoder（drop="first"避免多重共线性）
        ("cat_encoder", OneHotEncoder(drop="first", sparse_output=False), [0, 1]),
        # 数值特征（时长、出勤率、期中、作业完成率）直接保留
        ("num_passthrough", "passthrough", [2, 3, 4, 5])
    ]
)

# 4. 构建模型流水线（预处理+线性回归）
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# 5. 训练并评估模型
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_pipeline.fit(X_train, y_train)

# 评估模型性能（MSE越小、R²越接近1越好）
y_pred = model_pipeline.predict(X_test)
print(f"模型均方误差（MSE）：{mean_squared_error(y_test, y_pred):.2f}")
print(f"模型决定系数（R²）：{r2_score(y_test, y_pred):.2f}")

# 6. 保存模型和专业列表（用于预测界面下拉框）
joblib.dump(model_pipeline, "score_prediction_model.pkl")
joblib.dump(df["专业"].unique().tolist(), "majors_list.pkl")
print("模型与专业列表已保存至当前目录")
