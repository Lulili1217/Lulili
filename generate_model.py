import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 读取数据集，并将字符编码指定为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

# 删除缺失值所在的行
penguin_df.dropna(inplace=True)

# 将企鹅的种类定义为目标输出变量
output = penguin_df['企鹅的种类']

# 使用企鹅栖息的岛屿、喙的长度、喙的深度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]

# 对特征列进行独热编码
features = pd.get_dummies(features)

# 将目标输出变量转换为离散数值
output_codes, output_uniques = pd.factorize(output)

# 划分训练集（80%）和测试集（20%）
x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

# 构建随机森林分类器
rfc = RandomForestClassifier()

# 训练模型
rfc.fit(x_train, y_train)

# 预测测试集
y_pred = rfc.predict(x_test)

# 计算准确率
score = accuracy_score(y_test, y_pred)

print(f'该模型的准确率是：{score}')