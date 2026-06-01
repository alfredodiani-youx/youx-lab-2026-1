select 
	data_pedido, 
	extract(day from data_pedido) as dia,
	extract(month from data_pedido) as mes,
	extract(year from data_pedido) as ano
from
	pedido


select
	nome,
	substring (nome from 1 for 5),
	substring (nome, 2)
from
	cliente


select
	nome,
	upper(nome)
from
	cliente

select nome, coalesce(cpf, 'Não informado') from cliente


select
	case sigla
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa catarina'
	else sigla
	end as uf
from 
	uf