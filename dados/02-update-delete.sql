select * from cliente;
update cliente set nome = 'Teste' where idcliente = 1;


update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;


insert into cliente (idcliente, nome) values (16, 'João');
delete from cliente where idcliente = 16;


insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (16, 'Maicon', '12349596421', '1234', '1965-10-10', 'F', 'Empresário', null, null, null, null, null, 'Florianópolis', 'PR');


insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (17, 'Getúlio', null, '4631', null, 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (18, 'Sandra', null, null, null, 'M', 'Professor', 'Italiana', null, '12', 'Bloco A', null, null, null);

update cliente set cpf = '45390569432', genero = 'M', nacionalidade = 'Brasileira', uf = 'SC' where idcliente = 16;

update cliente set data_nascimento = '1978-04-01', genero = 'M' where idcliente = 17;

update cliente set genero = 'F', profissao = 'Professora', numero = 123 where idcliente = 18

delete from cliente where idcliente = 16;
delete from cliente where idcliente = 18;