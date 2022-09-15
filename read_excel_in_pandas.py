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
df = pd.read_csv('result_1663200089476.csv')

# df의 컬럼명 : 엑셒파일에서 제목행
# 엑셀에서 제목행이라 함음 첫번째 행을 말한다.
# read_excel, read_csv할때 제목행 지정도 가능하고, skip
print(df.columns)

# head, tail  --> df의 개략적인 모습을 파악목적, 앞에서 5줄, 뒤에서 5줄을 보여준다.
df.head()
df.tail()

# 특정한 열만 출력하고 싶을때
# 한개의 열만 파악

print(df.columns)
# columns는 list형이
columns = df.columns

#df 컬럼명에 '_u1.' 이라는 문자열을 삭제하서 새롭게 df 컬럼명을 수정하고 싶어요
# 자주쓰는 list comprehension기법으로 컬럼명을 수정
print([i.replace('_u1.','') for i in columns])
df.columns = [i.replace('_u1.','') for i in columns]

# unique값을 파악, --> 모든 지역담당이 다 있는지 확인하고 싶으면
print(df['region'].unique())

#각 지역 담당별로 데이터 갯수 파악 -> query groupby
print(df.groupby('region').size().reset_index(name = 'cnt'))

# 가공결과를 엑셀파일로 저장하고 싶다.
df2 = df.groupby('region').size().reset_index(name = 'cnt')
df2.to_excel('df2.xlsx')




# pandas  datafrmae에서 db파일을 만들다.
# sqlite3 package import
import sqlite3

# sqlite connection을 만들자, 지정하는 파일이 없으면 생성, 있으면 연결만 합니다. db파일의 용량제한 없습니다.
conn = sqlite3.connect('cei.db')

# 테이블에 데이터를 추가합니다. if_exists 옵션에 따라서
# 만약 처음에 만든 컬럼과 불일치하면 data가 import안됩니다. 컬럼의 변화가 있다면 db내 테이블에 컬럼 추가 작업을 해야 한다.
# replace -> 기존데이터 삭제, 다시 테이블 만든다.
# append -> 끝에 데이터 추가
# 문법 : df.to_sql(테이블명, 테이벨이 존재할 경우 선택옵션, index 번호 미포함, db connection정보)
df.to_sql('rawdata', if_exists='append', index=False, con=conn)



# 기존 sqlite3 db에서 쿼리를 실행시키고, 결과를 가져오자
query_string ='''
select region, systype, round(avg(new_hdv_cfi_value),2) as 평균, round(max(new_hdv_cfi_value),2) as 최대값, round(min(new_hdv_cfi_value),2) as 최소값,
       round(count(new_hdv_cfi_value),2) as 갯수 from rawdata group by region, systype;
'''


df3 = pd.read_sql(query_string, con=conn)

df3.to_excel('담당별cei통계.xlsx')