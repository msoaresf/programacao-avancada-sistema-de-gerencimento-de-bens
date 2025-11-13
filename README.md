# programacao-avancada-sistema-de-gerencimento-de-bens
Atividade Prática 1 – Programação Avançada
A UFSM precisa de um sistema para gerenciar os bens patrimoniais, como computadores,
mesas, projetores e outros equipamentos. O sistema deve permitir cadastrar, listar, editar,
excluir e gerar relatórios sobre os bens. Os dados deverão ser armazenados de forma persistente
em um arquivo binário utilizando o módulo pickle.
Estrutura do Sistema
O sistema deve ser orientado a objetos, contendo pelo menos duas classes principais:
1. Classe Bem
Representa um item patrimonial. Deve possuir os seguintes atributos:
• codigo (int)
• descricao (str)
• localizacao (str)
• situacao (str) — “Disponível”, “Em uso” ou “Em manutenção”
Deve conter métodos como:
• __init__(...) — inicializa os atributos.
• __str__(...) — retorna informações resumidas do bem.
• Outros métodos que o aluno considerar necessários (ex: atualizar dados via set).
2. Classe ControlePatrimonio
Gerencia os bens e a persistência de dados. Deve conter métodos como:
• carregar_dados(self) — carrega os bens do arquivo binário.
• salvar_dados(self) — salva os bens no arquivo binário.
• cadastrar_bem(self) — adiciona um novo bem.
• listar_bens(self) — exibe todos os bens cadastrados.
• editar_bem(self) — permite alterar dados de um bem.
• excluir_bem(self) — remove um bem, respeitando regras definidas.
• gerar_relatorio(self) — exibe estatísticas dos bens.
Persistência com pickle
• O arquivo de dados deve se chamar patrimonio.pkl.
• Ao iniciar o programa, os dados devem ser carregados (caso o arquivo exista).
• Sempre que houver alteração (cadastro, edição ou exclusão), o arquivo deve ser atualizado.
• Deve haver tratamento de exceções para: FileNotFoundError, IOError, pickle.PickleError,
EOFError e entradas inválidas.
Universidade Federal de Santa Maria – Campus Cachoeira do Sul Página 1 de 3
Atividade Prática 1 – Programação Avançada –
Menu Principal
O programa principal deve conter um menu interativo chamando os métodos da classe
ControlePatrimonio:
=== SISTEMA DE CONTROLE DE PATRIMÔNIO UNIVERSITÁRIO ===
Aluno: [NOME COMPLETO DO ALUNO]
1 - Cadastrar bem patrimonial
2 - Listar bens
3 - Editar bem
4 - Excluir bem
5 - Gerar relatório
0 - Sair
Regras obrigatórias
1. O uso de POO é obrigatório. Não será aceito código estruturado.
2. O código não deve conter comentários.
3. O nome completo do aluno deve aparecer no menu inicial.
4. Cada aluno deve criar uma regra de negócio própria (ex: não permitir excluir bens em
manutenção, código não se repetir, etc.).
5. O sistema deve tratar exceções e impedir encerramento inesperado.
Entrega e Apresentação
• Cada aluno apresentará individualmente em sala de aula o seu código/programa para o
professor.
• Cada aluno terá entre 5 e 10 minutos para a apresentação.
• O aluno deverá executar o programa, demonstrar todas as funcionalidades e explicar
verbalmente:
– Estrutura das classes e métodos.
– Funcionamento da persistência com pickle.
– Tratamento de exceções implementado.
– Regra de negócio própria.
– Comunicação do menu com as classes.
Critérios de Avaliação
Os trabalhos serão avaliados em aula no dia 13/11/2025 considerando os seguintes critérios:
Critério Peso
Uso correto de POO (classes, métodos, objetos, encapsulamento) 2,0
Manipulação de arquivos binários com pickle 2,0
Tratamento de exceções 1,0
Clareza e domínio na explicação oral 5,0
Entregáveis
• Arquivos .py com o código completo e funcional (sem comentários).
• Arquivo patrimonio.pkl com pelo menos 3 bens cadastrados.
Universidade Federal de Santa Maria – Campus Cachoeira do Sul Página 2 de 3
Atividade Prática 1 – Programação Avançada –
Exemplo de Execução
=== SISTEMA DE CONTROLE DE PATRIMÔNIO UNIVERSITÁRIO ===
Aluno: Adriano Oliveira
1 - Cadastrar bem patrimonial
2 - Listar bens
3 - Editar bem
4 - Excluir bem
5 - Gerar relatório
0 - Sair
Escolha: 1
Código: 105
Descrição: Computador I7 com 16GB de RAM
Localização: C1 - Sala 30
Situação: Em uso
Bem cadastrado com sucesso!
Escolha: 5
=== RELATÓRIO ===
Total de bens: 3
Disponíveis: 1
Em uso: 1
Em manutenção: 1
