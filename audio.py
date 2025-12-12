import streamlit as st

# 页面样式信息
st.set_page_config(page_title="简易音乐", layout="centered", page_icon="🎵")
st.title("🎵 音乐")
st.caption("使用Streamlit制作的歌单播放器，支持切换和基本信息展示")

# 歌曲索引
if 'song_idx' not in st.session_state:
    st.session_state.song_idx = 0

# 歌曲数据
songs = [
    {
        "name": "Bohemian Rhapsody",
        "singer": "Queen",
        "album_img": "https://ts1.tc.mm.bing.net/th/id/R-C.fad381bdc2f47ea8c3ceeee8139eed74?rik=X%2fbngK8VpR9RIQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20122%2f791%2fw396h395%2f20250426%2f1179-gif4f736820d1a436a85abf12925e5c4ba6.gif&ehk=9DdWXYCkmxlTfgSxq9wJ7dJCyOnZ3GN3eeH3ImhnS38%3d&risl=&pid=ImgRaw&r=0",
        "duration": "5:55"
    },
    {
        "name": "Shape of You",
        "singer": "Ed Sheeran",
        "album_img": "https://ts1.tc.mm.bing.net/th/id/R-C.1722f655fa70610d70b106f4d5b3fa2d?rik=oDxILgmidHOj6A&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20122%2f786%2fw392h394%2f20250426%2fa5af-gif945446f5db7a845a41183bcfbc53f693.gif&ehk=UzeEXm%2fVcotKhZZIZv628FOo7ZkyXHN%2bHrxh9TrtpSU%3d&risl=&pid=ImgRaw&r=0",
        "duration": "3:53"
    },
    {
        "name": "Yesterday",
        "singer": "The Beatles",
        "album_img": "https://ts1.tc.mm.bing.net/th/id/R-C.98f1c310728cb76ea2d6834dc27e1af3?rik=2zBdrk5zUwg%2fMQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20111%2f4%2fw400h404%2f20250318%2fd929-gif091047c85349ecdb8d6cecdc211110be.gif&ehk=w0GA%2b10ZuMbrNn7LwraoU%2fhYxPfTXRGS8ns%2f5vWlr5w%3d&risl=&pid=ImgRaw&r=0",
        "duration": "2:03"
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
# 读取音频URL
audio_file = 'https://music.163.com/song/media/outer/url?id=5257138.mp3'

st.audio(audio_file)
