import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 数据读取与预处理
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
penguin_df.dropna(inplace=True)
output = penguin_df['企鹅的种类']
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
features = pd.get_dummies(features)
output_codes, output_uniques = pd.factorize(output)

# 划分数据集并训练模型
x_train, x_test, y_train, y_test = train_test_split(
    features, output_codes, train_size=0.8, random_state=42
)
rfc = RandomForestClassifier(random_state=42)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
score = accuracy_score(y_test, y_pred)
print(f'模型准确率：{score}')

# 保存模型和映射关系
with open('rfc_model.pkl', 'wb') as f:
    pickle.dump(rfc, f)
with open('output_uniques.pkl', 'wb') as f:
    pickle.dump(output_uniques, f)

print('保存成功，已生成相关文件。')