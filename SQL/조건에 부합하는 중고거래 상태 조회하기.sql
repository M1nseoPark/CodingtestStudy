SELECT board_id, writer_id, title, price, decode(status, 'SALE', '판매중', 'RESERVED', '예약중', 'DONE', '거래완료') status
from used_goods_board
where to_char(created_date, 'yyyy-mm-dd') like '2022-10-05'
order by board_id desc