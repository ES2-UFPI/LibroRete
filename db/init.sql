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
    nome VARCHAR(150) PRIMARY KEY NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

INSERT IGNORE INTO usuario (id, nome, username, email, senha, foto) VALUES 
(1, 'maria eduarda', '@eduarda', 'eduarda@gmail.com','2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw0nQQC1W3yDwpOFLJJTqmirx88ESUttZFLA&s'),
(2, 'guilherme mancini', '@mancini', 'mancini@gmail.com','85e7613fc5c2e438bda561c68d9899cf3f648badaa558b01417630f06cf104c1', 'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png');


INSERT IGNORE INTO perfil (id, bio, interesses, id_usuario_perfil) VALUES
(1, 'Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela', 'Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕', 1),
(2, 'Idade: 35 anos Profissão: Professor | Pronome: Ele/Dele', 'Entusiasta da vida digital 🌐 | Apaixonado por aprender 📚 | Explorando o mundo, uma ideia de cada vez ✨', 2);

