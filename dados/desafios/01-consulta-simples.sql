select nome, genero from cliente order by nome desc;
select nome from cliente where nome like '%P%';
select nome from cliente where nome like 'C%';
select nome from cliente where nome like '%a';
select nome, bairro from cliente where bairro like 'Centro' or bairro like 'Ct%';
select nome, complemento from cliente where complemento like 'A%';
select nome, genero from cliente where genero like 'F';
select nome from cliente where cpf is null;
select nome, profissao from cliente order by profissao;
select nome, nacionalidade from cliente where nacionalidade like '%rasileir%';
select nome from cliente where numero is not null;
select nome, uf from cliente where uf like 'SC';
select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';
select nome, logradouro || ', ' || numero || ', ' || complemento || ', ' || bairro || ', ' || municipio || ', ' || uf from cliente