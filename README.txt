DESENVOLVIMENTO DE UMA API PARA AS FUNCIONALIDADES BÁSICAS DE UM CRUD.

O densenvolvimento da logica principal de efuncionamentoda API está no arquivo "main.py".
Desenvolvido em Python com o micro-framework Flask, a aplicação é composta por 6 rotas, sendo elas:

 - / : Home page do site com explicações básica da API.

 - /create/<nome>/<empresa>/<quantidade> : página de cadastro de informações a partir dos dados fornecidos


   
 - /readall : página de leitura de todos os dados da base de dados

   

 - /readone/<id>: página de leitura de um dado específico da base de dados. O parametro passado deve ser o ID da informação desejada.



 - /update/<id>/<campo>/<mudança> : página de atualização de um dado na base de dados. O primeiro parametro selecionado o dado a ser mudado; o segundo parametro seleciona o campo a ser mudado; e o terceiro parametro define a nova informação para o campo.



 - /delete : página para deletar um dado da base de dados. O parametro passado deve ser o ID a ser deletado.

A home page do site está no arquivo "index.html" na pasta "templates".
O arquivo "data.csv" é a base de dados.
