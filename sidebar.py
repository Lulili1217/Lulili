import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 全局页面配置（只能有一个，放在最前面）
st.set_page_config(
    page_title="多功能选项卡示例",
    page_icon="📋",
    layout="wide"
)

st.title("选项卡简单示例")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["选项卡1", "选项卡2", "选项卡3", "选项卡4", "选项卡5", "选项卡6"])

# 选项卡1：学生数字档案
with tab1:
    st.title('--学生 小陆👧-数字档案')
    st.header('📝基础信息')
    st.markdown('学生ID: NEO-2023-001')
    st.markdown('注册时间: :green[2023-10-01 08:30:17]|精神状态:正常')
    st.markdown('当前教室: :green[实训楼301]|安全等级: :green[绝密]')
    
    st.header('🛠️技能矩阵')
    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言", value="95℃", delta="2%")
    c2.metric(label="python", value="87%", delta="-1%")
    c3.metric(label="java", value="68%", delta="-10%")
    
    # 制作进度条
    st.subheader('Streamlit课程进度')
    st.text('Streamlit课程进度')
    st.progress(0.6)

    # 任务日志
    st.header("任务日志🚩")
    # 写数据，制作成表
    data = {
        '任务': ["学生数字档案", "课程管理系统", "数据图表展示"],
        '状态': ["完成😀", "进行中😅", "未完成😭"],
        '难度': ["🥰", "😟", "🙁"],
    }
    ind = pd.Series(['01月', '02月', '03月'], name='日期')
    df = pd.DataFrame(data, index=ind)
    st.dataframe(df)
    
    st.header("最新代码成果")
    st.caption("python代码")
    python_code = '''def hello():
    print("你好，Streamlit！")
    aaa
    ccc
    ccc
'''
    # 展示代码和列数
    st.code(python_code, line_numbers=True)

    st.markdown(':green[>>>system message:] 下个任务已解锁')
    st.markdown(':green[>>>system message:] 下个任务已解锁')
    st.markdown(':green[>>>system message:] 下个任务已解锁')

