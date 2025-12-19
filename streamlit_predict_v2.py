import streamlit as st
import pickle
import pandas as pd
import os  # 仅新增：路径兼容

# 页面配置（原有逻辑，仅固定位置）
st.set_page_config(
    page_title="医疗费用预测",
    page_icon="🏥",
    layout="wide"
)

def introduce_page():
    """当选择简介页面时，将呈现该函数的内容"""
    st.write("# 欢迎使用！")
    st.sidebar.success("单击 📝 预测医疗费用")
    st.markdown("""
    # 医疗费用预测应用
    这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。

    ## 背景介绍
    - 开发目标：帮助保险公司合理定价保险产品，控制风险。
    - 模型算法：利用随机森林回归算法训练医疗费用预测模型。

    ## 使用指南
    - 输入准确完整的被保险人信息，可以得到更准确的费用预测。
    - 预测结果可以作为保险定价的重要参考，但需审慎决策。
    - 有任何问题欢迎联系我们的技术支持。

    技术支持:email：support@example.com
    """)

def predict_page():
    """当选择预测费用页面时，将呈现该函数的内容"""
    st.markdown("""
    ## 使用说明
    这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。
    - **输入信息**：在下面输入被保险人的个人信息、疾病信息等。
    - **费用预测**：应用会预测被保险人的未来医疗费用支出。
    """)

    # 运用表单和表单提交按钮（原有逻辑不变）
    with st.form('user_inputs'):
        age = st.number_input('年龄', min_value=0)
        sex = st.radio('性别', options=['男性', '女性'])
        bmi = st.number_input('BMI', min_value=0.0)
        children = st.number_input("子女数量：", step=1, min_value=0)
        smoke = st.radio("是否吸烟", ("是", "否"))
        region = st.selectbox('区域', ('东南部', '西南部', '东北部', '西北部'))
        submitted = st.form_submit_button('预测费用')
        
        if submitted:
            # 原有编码逻辑不变
            sex_female, sex_male = 0, 0
            if sex == '女性':
                sex_female = 1
            elif sex == '男性':
                sex_male = 1

            smoke_yes, smoke_no = 0, 0
            if smoke == '是':
                smoke_yes = 1
            elif smoke == '否':
                smoke_no = 1

            region_northeast, region_southeast, region_northwest, region_southwest = 0, 0, 0, 0
            if region == '东北部':
                region_northeast = 1
            elif region == '东南部':
                region_southeast = 1
            elif region == '西北部':
                region_northwest = 1
            elif region == '西南部':
                region_southwest = 1

            format_data = [age, bmi, children, sex_female, sex_male,
                           smoke_no, smoke_yes,
                           region_northeast, region_southeast, region_northwest, region_southwest]
            
            # 仅新增：路径兼容 + 异常处理（必要修改）
            model_path = os.path.join(os.getcwd(), 'rfr_model.pkl')
            try:
                with open(model_path, 'rb') as f:
                    rfr_model = pickle.load(f)
            except FileNotFoundError:
                st.error("❌ 模型文件不存在！请先执行save_model.py生成rfr_model.pkl")
                st.stop()
            
            # 原有预测逻辑不变
            format_data_df = pd.DataFrame(data=[format_data], columns=rfr_model.feature_names_in_)
            predict_result = rfr_model.predict(format_data_df)[0]
            
            # 仅优化输出格式（非必要，保留原有逻辑也可）
            st.write('根据您输入的数据，预测该客户的医疗费用是：', round(predict_result, 2))
            st.write("技术支持:email：support@example.com")

# 原有导航逻辑不变
nav = st.sidebar.radio("导航", ["简介", "预测医疗费用"])
if nav == "简介":
    introduce_page()
else:
    predict_page()