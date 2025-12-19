import streamlit as st
import pickle
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# ===================== 基础配置 =====================
# 设置页面标题、图标和布局
st.set_page_config(
    page_title="企鹅分类器",
    page_icon=":penguin:",
    layout='wide'
)

# 定义路径兼容函数（适配Windows/Linux）
def get_file_path(file_name, sub_dir=""):
    """获取文件路径，兼容不同系统"""
    if sub_dir:
        return os.path.join(os.getcwd(), sub_dir, file_name)
    return os.path.join(os.getcwd(), file_name)

# ===================== 侧边栏 =====================
with st.sidebar:
    # 图片加载容错
    try:
        st.image(get_file_path("right_logo.png", "images"), width=100)
    except:
        st.warning("侧边栏logo图片未找到，使用文字替代")
        st.markdown("🐧 企鹅分类器")
    
    st.title('请选择页面')
    page = st.selectbox(
        "请选择页面", 
        ["简介页面", "预测分类页面"], 
        label_visibility='collapsed'
    )

# ===================== 简介页面 =====================
if page == "简介页面":
    st.title("企鹅分类器:penguin:")
    st.header('数据集介绍')
    st.markdown("""
    帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，
    也可以作为机器学习入门练习。
    该数据集是由 Gorman 等收集，并发布在一个名为 palmerpenguins 的 R 语言包，
    以对南极企鹅种类进行分类和研究。
    该数据集记录了 344 行观测数据，包含 3 个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和帽带企鹅的各种信息。
    """)
    
    st.header('三种企鹅的卡通图像')
    # 图片加载容错
    try:
        st.image(get_file_path("penguins.png", "images"), use_column_width=True)
    except:
        st.warning("企鹅卡通图片未找到")
        st.markdown("### 企鹅物种：阿德利企鹅、巴布亚企鹅、帽带企鹅")

# ===================== 预测分类页面 =====================
elif page == "预测分类页面":
    st.header("预测企鹅分类")
    st.markdown("""
    这个Web应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入6个信息，
    就可以预测企鹅的物种，使用下面的表单开始预测吧！
    """)

    # 3:1:2 列布局
    col_form, col, col_logo = st.columns([3, 1, 2])

    with col_form:
        # 表单收集用户输入
        with st.form('user_inputs'):
            island = st.selectbox('企鹅栖息的岛屿', options=['托尔森岛', '比斯科群岛', '德里姆岛'])
            sex = st.selectbox('性别', options=['雄性', '雌性'])
            bill_length = st.number_input('喙的长度（毫米）', min_value=0.0, max_value=100.0, value=40.0)
            bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0, max_value=50.0, value=15.0)
            flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0, max_value=300.0, value=200.0)
            body_mass = st.number_input('身体质量（克）', min_value=0.0, max_value=10000.0, value=4000.0)
            submitted = st.form_submit_button('预测分类')

            # ===================== 数据编码 =====================
            # 初始化岛屿变量
            island_biscoe, island_dream, island_torgerson = 0, 0, 0
            if island == '比斯科群岛':
                island_biscoe = 1
            elif island == '德里姆岛':
                island_dream = 1
            elif island == '托尔森岛':
                island_torgerson = 1

            # 初始化性别变量
            sex_female, sex_male = 0, 0
            if sex == '雌性':
                sex_female = 1
            elif sex == '雄性':
                sex_male = 1

            # 格式化输入数据
            format_data = [
                bill_length, bill_depth, flipper_length, body_mass,
                island_dream, island_torgerson, island_biscoe, sex_male, sex_female
            ]

            # ===================== 模型加载与预测 =====================
            predict_result_species = ""
            if submitted:
                # 校验输入数据
                if all(v == 0 for v in [bill_length, bill_depth, flipper_length, body_mass]):
                    st.error("请输入有效的企鹅特征数据，不能全为0！")
                else:
                    try:
                        # 加载模型和映射关系
                        with open(get_file_path("rfc_model.pkl"), 'rb') as f:
                            rfc_model = pickle.load(f)
                        with open(get_file_path("output_uniques.pkl"), 'rb') as f:
                            output_uniques_map = pickle.load(f)

                        # 构造DataFrame保证特征列匹配
                        format_data_df = pd.DataFrame(
                            data=[format_data],
                            columns=rfc_model.feature_names_in_
                        )
                        
                        # 模型预测
                        predict_result_code = rfc_model.predict(format_data_df)
                        predict_result_species = output_uniques_map[predict_result_code[0]]
                        
                        # 输出结果
                        st.success(f'✅ 预测结果：该企鹅的物种是 → **{predict_result_species}**')
                        
                    except FileNotFoundError as e:
                        st.error(f"❌ 模型文件缺失：{e}")
                        st.info("请先运行save_model.py生成rfc_model.pkl和output_uniques.pkl文件")
                    except Exception as e:
                        st.error(f"❌ 预测出错：{str(e)}")

    # ===================== 右侧图片展示区 =====================
    with col_logo:
        if not submitted:
            # 初始显示logo
            try:
                st.image(get_file_path("right_logo.png", "images"), width=300)
            except:
                st.markdown("### 🐧 等待您的预测...")
        else:
            # 预测后显示对应物种图片
            if predict_result_species:
                try:
                    st.image(get_file_path(f"{predict_result_species}.png", "images"), width=300)
                except:
                    st.warning(f"未找到{predict_result_species}的图片")
                    st.markdown(f"### 🐧 {predict_result_species}")