select * from cliente;
select 
	cln.nome as cliente,
	prf.nome as profissao,
	nac.nome as nacionalidade,
	logradouro,
	numero,
	com.nome as complemento,
	ba.nome as bairro,
	mu.nome as municipio,
	uf.sigla as uf
from cliente as cln
inner join
	profissao as prf on cln.idprofissao = prf.idprofissao
inner join
	nacionalidade as nac on cln.idnacionalidade = nac.id
inner join
	complemento as com on cln.idcomplemento = com.id
inner join
	bairro as ba on cln.idbairro = ba.id
inner join
	municipio as mu on cln.idmunicipio = mu.id
inner join
	uf on mu.iduf = uf.id;

select 
	pr.nome as produto,
	pr.valor as valor,
	fr.nome as fornecedor
from produto as pr
left join 
	fornecedor as fr on pr.idfornecedor = fr.idfornecedor;


select
	tra.nome as transportadora,
	mu.nome as municipio
from transportadora as tra
left join
	municipio as mu on tra.idmunicipio = mu.id;


select
	data_pedido as data,
	valor,
	cl.nome as cliente,
	tra.nome as transportadora,
	ve.nome as vendedor
from pedido as pe
left join
	cliente as cl on pe.idcliente = cl.idcliente
left join 
	transportadora as tra on pe.idtransportadora = tra.idtransportadora
left join
	vendedor as ve on pe.idvendedor = ve.idvendedor;


select
	pro.nome,
	quantidade,
	valor_unitario
from pedido_produto as pe
left join
	produto as pro on pe.idproduto = pro.idproduto;


select
	cliente.nome as cliente,
	pedido.data_pedido as data
from pedido
left join
	cliente on pedido.idcliente = cliente.idcliente
order by cliente.nome;


select 
	cliente.nome as cliente,
	pedido.data_pedido as data
from cliente
left join
	pedido on pedido.idcliente = cliente.idcliente
order by cliente.nome;


select
	mu.nome,
	count(idcliente) as quantidade_clientes
from cliente
left join
	municipio as mu on cliente.idmunicipio = mu.id
group by mu.nome;


select 
	fo.nome as fornecedor,
	count(pr.idproduto)
from fornecedor as fo
left join
	produto as pr on fo.idfornecedor = pr.idfornecedor
group by fo.nome;

select
	cl.nome,
	sum(pe.valor)
from pedido as pe
left join
	cliente as cl on pe.idcliente = cl.idcliente
group by cl.nome;


select
	ve.nome as vendedor,
	sum(pe.valor)
from pedido as pe
left join
	vendedor as ve on ve.idvendedor = pe.idvendedor
group by ve.nome


select
	tra.nome as transportadora,
	sum(pe.valor)
from pedido as pe
left join
	transportadora as tra on pe.idtransportadora = tra.idtransportadora
group by tra.nome


select
	cl.nome as cliente,
	count(pe.idpedido)
from pedido as pe
left join
	cliente as cl on pe.idcliente = cl.idcliente
group by cl.nome


select
	pro.nome as nome,
	sum(pe.quantidade)
from pedido_produto as pe
left join 
	produto as pro on pe.idproduto = pro.idproduto
group by nome


select
	data_pedido,
	sum(valor)
from pedido
group by data_pedido



select
	pe.data_pedido as data,
	sum(pedido_produto.quantidade)
from pedido as pe
left join
	pedido_produto on pedido_produto.idpedido = pe.idpedido
group by data

select * from pedido_produto