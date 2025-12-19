import streamlit as st
import pickle

# 加载训练好的随机森林模型
with open('rfc_model.pkl', 'rb') as f:
    rfc_model = pickle.load(f)

# 加载目标输出变量的映射关系
with open('output_uniques.pkl', 'rb') as f:
    output_uniques_map = pickle.load(f)

st.subheader('随机森林模型')
st.write(rfc_model)
st.subheader('映射关系示例')
st.write('"1" 应该对应 "巴布亚企鹅"')
st.write(output_uniques_map[1])