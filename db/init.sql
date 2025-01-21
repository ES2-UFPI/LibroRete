CREATE DATABASE IF NOT EXISTS librorete;

USE librorete;

CREATE TABLE IF NOT EXISTS usuario(
    id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(150) NOT NULL,
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(320) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    foto TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS perfil (
    id INT PRIMARY KEY NOT NULL,
    bio VARCHAR(255) NOT NULL,
    interesses TEXT NOT NULL,
    id_usuario_perfil INT NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario_perfil) REFERENCES usuario(id)
);

CREATE TABLE IF NOT EXISTS lista (
    id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(150) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    id_perfil_lista INT NOT NULL,
    FOREIGN KEY (id_perfil_lista) REFERENCES perfil(id)
);

CREATE TABLE IF NOT EXISTS livro (
    isbn VARCHAR(15) PRIMARY KEY NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(150) NOT NULL,
    genero VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS lista_livro(
    id_lista INT NOT NULL,
    FOREIGN KEY (id_lista) REFERENCES lista(id),
    isbn_livro VARCHAR(15) NOT NULL,
    FOREIGN KEY (isbn_livro) REFERENCES livro(isbn)
);

CREATE TABLE IF NOT EXISTS post(
    id INT PRIMARY KEY NOT NULL,
    conteudo VARCHAR(255) NOT NULL,
    midia TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS comentario(
    id INT PRIMARY KEY NOT NULL,
    conteudo VARCHAR(255) NOT NULL,
    id_comentario_pai INT NULL,
    id_post INT NOT NULL,
    FOREIGN KEY (id_comentario_pai) REFERENCES comentario(id),
    FOREIGN KEY (id_post) REFERENCES post(id)
);

CREATE TABLE IF NOT EXISTS interacao(
    id INT PRIMARY KEY NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    data_interacao DATETIME NOT NULL,
    id_usuario INT NOT NULL,
    id_perfil_seguir INT NULL,
    id_post INT NULL,
    id_comentario INT NULL,
    id_comentario_respondido INT NULL,
    curtida BOOLEAN NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_post) REFERENCES post(id),
    FOREIGN KEY (id_comentario) REFERENCES comentario(id),
    FOREIGN KEY (id_comentario_respondido) REFERENCES comentario(id),
    FOREIGN KEY (id_perfil_seguir) REFERENCES perfil(id)
);

CREATE TABLE IF NOT EXISTS tags(
    nome VARCHAR(50) PRIMARY KEY NOT NULL
);

CREATE TABLE IF NOT EXISTS post_tag(
    id_post INTEGER NOT NULL,
    nome_tag VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_post) REFERENCES post(id),
    FOREIGN KEY (nome_tag) REFERENCES tags(nome) 
);

INSERT IGNORE INTO usuario (id, nome, username, email, senha, foto) VALUES 
(1, 'Maria Eduarda', '@eduarda', 'eduarda@gmail.com','2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4', 'https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png'),
(2, 'Guilherme Mancini', '@mancini', 'mancini@gmail.com','85e7613fc5c2e438bda561c68d9899cf3f648badaa558b01417630f06cf104c1', 'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png'),
(3, 'Laila Teixeira', '@laila', 'laila@gmail.com', '45h3453774c5c2e438bda561c58d9899c43f648b3daa558b02417630f061f104c2','https://pub-static.fotor.com/assets/projects/pages/d5bdd0513a0740a8a38752dbc32586d0/fotor-03d1a91a0cec4542927f53c87e0599f6.jpg'),
(4, 'Ygor Francisco', '@ygor', 'ygor@gmail.com','123456789ab5de2e438bda561c58d9899c43f648b3daa558b02417630f061f104c2','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb0Zcycgq7wKymbe-jMm8Jadi6-_c6sc0WBA&s');

INSERT IGNORE INTO perfil (id, bio, interesses, id_usuario_perfil) VALUES
(1, 'Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela', 'Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕', 1),
(2, 'Idade: 35 anos Profissão: Professor | Pronome: Ele/Dele', 'Entusiasta da vida digital 🌐 | Apaixonado por aprender 📚 | Explorando o mundo, uma ideia de cada vez ✨', 2),
(3, 'Idade: 17 anos Profissão: Desenhista | Pronome: Ela/Dela', '🎨 Designer apaixonada por arte e criatividade | 🖌️ Transformando ideias em projetos incríveis | 💡 Inspirando com design e lifestyle', 3), -- Laila
(4, 'Idade: 23 anos Profissão: Animer | Pronome: Ele/Dele', '🌟 Apaixonado por viagens e aventuras | 📸 Capturando momentos ao redor do mundo | 🍽️ Explorando sabores, culturas e destinos', 4); -- ygor

