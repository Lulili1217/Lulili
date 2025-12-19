import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

# 读取数据集，并将字符编码指定为gbk，防止中文报错
insurance_df = pd.read_csv('data/insurance-chinese.csv', encoding='gbk')

# 将医疗费用定义为目标输出变量
output = insurance_df['医疗费用']

# 使用年龄、性别、BMI、子女数量、是否吸烟、区域作为特征列
features = insurance_df[['年龄', '性别', 'BMI', '子女数量', '是否吸烟', '区域']]

# 对特征列进行独热编码
features = pd.get_dummies(features)

# 划分训练集（80%）和测试集（20%）
x_train, x_test, y_train, y_test = train_test_split(features, output, train_size=0.8)

# 构建随机森林回归模型
rfr = RandomForestRegressor()

# 训练模型
rfr.fit(x_train, y_train)

# 预测测试集
y_pred = rfr.predict(x_test)

# 计算可决系数（R-squared）
r2 = r2_score(y_test, y_pred)

print(f'该模型的可决系数（R-squared）是：{r2}')