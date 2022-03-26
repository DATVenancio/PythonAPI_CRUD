DESENVOLVIMENTO DE UMA API PARA AS FUNCIONALIDADES B�SICAS DE UM CRUD.

O densenvolvimento da logica principal de efuncionamentoda API est� no arquivo "main.py".
Desenvolvido em Python com o micro-framework Flask, a aplica��o � composta por 6 rotas, sendo elas:

 - / : Home page do site com explica��es b�sica da API.

 - /create/<nome>/<empresa>/<quantidade> : p�gina de cadastro de informa��es a partir dos dados fornecidos


   
 - /readall : p�gina de leitura de todos os dados da base de dados

   

 - /readone/<id>: p�gina de leitura de um dado espec�fico da base de dados. O parametro passado deve ser o ID da informa��o desejada.



 - /update/<id>/<campo>/<mudan�a> : p�gina de atualiza��o de um dado na base de dados. O primeiro parametro selecionado o dado a ser mudado; o segundo parametro seleciona o campo a ser mudado; e o terceiro parametro define a nova informa��o para o campo.



 - /delete : p�gina para deletar um dado da base de dados. O parametro passado deve ser o ID a ser deletado.

A home page do site est� no arquivo "index.html" na pasta "templates".
O arquivo "data.csv" � a base de dados.
