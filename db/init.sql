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



DROP PROCEDURE IF EXISTS busca_livros_por_username;

DELIMITER $$
CREATE PROCEDURE busca_livros_por_username(IN username_param VARCHAR(20))
BEGIN
    SELECT 
        lista.nome AS nome_lista,
        lista.id,
        livro.titulo
    FROM 
        perfil 
    INNER JOIN usuario ON perfil.id_usuario_perfil = usuario.id 
    INNER JOIN lista ON lista.id_perfil_lista = perfil.id_usuario_perfil
    INNER JOIN lista_livro ON lista.id = lista_livro.id_lista
    INNER JOIN livro ON livro.isbn = lista_livro.isbn_livro
    WHERE usuario.username = username_param;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS busca_qtd_livros_de_uma_lista_por_username;

DELIMITER $$

CREATE PROCEDURE busca_qtd_livros_de_uma_lista_por_username(IN lista_nome VARCHAR(150), IN username_param VARCHAR(20))
BEGIN
    SELECT 
        COUNT(*) AS total
    FROM 
        perfil 
    INNER JOIN usuario ON perfil.id_usuario_perfil = usuario.id 
    INNER JOIN lista ON lista.id_perfil_lista = perfil.id_usuario_perfil
    INNER JOIN lista_livro ON lista.id = lista_livro.id_lista
    INNER JOIN livro ON livro.isbn = lista_livro.isbn_livro
    WHERE 
		usuario.username = username_param AND lista.nome=lista_nome;
END$$

DELIMITER ;

DROP PROCEDURE IF EXISTS busca_listas_de_um_usuario;
DELIMITER $$

CREATE PROCEDURE busca_listas_de_um_usuario(IN username_param VARCHAR(20))
BEGIN
    SELECT 
    lista.nome AS nome_lista
    FROM perfil
    INNER JOIN lista ON perfil.id=lista.id_perfil_lista
    INNER JOIN usuario ON perfil.id=usuario.id
    WHERE usuario.username=username_param;

END$$

DELIMITER ;



-- Busca TODOS os livros que o usuário cadastrou em diferentes listas
CALL busca_livros_por_username('@eduarda');

-- Busca TODAS as listas de um usuário
CALL busca_listas_de_um_usuario('@eduarda');

-- Busca a quantidade de livros de uma lista x em um perfl y
CALL busca_qtd_livros_de_uma_lista_por_username('top ever!','@eduarda');