INSERT IGNORE INTO lista (id, nome, descricao, id_perfil_lista) VALUES
(435, 'livros de 2024','meus favoritos de 2024', 1),
(546, 'desejados','minha lista de desejos :)', 1),
(325, 'top ever!','top dos tops', 1),
(294, 'lista do mancini', 'lista pessoal', 2);

INSERT IGNORE INTO livro (isbn, titulo, autor, genero) VALUES
(9788581051031, 'Carrie','S. King', 'Terror'),
(9788525408532, 'Hamlet','W. Shakespeare', 'Tragédia'),
(9788580864458, '1984','G. Orwell', 'Distopia'),
(9786555600155, 'Coraline','N. Gailman', 'Terror'),
(9788576572374, 'Duna','F. Herbert', 'Ficção Científica'),
(9788506069790, 'A Ilha Do Tesouro','Robert Louis Stevenson', 'Romance'),
(9788576572374, 'A Cirurgiã','Leslie Wolfe', 'Suspense'),
(9786559575978, 'A Paciente Silenciosa','Alex Michaelides', 'Suspense'),
(9788551002957, 'O Homem De Giz','C. J. Tudor', 'Policial'),
(9788542226133, 'Quarta Asa','Rebecca Yarros', 'Fantasia');

INSERT IGNORE INTO lista_livro (id_lista, isbn_livro) VALUES
(435, 9786555600155), 
(435, 9788576572374), 
(325, 9788581051031),
(325, 9788525408532),
(325, 9788580864458),
(325, 9786555600155),
(325, 9788576572374);


