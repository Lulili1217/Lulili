import streamlit as st

# 修改标签页的文字和图标
st.set_page_config(page_title="相册", page_icon="📷")

st.title("我的相册")

# 如果图片的索引在streamlit的内存中,下面的代码将当前索引存储在内存中的ind变量中
# 把当前内存中没有ind,才需要设置为0,否则不要设置ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

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

# url:图片的地址 caption:图片注释
st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['text'])

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
#按钮框
c1, c2 = st.columns(2)
with c1:
    st.button("上一张", on_click=nextImg, use_container_width=True)
with c2:
    st.button("下一张", on_click=nextImg, use_container_width=True)