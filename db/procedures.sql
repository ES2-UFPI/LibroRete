USE librorete;


DROP PROCEDURE IF EXISTS busca_posts;

DELIMITER $$
CREATE PROCEDURE busca_posts(IN username_param VARCHAR(20))
BEGIN
    IF username_param IS NULL THEN
        SELECT 
            usuario.foto AS foto_perfil, 
            usuario.nome, 
            usuario.username, 
            interacao.data_interacao,  
            post.conteudo, 
            post.midia
        FROM 
            interacao
        INNER JOIN usuario ON usuario.id=interacao.id_usuario
        INNER JOIN post ON post.id=interacao.id
        WHERE tipo='criar post';
    ELSE
        SELECT 
            usuario.foto AS foto_perfil, 
            usuario.nome, 
            usuario.username, 
            interacao.data_interacao,  
            post.conteudo, 
            post.midia
        FROM 
            interacao
        INNER JOIN usuario ON usuario.id=interacao.id_usuario
        INNER JOIN post ON post.id=interacao.id
        WHERE tipo='criar post' AND usuario.username=username_param;
    END IF;
END$$
DELIMITER ;


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
-- CALL busca_livros_por_username('@eduarda');

-- Busca TODAS as listas de um usuário
-- CALL busca_listas_de_um_usuario('@eduarda');

-- Busca a quantidade de livros de uma lista x em um perfl y
-- CALL busca_qtd_livros_de_uma_lista_por_username('top ever!','@eduarda');

-- Busca TODOS os post cadastrados CASO SEJA PASSADO O VALOR NULL COMO PARAMETRO
-- CALL busca_posts(NULL);

-- Busca TODOS os posts de um pessoa pelo seu USERNAME (seu @)
-- CALL busca_posts('@eduarda');
