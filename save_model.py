import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import os  # 仅新增：路径兼容

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

# 仅新增：兼容多系统路径 + 编码容错（必要修改）
data_path = os.path.join("data", "insurance-chinese.csv")
try:
    insurance_df = pd.read_csv(data_path, encoding='gbk')
except UnicodeDecodeError:
    insurance_df = pd.read_csv(data_path, encoding='utf-8')

# 原有逻辑不变
output = insurance_df['医疗费用']
features = insurance_df[['年龄', '性别', 'BMI', '子女数量', '是否吸烟', '区域']]
features = pd.get_dummies(features)

# 仅新增：random_state保证模型可复现（必要修改）
x_train, x_test, y_train, y_test = train_test_split(
    features, output, train_size=0.8, random_state=42
)

# 仅新增：random_state保证模型可复现（必要修改）
rfr = RandomForestRegressor(random_state=42)
rfr.fit(x_train, y_train)
y_pred = rfr.predict(x_test)
r2 = r2_score(y_test, y_pred)

# 原有逻辑不变
with open('rfr_model.pkl', 'wb') as f:
    pickle.dump(rfr, f)

print(f'保存成功，已生成相关文件。模型可决系数：{r2:.4f}')