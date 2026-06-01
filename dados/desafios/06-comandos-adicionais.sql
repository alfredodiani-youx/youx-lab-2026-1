select * from cliente;
select
	nome,
	coalesce(extract(month from data_nascimento), 0)
from cliente;

select
	nome,
	case extract(month from data_nascimento)
		when 1 then 'Janeiro'
		when 2 then 'Fevereiro'
		when 3 then 'Março'
		when 4 then 'Abril'
		when 5 then 'Maio'
		when 6 then 'Junho'
		when 7 then 'Julho'
		when 8 then 'Agosto'
		when 9 then 'Setembro'
		when 10 then 'Outubro'
		when 11 then 'Novembro'
		when 12 then 'Dezembro'
	else
		'Não informado'
	end as mes_aniversario
from cliente

select 
	nome,
	coalesce(extract(year from data_nascimento), 0) as ano
from cliente

select
	substring (nome from 5 for 10)
from municipio

select
	upper(nome)
from municipio
select
	nome
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	else 'não informado'
	end
from cliente

select
	nome,
	case
		when valor >= 500 then 'Acima ou igual a 500'
		else 'Abaixo de 500'
		end
from produto;
	

select * from cliente