select '/home/grep/src/' || b.board_id || '/' || b.file_id || b.file_name || b.file_ext as file_path
from USED_GOODS_BOARD a, USED_GOODS_FILE b
where a.board_id = b.board_id and a.views = (SELECT max(views) from used_goods_board) 
order by b.file_id desc