select * from pedido
select avg(valor) from pedido group by idvendedor having avg(valor) > 200
select sum(valor) from pedido group by idvendedor having sum(valor) >= 1500
select nome from vendedor where idvendedor in (1,2,3,4)
select sum(valor) from pedido group by idvendedor
select count(id) from municipio
select count(id) from municipio where iduf in (1,2)
select * from uf

-- não dei ctrl + s, e perdi todo restante do código :/  (voltarei no fim do curso)