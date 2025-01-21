import { React, useState } from 'react'
import './Comment.css'
import axios from 'axios'

import { AiFillLike } from 'react-icons/ai'
import { AiOutlineLike } from 'react-icons/ai'

const Comment = ({
  id,
  conteudo,
  username,
  foto,
  id_comentario_pai,
  id_post,
  liked = false,
  num_likes = 0,
}) => {
  const [isLiked, setIsLiked] = useState(liked)
  const [numLikes, setNumLikes] = useState(num_likes)

  const handleLikeClick = () => {
    const newLiked = !isLiked

    if (newLiked) {
      const json_like_comment = {
        tipo: 'like comentario',
        id_usuario: 1,
        id_post: id_post,
        id_comentario: id,
      }

      console.log(json_like_comment)

      axios
        .post('http://localhost:8000/api/interacoes/', json_like_comment, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(response => {
          console.log('Response:', response.data)
          setIsLiked(newLiked)
          setNumLikes(prev => prev + 1)
        })
        .catch(error => {
          console.error('Erro ao registrar curtida no comentário:', error)
        })
    }
  }

  return (
    <div className="comment-container">
      <div className="user-comment-container">
        <img
          src={foto}
          alt="foto de perfil"
          className="foto-perfil-comment"
        ></img>
        <p id="username-p">{username}</p>
      </div>
      <div className="info-comment-container">
        <p>{conteudo}</p>
        <div className="likes-container">
          <p className="num_likes">{numLikes}</p>
          {isLiked ? (
            <AiFillLike
              className="like-icon"
              size={20}
              onClick={handleLikeClick}
            />
          ) : (
            <AiOutlineLike
              className="like-icon"
              size={20}
              onClick={handleLikeClick}
            />
          )}
        </div>
      </div>
    </div>
  )
}

export default Comment
