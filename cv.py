import streamlit as st
from datetime import datetime

st.set_page_config(page_title="个人简历生成器", layout="wide")
st.title("📝 个人简历生成器")
st.divider()

# 列比例：左1右2（使用width参数替代已废弃的column_width）
c1, c2 = st.columns([1, 2])

with c1:
    st.subheader("信息填写")

    # （八）单行文本输入框
    name = st.text_input("姓名")
    job_title = st.text_input("意向职位")
    phone = st.text_input("联系电话")
    email = st.text_input("电子邮箱")
    location = st.text_input("现居地址")

    # （二）单选按钮radio
    gender = st.radio("性别", ["男", "女", "其他"], horizontal=True)

    # （十一）日期选择组件
    birth_date = st.date_input(
        "出生日期",
        value=datetime(1995, 1, 1),
        min_value=datetime(1990, 1, 1),
        max_value=datetime(2025, 12, 31)
    )
    age = datetime.now().year - birth_date.year

    # （四）下拉按钮selectbox
    education = st.selectbox("最高学历", ["高中/中专", "专科", "本科", "硕士", "博士"])
    work_exp = st.selectbox("工作经验", ["应届生", "0-1年", "1-3年", "3-5年", "5年以上"])
    work_place = st.selectbox("意向工作地点", ["北京", "上海", "广州", "深圳", "其他"])

    # （五）多选下拉按钮multiselect
    skills = st.multiselect("掌握技能", ["Python", "Java", "SQL", "前端开发", "数据分析", "项目管理"])

    # （三）复选框checkbox
    has_project = st.checkbox("是否有项目经验")

    # （七）范围选择滑块组件
    salary_range = st.slider(
        "期望薪资范围（月薪）",
        min_value=3000,
        max_value=50000,
        value=(10000, 20000)
    )

    # （九）数字输入组件
    project_count = st.number_input("项目经验数量", min_value=0, max_value=20, value=2)

    # （十二）时间选择组件
    available_time = st.time_input(
        "可到岗时间",
        value=datetime.strptime("09:00", "%H:%M")
    )

    # （十）多行文本输入框
    intro = st.text_area("个人简介", placeholder="介绍你的专业背景和优势...", height=120)

    # （一）普通按钮button
    if st.button("保存信息"):
        st.success("信息已保存！")
        if 'avatar_file' in locals() and avatar_file:
            st.success("头像已同步保存 ✅")

    # 照片上传放到最下面
    st.divider()
    st.markdown("**头像上传**")
    avatar_file = st.file_uploader(
        "选择头像图片",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )


with c2:
    st.subheader("简历实时预览")
    st.divider()

    # 预览卡片
    with st.container(border=True):
        # 修复头像+信息布局（使用width参数替代column_width）
        avatar_col, info_col = st.columns([1, 4], gap="small")
        with avatar_col:
            if 'avatar_file' in locals() and avatar_file:
                st.image(avatar_file, width=100, caption="个人头像")
            else:
                st.image("https://via.placeholder.com/100", width=100, caption="未上传头像")
        with info_col:
            # 修复联系方式显示为空的问题
            st.markdown(f"### {name if name else '未填写姓名'}")
            st.markdown(f"**意向职位**：{job_title if job_title else '未填写'}")
            contact_text = []
            if phone:
                contact_text.append(phone)
            if email:
                contact_text.append(email)
            st.markdown(f"**联系方式**：{' | '.join(contact_text) if contact_text else '未填写'}")
        
        st.divider()

        # 基础信息
        st.markdown("#### 基础信息")
        col_info1, col_info2 = st.columns(2)
        with col_info1:
            st.write(f"性别：{gender}")
            st.write(f"年龄：{age}岁（{birth_date.strftime('%Y-%m-%d')}）")
            st.write(f"学历：{education}")
        with col_info2:
            st.write(f"工作经验：{work_exp}")
            st.write(f"现居地址：{location if location else '未填写'}")
            st.write(f"意向地点：{work_place}")

        # 求职信息
        st.markdown("#### 求职期望")
        st.write(f"期望薪资：{salary_range[0]} - {salary_range[1]} 元/月")
        st.write(f"可到岗时间：{available_time.strftime('%H:%M')}")
        st.write(f"项目经验：{'有' if has_project else '无'}（共{project_count}个项目）")
        st.write(f"掌握技能：{', '.join(skills) if skills else '未填写'}")

        # 个人简介
        st.markdown("#### 个人简介")
        st.write(intro if intro else "暂无简介")