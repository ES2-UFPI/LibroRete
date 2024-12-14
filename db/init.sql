CREATE DATABASE IF NOT EXISTS librorete;

USE librorete;

CREATE TABLE IF NOT EXISTS usuario(
    id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(150) NOT NULL,
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(320) UNIQUE NOT NULL,
    senha VARCHAR(255) UNIQUE NOT NULL,
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
    data_criacao DATETIME NOT NULL,
    midia TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS comentario(
    id INT PRIMARY KEY NOT NULL,
    conteudo VARCHAR(255) NOT NULL,
    data_criacao DATETIME NOT NULL,
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
    id_post INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_post) REFERENCES post(id)
);



INSERT IGNORE INTO usuario (id, nome, username, email, senha, foto) VALUES 
(1, 'maria eduarda', '@eduarda', 'eduarda@gmail.com','2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw0nQQC1W3yDwpOFLJJTqmirx88ESUttZFLA&s'),
(2, 'guilherme mancini', '@mancini', 'mancini@gmail.com','85e7613fc5c2e438bda561c68d9899cf3f648badaa558b01417630f06cf104c1', 'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png');


INSERT IGNORE INTO perfil (id, bio, interesses, id_usuario_perfil) VALUES
(1, 'Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela', 'Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕', 1),
(2, 'Idade: 35 anos Profissão: Professor | Pronome: Ele/Dele', 'Entusiasta da vida digital 🌐 | Apaixonado por aprender 📚 | Explorando o mundo, uma ideia de cada vez ✨', 2);

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
(9788576572374, 'Duna','F. Herbert', 'Ficção Científica');

INSERT IGNORE INTO lista_livro (id_lista, isbn_livro) VALUES
(435, 9786555600155), 
(435, 9788576572374), 
(325, 9788581051031),
(325, 9788525408532),
(325, 9788580864458),
(325, 9786555600155),
(325, 9788576572374);


INSERT IGNORE INTO post (id, conteudo, data_criacao, midia) VALUES
(1, "amei esse livro gente :)", "2024/12/13 12:13:34", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ailnDneVDYRN_d55CjsYSy0Vk_sxHyvK9g&s"),
(2, "Quem já leu essa maravilha??", "2024/12/14 09:10:17", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQB_geGRhJccyOA5-XTRH7U1wmae-1CGGaxww&s");

INSERT INTO comentario (id, conteudo, data_criacao, id_comentario_pai, id_post) VALUES
(1, "Tbm gostei miga", "2024/12/13 12:20:13", NULL, 1),
(2, "Parabens pela ÓTIMAAAA escolha de livro 📚", "2024/12/13 13:45:06", NULL, 1),
(3, "É muito bom né? kkk", "2024/12/13 12:30:42", 1, 1),
(4, "Siiimmmm queria poder bater minha cabeça só pra esquecer, e ler de novo kkkk", "2024/12/13 12:35:23", 3, 1),
(5, "Esse livro é coisa de outro mundo 👽", "2024/12/14 13:12:54", NULL, 2);


INSERT IGNORE INTO interacao (id, tipo, data_interacao, id_usuario, id_post) VALUES
(1, "criar post", "2024/12/13 12:13:34", 1, 1),
(2, "criar post", "2024/12/13 15:40:31", 2, 2);

