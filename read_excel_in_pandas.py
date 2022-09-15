"""
1. 필요한 패키지를 importing 과정
2. 엑셀파일에서 필요한 데이터 읽어온다.
3. 원하는 정보만 필터링하여 남긴다.
4. 원하는 정보만 출력한다.
"""

#1. -----------------------------------------
# pandas를 import한다.
import pandas as pd

#2. ----------- reading excel file
# FDF선벙장 EXCEL 파일을 읽어서 변수 df에 저장합니다. (df : dataframe양자)
df = pd.read_excel('FDF선번장 연결정보.xlsx')

# df의 컬럼명 : 엑셒파일에서 제목행
# 엑셀에서 제목행이라 함음 첫번째 행을 말한다.
# read_excel, read_csv할때 제목행 지정도 가능하고, skip
print(df.columns)

# head, tail  --> df의 개략적인 모습을 파악목적, 앞에서 5줄, 뒤에서 5줄을 보여준다.
df.head()
df.tail()

# 특정한 열만 출력하고 싶을때
# 한개의 열만 파악
df['서비스 사용내역']


# unique값을 파악