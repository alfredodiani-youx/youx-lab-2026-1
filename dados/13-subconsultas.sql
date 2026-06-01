select
	data_pedido,
	valor
from
	pedido
where
	valor >= (select avg(valor) from pedido)