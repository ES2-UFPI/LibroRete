import './ModalPost.css'
import Post from '../post/Post'

import { React, useState } from 'react'

import { IoCloseCircleSharp } from 'react-icons/io5'
import { IoCloseCircleOutline } from 'react-icons/io5'

const ModalPost = ({ isOpen, onClose, post }) => {
  const [isHovered, setIsHovered] = useState(false)
  const [isActive, setIsActive] = useState(false)

  const handleMouseEnter = () => {
    setIsHovered(true)
  }

  const handleMouseLeave = () => {
    setIsHovered(false)
  }

  const handleMouseDown = () => {
    setIsActive(true)
  }

  const handleMouseUp = () => {
    setIsActive(false)
    onClose()
    setIsHovered(false)
  }

  if (!isOpen) return null

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-post" onClick={e => e.stopPropagation()}>
        <div className="modal-post-header">
          {isActive || isHovered ? (
            <IoCloseCircleSharp
              className="modal-close"
              size={30}
              onClick={handleMouseUp}
              onMouseEnter={handleMouseEnter}
              onMouseLeave={handleMouseLeave}
              onMouseDown={handleMouseDown}
              style={{
                color: isActive ? '#5a4536' : '#8a726a',
              }}
            />
          ) : (
            <IoCloseCircleOutline
              className="modal-close"
              size={30}
              onClick={handleMouseUp}
              onMouseEnter={handleMouseEnter}
              onMouseLeave={handleMouseLeave}
              onMouseDown={handleMouseDown}
              style={{
                color: '#8a726a',
              }}
            />
          )}
        </div>
        <div className="modal-post-content">
          <Post
            id={post.id}
            user_id={1}
            foto={post.foto}
            time={post.time}
            liked={false}
            image={post.midia}
            caption={post.conteudo}
            username={post.nome}
            num_likes={post.curtidas}
            num_shares={0}
            num_comments={post.comentarios}
            comments={post.lista_comentarios}
          />
        </div>
      </div>
    </div>
  )
}

export default ModalPost
