-- 주석은 -- 두번 이후에 작성

-- database : 엑셀파일
-- table : 엑셀 시트
-- roa : 엑셀 시트내 행
-- 필드 : 엑셀 열, 컬럼
--  rawdata 테이블에서 모든 컬럼 내용을 10행만 가져오라
select * from rawdata limit 10;

-- 원하는 컬럼만 선택해서 가져온다.
select systype,region from rawdata limit 20;


-- region에서 unique한 값만 파악하고 싶을때
select distinct region from rawdata;
select distinct region, team from rawdata;

-- 컬럼의 제목을 변경해서 가져오고 싶을때
select region as 본부, team 팀 from rawdata limit 10;

-- 기존 데이터에 덧붙이고 싶을때
select region || '본부' as 본부, team 팀 from rawdata limit 10;

-- 조건에 따라서 검색
select region, team from rawdata where team <> 'ALL' limit 10;

-- 필드값의 일부를 제거하고 싶을때

select team from rawdata limit 10

-- 무조건 윈쬑에서 2개문자 취하는 경우, 동부산팀의 경우에 맞지 않는다.
select region, leftstr(team,2) as 팀제거명 from rawdata where team <> 'ALL' limit 10;

-- 마지막 문자가 팀이라고 가정하고 전체 길이에서 1 뺀 길이로 왼쪽에서부터 가져온다.
select region, team, LENGTH(team) as 팀이름길이 from rawdata where team <> 'ALL' limit 10;
select region, team, LENGTH(team) as 팀이름길이, leftstr(team, length(team)-1) from rawdata where team <> 'ALL' limit 10;

-- 집계합수
select region, systype, avg(new_hdv_cfi_value) as 평균, max(new_hdv_cfi_value) as 최대값, min(new_hdv_cfi_value) as 최소값,
       count(new_hdv_cfi_value) as 갯수 from rawdata group by region, systype;

-- round처리, 소수점기준 반올림
select region, systype, round(avg(new_hdv_cfi_value),2) as 평균, round(max(new_hdv_cfi_value),2) as 최대값, round(min(new_hdv_cfi_value),2) as 최소값,
       round(count(new_hdv_cfi_value),2) as 갯수 from rawdata group by region, systype;




