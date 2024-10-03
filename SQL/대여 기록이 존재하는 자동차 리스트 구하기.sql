SELECT distinct(CAR_ID)
from (select A.CAR_ID CAR_ID
     from CAR_RENTAL_COMPANY_CAR A inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY B
     on A.CAR_ID = B.CAR_ID
     where A.CAR_TYPE like '세단' and extract(month from START_DATE) = '10')
order by CAR_ID desc