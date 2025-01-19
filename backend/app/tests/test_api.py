from django.test import TestCase
from django.urls import reverse
import requests

class APITests(TestCase):
    def test_usuario_endpoint(self):
        response = self.client.get("/api/usuarios/@eduarda")
        
        # Validações
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é 200 OK
        self.assertEqual(response.json(), {"id":1,"nome":"Maria Eduarda","username":"@eduarda","email":"eduarda@gmail.com","senha":"2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4","foto":"https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png"})  # Substitua pelo JSON esperado
    
    def test_perfil_endpoint_online(self):
        response = self.client.get("/api/perfis/@eduarda")
        self.assertEqual(response.status_code, 200)
    
    def test_perfil_endpoint_no_user(self):
        response = self.client.get("/api/perfis/@marcio")
        self.assertEqual(response.status_code, 404)

    
    def test_perfil_endpoint_numeros(self):
        response = self.client.get("/api/perfis/@eduarda")

        self.assertEqual(response.json()['numero_posts'], 3)
        self.assertEqual(response.json()['numero_seguidores'], 3)
        self.assertEqual(response.json()['numero_seguindo'], 1)    

    def test_perfil_endpoint_info_perfil(self):
        response = self.client.get("/api/perfis/@eduarda")

        self.assertEqual(response.json()['bio'], "Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela")
        self.assertEqual(response.json()['interesses'], "Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕")  
    
    def test_perfil_endpoint_info_usuario(self):
        response = self.client.get("/api/perfis/@eduarda")

        self.assertEqual(response.json()['nome'], "Maria Eduarda")
        self.assertEqual(response.json()['username'], "@eduarda")
        self.assertEqual(response.json()['foto'], "https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png")
    
    def test_perfil_endpoint_json(self):
        response = self.client.get("/api/perfis/@eduarda")
        self.assertEqual(response.json(), {"numero_seguidores": 3,"numero_seguindo": 1,"numero_posts": 3,"bio": "Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela","nome": "Maria Eduarda","foto": "https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png","username": "@eduarda","interesses": "Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕"}) 
    
    def test_listas_endpoint_online(self):
        response = self.client.get("/api/listas/@eduarda") #http://localhost:8000/api/listas/@eduarda?format=json
        self.assertEqual(response.status_code, 200)
    
    def test_listas_endpoint_json(self):
        response = self.client.get("/api/listas/@eduarda")
        self.assertEqual(response.json(), [
    {
        "lista": "top ever!",
        "descricao": "top dos tops",
        "livros": [
            [
                "Carrie"
            ],
            [
                "Hamlet"
            ],
            [
                "1984"
            ],
            [
                "Coraline"
            ],
            [
                "Duna"
            ]
        ],
        "livrosAPIGoogle": [
            {
                "titulo": "Carrie, a estranha",
                "autor": [
                    "Stephen King"
                ],
                "data_publicacao": "2007-01-11",
                "descricao": "Até 1972, Stephen King ainda era um professor cujo salário mal dava para sustentar a mulher, Tabitha, e os dois filhos. Nas horas vagas, escrevia histórias de suspense, sempre rejeitadas pelas editoras. Foi então que finalizou mais uma obra. Em seguida, porém, desiludido com o mercado editorial, King arremessou-a pela janela. Foi Tabitha quem o convenceu de recuperar os originais e tentar outra vez. Enviado a um editor, o livro foi aceito. Nascia Carrie, a Estranha, obra que lançou Stephen King no cenário literário mundial. O livro narra a atormentada adolescência de uma jovem problemática, perseguida pelos colegas, professores e impedida pela mãe de levar a vida como as garotas de sua idade. Só que Carrie guarda um segredo: quando ela está por perto, objetos voam, portas são trancadas ao sabor do nada, velas se apagam e voltam a iluminar, misteriosamente. Com tantos ingredientes de suspense, Carrie, a Estranha\"\" logo se transformou num enorme sucesso internacional. Ao ser transportado para as telas, em 1976, pelas mãos de Brian de Palma, teve a atriz Sissy Spacek e John Travolta em seus papéis principais.",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=QB19ir2j2TMC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=QB19ir2j2TMC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            },
            {
                "titulo": "Hamlet",
                "autor": [
                    "William Shakespeare"
                ],
                "data_publicacao": "1997-05-05",
                "descricao": "\"Hamlet\", de William Shakespeare, é uma obra clássica permanentemente atual pela força com que trata de problemas fundamentais da condição humana. A obsessão de uma vingança onde a dúvida e o desespero concentrados nos monólogos do príncipe Hamlet adquirem uma impressionante dimensão trágica. Nesta versão, Millôr Fernandes resgata o prazer de ler Shakespeare, o maior dramaturgo da literatura universal, em uma das suas obras mais famosas.",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=9HIv76atRQIC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=9HIv76atRQIC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            },
            {
                "titulo": "1984",
                "autor": [
                    "George Orwell"
                ],
                "data_publicacao": "2009-07-21",
                "descricao": "Publicada originalmente em 1949, a distopia futurista 1984 é um dos romances mais influentes do século XX, um inquestionável clássico moderno. Lançada poucos meses antes da morte do autor, é uma obra magistral que ainda se impõe como uma poderosa reflexão ficcional sobre a essência nefasta de qualquer forma de poder totalitário. Winston, herói de 1984, último romance de George Orwell, vive aprisionado na engrenagem totalitária de uma sociedade completamente dominada pelo Estado, onde tudo é feito coletivamente, mas cada qual vive sozinho. Ninguém escapa à vigilância do Grande Irmão, a mais famosa personificação literária de um poder cínico e cruel ao infinito, além de vazio de sentido histórico. De fato, a ideologia do Partido dominante em Oceânia não visa nada de coisa alguma para ninguém, no presente ou no futuro. O'Brien, hierarca do Partido, é quem explica a Winston que \"só nos interessa o poder em si. Nem riqueza, nem luxo, nem vida longa, nem felicidade: só o poder pelo poder, poder puro\". Quando foi publicada em 1949, essa assustadora distopia datada de forma arbitrária num futuro perigosamente próximo logo experimentaria um imenso sucesso de público. Seus principais ingredientes - um homem sozinho desafiando uma tremenda ditadura; sexo furtivo e libertador; horrores letais - atraíram leitores de todas as idades, à esquerda e à direita do espectro político, com maior ou menor grau de instrução. À parte isso, a escrita translúcida de George Orwell, os personagens fortes, traçados a carvão por um vigoroso desenhista de personalidades, a trama seca e crua e o tom de sátira sombria garantiram a entrada precoce de 1984 no restrito panteão dos grandes clássicos modernos. \"O maior escritor do século XX.\" - Observer \"Obra-prima terminal de Orwell, 1984 é uma leitura absorvente e indispensável para a compreensão da história moderna.\" - Timothy Garton Ash, New York Review of Books \" A obra mais sólida e mais impressionante de Orwell.\" - V. S. Pritchett",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=5VD2SwmX7dAC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=5VD2SwmX7dAC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            },
            {
                "titulo": "Coraline",
                "autor": [
                    "Neil Gaiman"
                ],
                "data_publicacao": "2020-06-19",
                "descricao": "Clássico de Neil Gaiman que mistura terror e conto de fadas ganha edição especial Certas portas não devem ser abertas. E Coraline descobre isso pouco tempo depois de chegar com os pais à sua nova casa, um apartamento em um casarão antigo ocupado por vizinhos excêntricos e envolto por uma névoa insistente, um mundo de estranhezas e magia, o tipo de universo que apenas Neil Gaiman pode criar. Ao abrir uma porta misteriosa na sala de casa, a menina se depara com um lugar macabro e fascinante. Ali, naquele outro mundo, seus outros pais são criaturas muito pálidas, com botões negros no lugar dos olhos, sempre dispostos a lhe dar atenção, fazer suas comidas preferidas e mostrar os brinquedos mais divertidos. Coraline enfim se sente... em casa. Mas essa sensação logo desaparece, quando ela descobre que o lugar guarda mistérios e perigos, e a menina se dá conta de que voltar para sua verdadeira casa vai ser muito mais difícil — e assustador — do que imaginava. Publicado pela primeira vez em 2002, Coraline foi o primeiro livro de Neil Gaiman para o público infantojuvenil e se tornou uma das obras mais emblemáticas do escritor. Repleta de elementos ao mesmo tempo sombrios e lúdicos, a história conquistou crianças e adultos em todo o mundo e, em 2009, ganhou as telas de cinema em uma animação dirigida por Henry Selick, de O estranho mundo de Jack. Nesta edição especial em capa dura, com introdução do autor e projeto gráfico exclusivo, coube ao renomado ilustrador Chris Riddell dar vida ao universo mágico e aterrorizante criado por Neil Gaiman.",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=xxLmDwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=xxLmDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            },
            {
                "titulo": "Duna",
                "autor": [
                    "Frank Herbert"
                ],
                "data_publicacao": "2015-09-16",
                "descricao": "A vida do jovem Paul Atreides está prestes a mudar radicalmente. Após a visita de uma mulher misteriosa, ele é obrigado a deixar seu planeta natal para sobreviver ao ambiente árido e severo de Arrakis, o Planeta Deserto. Envolvido numa intrincada teia política e religiosa, Paul divide-se entre as obrigações de herdeiro e seu treinamento nas doutrinas secretas de uma antiga irmandade, que vê nele a esperança de realização de um plano urdido há séculos. Ecos de profecias ancestrais também o cercam entre os nativos de Arrakis. Seria ele o eleito que tornaria viáveis seus sonhos e planos ocultos? Ao lado das trilogias Fundação, de Isaac Asimov, e O Senhor dos Anéis, de J. R. R. Tolkien, Duna é considerada uma das maiores obras de fantasia e ficção científica de todos os tempos. Um premiado best-seller já levado às telas de cinema pelas mãos do consagrado diretor David Lynch.",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=q82uCgAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=q82uCgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            }
        ]
    },
    {
        "lista": "livros de 2024",
        "descricao": "meus favoritos de 2024",
        "livros": [
            [
                "Coraline"
            ],
            [
                "Duna"
            ]
        ],
        "livrosAPIGoogle": [
            {
                "titulo": "Coraline",
                "autor": [
                    "Neil Gaiman"
                ],
                "data_publicacao": "2020-06-19",
                "descricao": "Clássico de Neil Gaiman que mistura terror e conto de fadas ganha edição especial Certas portas não devem ser abertas. E Coraline descobre isso pouco tempo depois de chegar com os pais à sua nova casa, um apartamento em um casarão antigo ocupado por vizinhos excêntricos e envolto por uma névoa insistente, um mundo de estranhezas e magia, o tipo de universo que apenas Neil Gaiman pode criar. Ao abrir uma porta misteriosa na sala de casa, a menina se depara com um lugar macabro e fascinante. Ali, naquele outro mundo, seus outros pais são criaturas muito pálidas, com botões negros no lugar dos olhos, sempre dispostos a lhe dar atenção, fazer suas comidas preferidas e mostrar os brinquedos mais divertidos. Coraline enfim se sente... em casa. Mas essa sensação logo desaparece, quando ela descobre que o lugar guarda mistérios e perigos, e a menina se dá conta de que voltar para sua verdadeira casa vai ser muito mais difícil — e assustador — do que imaginava. Publicado pela primeira vez em 2002, Coraline foi o primeiro livro de Neil Gaiman para o público infantojuvenil e se tornou uma das obras mais emblemáticas do escritor. Repleta de elementos ao mesmo tempo sombrios e lúdicos, a história conquistou crianças e adultos em todo o mundo e, em 2009, ganhou as telas de cinema em uma animação dirigida por Henry Selick, de O estranho mundo de Jack. Nesta edição especial em capa dura, com introdução do autor e projeto gráfico exclusivo, coube ao renomado ilustrador Chris Riddell dar vida ao universo mágico e aterrorizante criado por Neil Gaiman.",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=xxLmDwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=xxLmDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            },
            {
                "titulo": "Duna",
                "autor": [
                    "Frank Herbert"
                ],
                "data_publicacao": "2015-09-16",
                "descricao": "A vida do jovem Paul Atreides está prestes a mudar radicalmente. Após a visita de uma mulher misteriosa, ele é obrigado a deixar seu planeta natal para sobreviver ao ambiente árido e severo de Arrakis, o Planeta Deserto. Envolvido numa intrincada teia política e religiosa, Paul divide-se entre as obrigações de herdeiro e seu treinamento nas doutrinas secretas de uma antiga irmandade, que vê nele a esperança de realização de um plano urdido há séculos. Ecos de profecias ancestrais também o cercam entre os nativos de Arrakis. Seria ele o eleito que tornaria viáveis seus sonhos e planos ocultos? Ao lado das trilogias Fundação, de Isaac Asimov, e O Senhor dos Anéis, de J. R. R. Tolkien, Duna é considerada uma das maiores obras de fantasia e ficção científica de todos os tempos. Um premiado best-seller já levado às telas de cinema pelas mãos do consagrado diretor David Lynch.",
                "foto": {
                    "smallThumbnail": "http://books.google.com/books/content?id=q82uCgAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=q82uCgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                }
            }
        ]
    },
    {
        "lista": "desejados",
        "descricao": "minha lista de desejos :)",
        "livros": [],
        "livrosAPIGoogle": []
    }
])
