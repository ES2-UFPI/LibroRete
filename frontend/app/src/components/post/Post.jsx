import './Post.css'
import React from 'react'
import axios from 'axios'
import ModalShare from '../modals/modalShare/ModalShare'
import ModalComment from '../modals/modalComment/ModalComment'

import { useEffect, useState } from 'react'
import { AiFillLike } from 'react-icons/ai'
import { AiOutlineLike } from 'react-icons/ai'
import { BsPersonCircle } from 'react-icons/bs'
import { FaRegCommentAlt } from 'react-icons/fa'
import { RiShareForwardLine } from 'react-icons/ri'
import { HiOutlineDotsHorizontal } from 'react-icons/hi'

const Post = ({
  id,
  user_id,
  foto,
  liked,
  time,
  num_likes,
  num_shares,
  num_comments,
  username,
  image,
  caption,
  comments,
}) => {
  const [isLiked, setIsLiked] = useState(liked)
  const [numLikes, setNumLikes] = useState(num_likes)
  const [isModalCommentOpen, setIsModalCommentOpen] = useState(false)
  const [isModalShareOpen, setIsModalShareOpen] = useState(false)
  const [numShares, setNumShares] = useState(num_shares)
  const [numComments, setNumComments] = useState(num_comments)

  const [comment, setComment] = useState([])

  const openModalShare = () => {
    setIsModalShareOpen(true)
  }

  const closeModalShare = () => {
    setIsModalShareOpen(false)
  }

  const openModalComment = () => {
    setIsModalCommentOpen(true)
  }

  const closeModalComment = () => {
    setIsModalCommentOpen(false)
  }

  function sendToApi(json, type) {
    axios
      .post('http://localhost:8000/api/interacoes/', json, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        console.log('Response:', response.data)
        return true
      })
      .catch(error => {
        console.error(`Erro ao registrar ${type}:`, error)
        return false
      })
  }

  const handleLikeClick = e => {
    e.preventDefault()

    const newLiked = !isLiked

    if (newLiked) {
      const json_like = {
        tipo: 'like post',
        id_usuario: user_id,
        id_post: id,
      }

      if (sendToApi(json_like, 'curtida')) {
        setIsLiked(newLiked)
        setNumLikes(prev => prev + 1)
      }
    }
  }

  const handleCommentClick = () => {
    openModalComment()
  }

  const handleSubmitComment = comment => {
    setComment(prevComments => [...prevComments, comment])

    const json_comment = {
      tipo: 'criar comentario',
      id_usuario: user_id,
      id_post: id,
      conteudo_comentario: comment,
    }

    if (sendToApi(json_comment, 'comentário')) {
      setNumComments(prev => prev + 1)
    }
  }

  const handleShareClick = () => {
    openModalShare()

    // const json_share = {
    //   tipo: 'share',
    //   id_usuario: user_id,
    //   id_post: id,
    // }

    // axios
    //   .post('http://localhost:8000/api/interacoes/', json_share, {
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //   })
    //   .then(response => {
    //     console.log('Response:', response.data)
    //     setNumShares(prev => prev + 1)
    //   })
    //   .catch(error => {
    //     console.error('Erro ao registrar compartilhamento:', error)
    //   })

    // console.log('Compartilhamento enviado com sucesso!')
  }

  return (
    <div className="Post">
      <div className="header">
        <div className="l-container">
          {foto ? (
            <img id="user_photo_post" src={foto} alt="Foto de perfil" />
          ) : (
            <BsPersonCircle id="user_photo_post" size={26} />
          )}
          <div className="username-container">
            <p id="user">{username}</p>
            <p id="time">{time}</p>
          </div>
        </div>
        <div className="r-container">
          <HiOutlineDotsHorizontal size={20} />
        </div>
      </div>
      <img src={image} alt="my-post" width={600} />
      <div className="footer">
        <div className="interactions">
          <div className="info-interaction">
            <p className="num_interactions">{numLikes}</p>
            {isLiked ? (
              <AiFillLike
                className="interaction"
                size={24}
                onClick={handleLikeClick}
              />
            ) : (
              <AiOutlineLike
                className="interaction"
                size={24}
                onClick={handleLikeClick}
              />
            )}
          </div>
          <div className="info-interaction">
            <p className="num_interactions">{numComments}</p>
            <FaRegCommentAlt
              className="interaction"
              size={24}
              onClick={handleCommentClick}
            />
            <ModalComment
              isOpen={isModalCommentOpen}
              onClose={closeModalComment}
              onSubmitComment={handleSubmitComment}
              id_post={id}
              comments={comments}
            ></ModalComment>
          </div>
          <div className="info-interaction">
            <p className="num_interactions">{numShares}</p>
            <RiShareForwardLine
              className="interaction"
              size={24}
              onClick={handleShareClick}
            />
            <ModalShare
              isOpen={isModalShareOpen}
              onClose={closeModalShare}
            ></ModalShare>
          </div>
        </div>
        <div className="text">
          <p id="user">{username}</p>
          <p id="caption-post">{caption}</p>
        </div>
      </div>
    </div>
  )
}

export default Post
