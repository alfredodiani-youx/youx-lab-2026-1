alter table cliente rename column profissao to idprofissao
alter table cliente alter column idprofissao type integer
-- e: 1,9,10,12,15,17
-- enge: 2
-- pedr: 3
-- jorna: 4,5
-- profe: 6,7,8,13
-- nada: 11,14
select * from cliente
alter table cliente drop idprofissao
alter table cliente add idprofissao int
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);

update cliente set idprofissao = 1 where idcliente in (1,9,10,12,15,17);
update cliente set idprofissao = 2 where idcliente in (2);
update cliente set idprofissao = 3 where idcliente in (3);
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6,7,8,13);
select * from profissao


