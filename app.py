import urllib
import streamlit as st
import pendulum as pdlm
from io import StringIO
from contextlib import contextmanager, redirect_stdout
import taixuanshifa

@contextmanager
def st_capture(output_func):
    with StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write
        def new_write(string):
            ret = old_write(string)
            output_func(stdout.getvalue())
            return ret
        stdout.write = new_write
        yield
        
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/kentang2017/taixuanshifa/master/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

def get_file_content_as_string1(path):
    url = 'https://raw.githubusercontent.com/kentang2017/kinliuren/master/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

st.set_page_config(layout="wide",page_title="堅太玄 - 太玄筮法排盘")
pan,guji,links = st.tabs([' 排盤 ', ' 古籍 ',' 連結 ' ])
with st.sidebar:
    pp_date=st.date_input("日期",pdlm.now(tz='Asia/Shanghai').date())
    pp_time=st.time_input("時間",pdlm.now(tz='Asia/Shanghai').time())
    p = str(pp_date).split("-")
    pp = str(pp_time).split(":")
    y = int(p[0])
    m = int(p[1])
    d = int(p[2])
    h = int(pp[0])
    min = int(pp[1])
   
with links:
    st.header('連結')
    st.markdown(get_file_content_as_string1("update.md"),  unsafe_allow_html=True)
    
with pan:
    st.header('堅太玄')
    pan = taixuanshifa.Taixuan(y,m,d,h).pan()
    output = st.empty()
    with st_capture(output.code):
        print(pan)
