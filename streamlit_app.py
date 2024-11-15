import streamlit as st
from PIL import Image

st.title("리뷰야 알려줘!")
st.subheader("흑백요리사 :일:라운드, :red[대중]들이 심사하면 어떨까?")
st.write('네이버 지도 흑백요리사 맛집리스트의 :blue[리뷰 점수화]를 통한 :blue[평균값 도출, 순위 비교]')
st.caption("리뷰의 점수화는 GPT를 활용하였으며, **맛, 분위기, 위생, 친절함, 재방문의사**를 기준으로 책정하였습니다.")
st.divider()

tab1, tab2, tab3, tab4= st.tabs(['대중Pick:상반신_그림자:' , '친구Pick:반짝임:', '커플Pick:하트2:', '가족Pick:가족:'])
#대중Pick:상반신_그림자: 를 누르면 표시될 내용

with tab1:
  my_image1 = Image.open('/workspaces/wbc_canbe_all/picture/1.jpg')
  st.image(my_image1, use_container_width=True)
#친구Pick:반짝임:를 누르면 표시될 내용
with tab2:
  my_image2 = Image.open('/workspaces/wbc_canbe_all/picture/2.jpg')
  st.image(my_image2, use_container_width=True)
#커플Pick:하트2:를 누르면 표시될 내용
with tab3:
  my_image3 = Image.open('/workspaces/wbc_canbe_all/picture/3.jpg')
  st.image(my_image3, use_container_width=True)
#가족Pick:가족:를 누르면 표시될 내용
with tab4:
  my_image4 = Image.open('/workspaces/wbc_canbe_all/picture/4.jpg')
  st.image(my_image4, use_container_width=True)