# 选项卡2：餐厅数据可视化
with tab2:
    st.header("门店数据与可视化分析")
    
    # 餐厅评分-条形图
    st.subheader("🍽️ 餐厅评分分析")
    # 定义数据
    data = {
        '门店': ['星怡会尝不忘', '老友粉', '高峰柠檬鸭', '好友缘', '西冷牛排店'],
        '评分': [4.5, 4.2, 4.8, 4.7, 4.5],
    }
    df = pd.DataFrame(data, index=pd.Series([1,2,3,4,5], name='序号'))
    st.write("门店评分数据")
    st.dataframe(df)
    
    st.subheader("设置x参数")
    st.bar_chart(df, x='门店')
    
    # 修改df，用门店列作为索引
    df_set = df.set_index('门店', drop=True)
    st.subheader("设置y参数")
    st.bar_chart(df_set, y='评分')
    
    st.subheader("设置宽度和高度")
    st.bar_chart(df_set, width=400, height=300, use_container_width=False)

    st.divider()
    
    # 餐厅价格-折线图
    st.subheader("💰 餐厅价格分析")
    data_price = {
        '门店': ['星怡会尝不忘', '老友粉', '高峰柠檬鸭', '好友缘', '西冷牛排店'],
        '价格': [6, 7, 8, 7, 15],
    }
    df_price = pd.DataFrame(data_price, index=pd.Series([1,2,3,4,5], name='序号'))
    st.write("门店价格数据")
    st.dataframe(df_price)
    
    st.subheader("设置x参数")
    st.line_chart(df_price, x='门店')
    
    df_price_set = df_price.set_index('门店', drop=True)
    st.subheader("设置y参数")
    st.line_chart(df_price_set, y='价格')
    
    st.subheader("设置宽度和高度")
    st.line_chart(df_price_set, width=300, height=300, use_container_width=False)

    st.divider()
    
    # 用餐高峰时段-面积图
    st.subheader("⏰ 用餐高峰时段分析")
    data_time = {
        '时间': [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        '星怡会尝不忘': [200, 150, 180, 300, 200, 100, 120, 80, 200, 400, 300, 200, 100, 120, 50],
        '老友粉': [120, 160, 123, 300, 200, 100, 120, 80, 200, 400, 120, 200, 100, 120, 50],
        '高峰柠檬鸭': [110, 100, 160, 300, 200, 100, 120, 80, 200, 300, 300, 200, 100, 120, 50],
        '好友缘': [110, 100, 160, 300, 200, 100, 120, 80, 200, 300, 300, 200, 100, 120, 50],
        '西冷牛排店': [120, 160, 123, 300, 200, 100, 120, 80, 150, 400, 300, 200, 100, 120, 50]
    }
    df_time = pd.DataFrame(data_time, index=pd.Series(range(1,16), name='序号'))
    st.write("时段客流数据")
    st.dataframe(df_time)
    
    st.subheader("设置x参数")
    st.area_chart(df_time, x='时间')
    
    df_time_set = df_time.set_index('时间', drop=True)
    st.subheader("单门店数据")
    st.area_chart(df_time_set, y='星怡会尝不忘')
    
    st.subheader("多门店对比")
    st.area_chart(df_time_set, y=['老友粉', '高峰柠檬鸭', '好友缘', '西冷牛排店'])
    
    st.subheader("设置宽度和高度")
    st.area_chart(df_time_set, width=300, height=300, use_container_width=False)

    st.divider()
    
    # 餐厅位置-地图
    st.subheader("🗺️ 餐厅位置分布")
    data_location = {
        '门店': ['星怡会尝不忘', '老友粉', '高峰柠檬鸭', '好友缘', '西冷牛排店'],
        '纬度': [22.853838, 22.863838, 22.873838, 22.893838, 22.823838],
        '经度': [108.222177, 108.232177, 108.252177, 108.272177, 108.282177],
    }
    df_location = pd.DataFrame(data_location)
    st.write("门店位置数据")
    st.dataframe(df_location)
    
    map_data = {
        "latitude": [22.853838, 22.863838, 22.873838, 22.893838, 22.823838],
        "longitude": [108.222177, 108.232177, 108.252177, 108.272177, 108.282177]
    }
    mp_df = pd.DataFrame(map_data)
    st.map(mp_df, zoom=11)

# 选项卡3：图片相册
with tab3:
    st.title("📷 我的相册")

    # 初始化图片索引
    if 'img_ind' not in st.session_state:
        st.session_state['img_ind'] = 0

    images = [
        {
            'url': "https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg",
            'text': '猫'
        },
        {
            'url': "https://cdn.britannica.com/82/232782-050-8062ACFA/Black-labrador-retriever-dog.jpg",
            'text': '狗'
        },
        {
            'url': "https://live.staticflickr.com/2686/4497672316_d283310530_3k.jpg",
            'text': '狮子'
        }
    ]

    # 显示当前图片
    st.image(images[st.session_state['img_ind']]['url'], 
             caption=images[st.session_state['img_ind']]['text'],
             width=600)

    # 切换图片函数
    def prev_img():
        st.session_state['img_ind'] = (st.session_state['img_ind'] - 1) % len(images)
    
    def next_img():
        st.session_state['img_ind'] = (st.session_state['img_ind'] + 1) % len(images)
    
    # 按钮布局
    c1, c2 = st.columns(2)
    with c1:
        st.button("上一张", on_click=prev_img, use_container_width=True)
    with c2:
        st.button("下一张", on_click=next_img, use_container_width=True)

# 选项卡4：音乐播放器
with tab4:
    st.title("🎵 音乐播放器")
    st.caption("使用Streamlit制作的歌单播放器，支持切换和基本信息展示")

    # 初始化歌曲索引
    if 'song_idx' not in st.session_state:
        st.session_state.song_idx = 0

    # 歌曲数据
    songs = [
        {
            "name": "Bohemian Rhapsody",
            "singer": "Queen",
            "album_img": "https://ts1.tc.mm.bing.net/th/id/R-C.fad381bdc2f47ea8c3ceeee8139eed74?rik=X%2fbngK8VpR9RIQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20122%2f791%2fw396h395%2f20250426%2f1179-gif4f736820d1a436a85abf12925e5c4ba6.gif&ehk=9DdWXYCkmxlTfgSxq9wJ7dJCyOnZ3GN3eeH3ImhnS38%3d&risl=&pid=ImgRaw&r=0",
            "duration": "5:55",
            "url": "https://music.163.com/song/media/outer/url?id=5257138.mp3"
        },
        {
            "name": "Shape of You",
            "singer": "Ed Sheeran",
            "album_img": "https://ts1.tc.mm.bing.net/th/id/R-C.1722f655fa70610d70b106f4d5b3fa2d?rik=oDxILgmidHOj6A&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20122%2f786%2fw392h394%2f20250426%2fa5af-gif945446f5db7a845a41183bcfbc53f693.gif&ehk=UzeEXm%2fVcotKhZZIZv628FOo7ZkyXHN%2bHrxh9TrtpSU%3d&risl=&pid=ImgRaw&r=0",
            "duration": "3:53",
            "url": "https://music.163.com/song/media/outer/url?id=467772038.mp3"
        },
        {
            "name": "Yesterday",
            "singer": "The Beatles",
            "album_img": "https://ts1.tc.mm.bing.net/th/id/R-C.98f1c310728cb76ea2d6834dc27e1af3?rik=2zBdrk5zUwg%2fMQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20111%2f4%2fw400h404%2f20250318%2fd929-gif091047c85349ecdb8d6cecdc211110be.gif&ehk=w0GA%2b10ZuMbrNn7LwraoU%2fhYxPfTXRGS8ns%2f5vWlr5w%3d&risl=&pid=ImgRaw&r=0",
            "duration": "2:03",
            "url": "https://music.163.com/song/media/outer/url?id=18324517.mp3"
        }
    ]

    # 切换歌曲函数
    def prev_song():
        st.session_state.song_idx = (st.session_state.song_idx - 1) % len(songs)

    def next_song():
        st.session_state.song_idx = (st.session_state.song_idx + 1) % len(songs)

    # 当前歌曲信息
    current_song = songs[st.session_state.song_idx]

    # 布局
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(current_song["album_img"], width=180)
    with col2:
        st.subheader(current_song["name"])
        st.write(f"歌手: {current_song['singer']}")
        st.write(f"时长: {current_song['duration']}")

    # 切换按钮
    col_prev, col_next = st.columns(2)
    with col_prev:
        st.button("◀ 上一首", on_click=prev_song, use_container_width=True)
    with col_next:
        st.button("下一首 ▶", on_click=next_song, use_container_width=True)
    
    # 音频播放
    st.audio(current_song["url"], format="audio/mp3")

# 选项卡5：视频播放器
with tab5:
    st.title("🎥 海绵宝宝视频集")

    video_arr = [
        {
            'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
            'title': '海绵宝宝_第1集'
        },
        {
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '海绵宝宝_第2集'
        },
        {
            'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
            'title': '海绵宝宝_第3集'
        },
        {
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '海绵宝宝_第4集'
        },
        {
            'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
            'title': '海绵宝宝_第5集'
        }
    ]

    # 初始化视频索引（使用不同的session key避免冲突）
    if 'video_ind' not in st.session_state:
        st.session_state['video_ind'] = 0

    # 显示当前视频
    st.video(video_arr[st.session_state['video_ind']]['url'], autoplay=False)

    # 播放函数
    def play_video(i):
        st.session_state['video_ind'] = int(i)
    
    # 创建一行5个列容器
    cols = st.columns(5)
    # 遍历视频列表，将按钮放入列中
    for i in range(len(video_arr)):
        with cols[i]:  # 每个按钮对应一个列
            st.button(f'第{i + 1}集', use_container_width=True, on_click=play_video, args=[i])
    
    # 剧情介绍
    st.divider()
    st.info('《海绵宝宝》（SpongeBob SquarePants）是一部由史蒂芬·海伦伯格原创，舍曼·科恩、沃特·杜赫、山姆·亨德森、保罗·蒂比特、沃尔特·道恩 等导演，汤姆·肯尼、比尔·法格巴克、罗杰·布帕斯等配音的美国喜剧动画，于1999年7月17日在尼克国际儿童频道开播。')

# 选项卡6：个人简历生成器
with tab6:
    st.title("📝 个人简历生成器")
    st.divider()

    # 左右比例1：2
    c1, c2 = st.columns([1, 2])

    with c1:
        st.subheader("信息填写")

        # 单行文本输入框
        name = st.text_input("姓名")
        job_title = st.text_input("意向职位")
        phone = st.text_input("联系电话")
        email = st.text_input("电子邮箱")
        location = st.text_input("现居地址")

        # 单选按钮radio
        gender = st.radio("性别", ["男", "女", "其他"], horizontal=True)

        # 日期选择组件
        birth_date = st.date_input(
            "出生日期",
            value=datetime(1995, 1, 1),
            min_value=datetime(1990, 1, 1),
            max_value=datetime(2025, 12, 31)
        )
        age = datetime.now().year - birth_date.year

        # 下拉按钮selectbox
        education = st.selectbox("最高学历", ["高中/中专", "专科", "本科", "硕士", "博士"])
        work_exp = st.selectbox("工作经验", ["应届生", "0-1年", "1-3年", "3-5年", "5年以上"])
        work_place = st.selectbox("意向工作地点", ["北京", "上海", "广州", "深圳", "其他"])

        # 多选下拉按钮multiselect
        skills = st.multiselect("掌握技能", ["Python", "Java", "SQL", "前端开发", "数据分析", "项目管理"])

        # 复选框checkbox
        has_project = st.checkbox("是否有项目经验")

        # 范围选择滑块组件
        salary_range = st.slider(
            "期望薪资范围（月薪）",
            min_value=3000,
            max_value=50000,
            value=(10000, 20000)
        )

        # 数字输入组件
        project_count = st.number_input("项目经验数量", min_value=0, max_value=20, value=2)

        # 时间选择组件
        available_time = st.time_input(
            "可到岗时间",
            value=datetime.strptime("09:00", "%H:%M")
        )

        # 多行文本输入框
        intro = st.text_area("个人简介", placeholder="介绍你的专业背景和优势...", height=120)

        # 照片上传
        st.divider()
        st.markdown("**头像上传**")
        avatar_file = st.file_uploader(
            "选择头像图片",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

        # 普通按钮button（放在上传后面，避免保存时还没上传）
        if st.button("保存信息"):
            st.success("信息已保存！")
            if avatar_file:
                st.success("头像已同步保存 ✅")

    with c2:
        st.subheader("简历实时预览")
        st.divider()

        # 预览卡片
        with st.container(border=True):
            avatar_col, info_col = st.columns([1, 4], gap="small")
            with avatar_col:
                if avatar_file:
                    st.image(avatar_file, width=100, caption="个人头像")
                else:
                    st.image("https://via.placeholder.com/100", width=100, caption="未上传头像")
            with info_col:
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