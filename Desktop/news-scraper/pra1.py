import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = "https://agw.cdp.yna.co.kr/rec/rec0601?size=10&ifid=MNS_CDP_13605&section=%EB%A9%94%EC%9D%B8"
results=[]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
resp=requests.get(url, headers=headers)
resp.raise_for_status()              # 200~299 시 진행 그외 값인 경우에 오류발생
data = resp.json()  # json 데이터형태로 변환 , 딕셔너리 형태로 변환됨 문자열로 받을 경우 일일이 json.lads()를 쓰거나 split?regex로 직접 파싱해야함
results= data['results']

Result = [None] * 10  

for i in range(10):  # 0부터 9까지
    import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = "https://agw.cdp.yna.co.kr/rec/rec0601?size=10&ifid=MNS_CDP_13605&section=%EB%A9%94%EC%9D%B8"
results=[]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
resp=requests.get(url, headers=headers)
resp.raise_for_status()              # 200~299 시 진행 그외 값인 경우에 오류발생
data = resp.json()  # json 데이터형태로 변환 , 딕셔너리 형태로 변환됨 문자열로 받을 경우 일일ㅎ이 json.lads()를 쓰거나 split?regex로 직접 파싱해야함
results= data['results']

titles ,dates ,  = [None] * 10 , [None] * 10 # 튜플형식 

for i in range(10):  # 0부터 9까지
    titles[i] = results[i]["cr_title"]
    dates[i] = results[i]["cr_ddt"]
   
df= pd.DataFrame(
    {'title' : titles
     ,'dates': dates} # pandas는 딕셔너리형태로 열 중심으로 데이터를 주고 딕셔너리의 key는 한 행을 담당하고 value는 그 리스트의 인덱스 0부터 차례대로 열로 들어간다
                  ) 
output_path = 't2.xlsx'
df.to_excel(output_path, index=False, sheet_name='sheet1')