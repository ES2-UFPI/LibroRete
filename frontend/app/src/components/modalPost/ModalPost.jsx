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
            time={post.time}
            liked={post.liked}
            image={post.image}
            caption={post.caption}
            username={post.username}
            num_likes={post.num_likes}
            num_shares={post.num_shares}
            num_comments={post.num_comments}
          />
        </div>
      </div>
    </div>
  )
}

export default ModalPost
