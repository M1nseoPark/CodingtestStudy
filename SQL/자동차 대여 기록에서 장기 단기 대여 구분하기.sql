SELECT HISTORY_ID, CAR_ID, to_char(START_DATE, 'yyyy-mm-dd') START_DATE, to_char(END_DATE, 'yyyy-mm-dd') END_DATE, case when (end_date - start_date + 1) >= 30 then '장기 대여' else '단기 대여' end RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where extract(year from START_DATE) = 2022 and extract(month from START_DATE) = 9
order by history_id desc