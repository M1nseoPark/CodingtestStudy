SELECT ANIMAL_ID, NAME
from (select A.ANIMAL_ID ANIMAL_ID, A.NAME NAME, B.DATETIME - A.DATETIME AS PERIOD
      from ANIMAL_INS A inner join ANIMAL_OUTS B
      on A.ANIMAL_ID = B.ANIMAL_ID
      order by PERIOD desc)
where rownum < 3