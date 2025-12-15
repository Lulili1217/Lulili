import streamlit as st
st.set_page_config(page_title="电影世界",page_icon='🎥')
st.title("海绵宝宝")

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

# 判断内存中有没有ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.video(video_arr[st.session_state['ind']]['url'], autoplay=True)

def play(i):
    st.session_state['ind'] = int(i)
#创建一行5个列容器
cols = st.columns(5)
#遍历视频列表，将按钮放入列中
for i in range(len(video_arr)):
    with cols[i]:  # 每个按钮对应一个列
        st.button('第' + str(i + 1) + '集', use_container_width=True, on_click=play, args=[i])
st.text('《海绵宝宝》（SpongeBob SquarePants）是一部由史蒂芬·海伦伯格原创，舍曼·科恩、沃特·杜赫、山姆·亨德森、保罗·蒂比特、沃尔特·道恩 [21]等导演，汤姆·肯尼、比尔·法格巴克、罗杰·布帕斯等配音的美国喜剧动画，于1999年7月17日在尼克国际儿童频道开播。')