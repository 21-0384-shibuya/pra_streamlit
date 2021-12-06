# from typing import Collection
import streamlit as st
# import numpy as np
# import pandas as pd
import time as time
# from PIL import Image

st.title('Streamlit超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration =st.empty()
bar=st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

st.write('DataFlame')
#緯度経度の指定で地図上にプロットすることができる
# df = pd.DataFrame(
#   np.random.rand(100,2)/[50,50]+[35.69,139.70],
#   columns=['lat','lon']
# )

#dataframeは表示する表の大きさを引数で指定可能,ハイライトの挿入できる
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df)#ソートができない様な静的な表の表示
# st.write(df)
#APIreferenceの中により多く載っている
# st.write('display image')
# if st.checkbox('Show Image'):
#   img =Image.open('path63.png')
#   st.image(img,caption='ksksk',use_column_width = True)
st.write('Interactive Widget')

left_column,right_column = st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右からむです')

expander=st.expander('問合せ1')
expander.write('問合せ内容1')
expander=st.expander('問合せ2')
expander.write('問合せ内容2')
expander=st.expander('問合せ3')
expander.write('問合せ内容3')
# text = st.text_input('あなたの趣味を教えてください .')
# condition=st.slider('あなたの今の調子は？',0,100,50)
# 'あなたの趣味：', text 
# 'Condition :',condition
  #1~10のリストを作成
#   list(range(1,10))
# )
# option = st.selectbox(
#   'あなたが好きな数字を教えてください',
#   #1~10のリストを作成
#   list(range(1,10))
# )
# 'あなたが好きな数字は',option,'です'

