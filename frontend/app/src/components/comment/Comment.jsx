import { React, useState } from 'react'
import './Comment.css'

import { AiFillLike } from 'react-icons/ai'
import { AiOutlineLike } from 'react-icons/ai'

const Comment = ({
  id,
  conteudo,
  username = 'qualquer',
  foto = 'https://picsum.photos/seed/picsum/200/300',
  id_comentario_pai,
  id_post,
  liked = false,
  num_likes = 0,
}) => {
  const [isLiked, setIsLiked] = useState(liked)
  const [numLikes, setNumLikes] = useState(num_likes)
  const handleLikeClick = () => {
    const newLiked = !isLiked

    if (newLiked) setNumLikes(prev => prev + 1)
    else setNumLikes(prev => prev - 1)
    setIsLiked(newLiked)
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