INSERT IGNORE INTO post (id, conteudo, midia) VALUES
(1, "amei esse livro gente :)", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ailnDneVDYRN_d55CjsYSy0Vk_sxHyvK9g&s"),
(2, "Quem já leu essa maravilha??", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQB_geGRhJccyOA5-XTRH7U1wmae-1CGGaxww&s"),
(3, "Já tô preparando minha estante kkjjk", "https://static.wixstatic.com/media/c5af93_a56b3ef2ca444a9ba69e260989c10a3c~mv2.jpg/v1/fill/w_980,h_860,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/c5af93_a56b3ef2ca444a9ba69e260989c10a3c~mv2.jpg"),
(4, "Lendo um clássicooooo!!!", "https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2015/04/17/thumbnail644.jpg"),
(5, "Ler crônicas nunca é demais 😎", "https://m.media-amazon.com/images/I/41pjH50wvrL.jpg"),
(6, "Vou reeler só pela décima vez 😂", "https://cdn.awsli.com.br/800x800/2099/2099388/produto/172329856/3a725c4a7b.jpg"),
(7, "Aprendendo mais sobre um dos meus países favoritos <3", "https://m.media-amazon.com/images/I/91NDFlRPGTL._UF894,1000_QL80_.jpg"), -- ygor
(8, "Será se as cores são tão importantes assim? 🤔 Veremos 👀", "https://m.media-amazon.com/images/I/41RuWuRzqsL._SY445_SX342_.jpg"); -- laila

INSERT IGNORE INTO comentario (id, conteudo, id_comentario_pai, id_post) VALUES
(1, "Tbm gostei miga", NULL, 1),
(2, "Parabens pela ÓTIMAAAA escolha de livro 📚", NULL, 1),
(3, "É muito bom né? kkk", 1, 1),
(4, "Siiimmmm queria poder bater minha cabeça só pra esquecer, e ler de novo kkkk",  3, 1),
(5, "Esse livro é coisa de outro mundo 👽", NULL, 2),
(6, "Desculpa, mas as únicas crônicas que sei é as de Nárnia kkkk",NULL,5),
(7, "Esse eu já perdi as contas de quanto já li", NULL, 6);

INSERT IGNORE INTO tags (nome) VALUES 
("#Ficção"),
("#Romance"),
("#Fantasia"),
("#Terror"),
("#Aventura"),
("#Drama"),
("#Policial"),
("#Suspense"),
("#Historico"),
("#Aprendendo"),
("#Distopia"),
("#Fabula"),
("#DiaDaLeitura"),
("#GeorgeOrwell"),
("#DavidArnold"),
("#A.J.Fikry"),
("#CharlesDarwin"),
("#DanielNoNohay"),
("#PequenoPrincipe"),
("#Top"),
("#Reflexão");

INSERT IGNORE INTO post_tag (id_post, nome_tag) VALUES
(1, "#DiaDaLeitura"),
(1, "#Top"),
(1, "#Fantasia"),
(1, "#Ficção"),
(3, "#GeorgeOrwell"),
(3, "#DavidArnold"),
(3, "#A.J.Fikry"),
(3, "#CharlesDarwin"),
(3, "#DanielNoNohay"),
(3, "#Distopia"),
(3, "#Historico"),
(3, "#Top"),
(3, "#Ficção"),
(4, "#Fabula"),
(4, "#Fantasia"),
(4, "#PequenoPrincipe"),
(4, "#Ficção"),
(5, "#PequenoPrincipe"),
(5, "#Reflexão"),
(5, "#Ficção"),
(7, "#Historico"),
(7, "#Suspense");
(8, "#Aprendendo");
(8, "#Suspense");

INSERT IGNORE INTO interacao (id, tipo, data_interacao, id_usuario, id_post, id_comentario,id_comentario_respondido, curtida, id_perfil_seguir) VALUES
(1, "criar post", "2024/12/13 12:13:34", 1, 1, NULL,NULL, FALSE, NULL), -- Usuário 1 criou o post 1
(2, "criar comentario", "2024/12/13 16:34:01", 2, 1, 1, NULL, FALSE, NULL), -- Usuário 2, no post 1, criou o comentário 1
(3, "like post","2024/12/13 17:43:10", 2, 1, NULL,NULL, TRUE, NULL), -- Usuário 2, no post 1, deu um like no post
(4, "criar comentario", "2024/12/13 18:12:21", 1, 1, 3, NULL, FALSE, NULL), -- Usuário 1, no post 1, criou o comentário 3
(5, "responder comentario", "2024/12/13 18:12:21", 1, 1, 3, 1, FALSE, NULL), -- Usuário 1, no post 1, com o comentário 3 respondeu o comentário 1
(6, "like comentario", "2024/12/13 19:35:05", 2, 1, 3, NULL, TRUE, NULL), -- Usuário 2, no post 1, deu um like no comentário 3
(7, "seguir perfil", "2024/12/20 20:55:05", 1, NULL, NULL,NULL,FALSE,2), -- Usuário 1 está seguindo o perfil de id 2
(8, "criar post", "2025/01/01 14:04:00", 1, 3,NULL,NULL,FALSE,NULL), -- Usuário 1 criou o post 3
(9, "criar post", "2025/01/02 15:10:21", 1, 4,NULL,NULL,FALSE,NULL), -- Usuário 1 criou o post 4
(10, "criar post", "2025/01/07 10:23:50",2,5,NULL,NULL,FALSE,NULL), -- Usuário 2 criou o post 5         
(11, "criar post", "2025/01/10 20:43:12",2,6,NULL,NULL,FALSE,NULL), -- Usuário 2 criou o post 6
(12, "criar comentario", "2025/01/07 14:05:04", 1, 5, 6,NULL,FALSE,NULL), -- Usuário 1, no post 5, criou o comentario 6
(13, "criar comentario", "2025/01/11 12:32:23", 1, 6, 7,NULL,FALSE,NULL), -- Usuário 1, no post 6, criou o comentario 7
(14, "criar post", "2025/01/09 14:50:12", 4, 7,NULL,NULL,FALSE,NULL), -- Usuário 4 criou o post 7
(15, "criar post", "2025/01/08 12:06:14", 3, 8,NULL,NULL,FALSE,NULL), -- Usuário 3 criou o post 8
(16, "seguir perfil", "2025/01/01 12:55:10", 3, NULL, NULL,NULL,FALSE,4), -- Usuário 3 está seguindo o perfil de id 4
(17, "seguir perfil", "2025/01/01 13:03:00", 4, NULL, NULL,NULL,FALSE,3), -- Usuário 4 está seguindo o perfil de id 3
(18, "like post","2025/01/10 17:12:05", 3, 8, NULL,NULL, TRUE, NULL), -- Usuário 3, no post 8, deu um like no post
(19, "like post","2025/01/11 20:30:10", 4, 7, NULL,NULL, TRUE, NULL), -- Usuário 4, no post 7, deu um like no post
(20, "seguir perfil", "2025/01/09 13:44:10", 2, NULL, NULL,NULL,FALSE,1), -- Usuário 2 está seguindo o perfil de id 1
(21, "seguir perfil", "2025/01/04 11:32:03", 2, NULL, NULL,NULL,FALSE,3), -- Usuário 2 está seguindo o perfil de id 3
(22, "seguir perfil", "2025/01/03 19:15:02", 2, NULL, NULL,NULL,FALSE,4), -- Usuário 2 está seguindo o perfil de id 4
(23, "like post","2025/01/08 04:12:30", 1, 5, NULL,NULL, TRUE, NULL), -- Usuário 1, no post 5, deu um like no post
(24, "seguir perfil", "2025/01/09 10:02:03", 3, NULL, NULL,NULL,FALSE,1), -- Usuário 3 está seguindo o perfil de id 1
(25, "seguir perfil", "2025/01/10 03:05:02", 4, NULL, NULL,NULL,FALSE,1); -- Usuário 4 está seguindo o perfil de id 1
