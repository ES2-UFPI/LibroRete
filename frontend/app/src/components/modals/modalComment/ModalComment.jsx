import { React, useState } from 'react'
import './ModalComment.css'

import { IoCloseCircleSharp } from 'react-icons/io5'
import { IoCloseCircleOutline } from 'react-icons/io5'

const ModalComment = ({ isOpen, onClose, onSubmitComment }) => {
  const [formData, setFormData] = useState({
    comment: '',
  })

  const [isHovered, setIsHovered] = useState(false)
  const [isActive, setIsActive] = useState(false)

  const handleChange = e => {
    const { name, value } = e.target
    setFormData({ ...formData, [name]: value })
  }

  const handleSubmit = () => {
    onSubmitComment(formData.comment)
    setFormData({ comment: '' })
    onClose()
  }

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
      <div className="modal-comment" onClick={e => e.stopPropagation()}>
        <div className="modal-comment-header">
          <h3>Faça seu comentário!</h3>
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
        <div className="modal-comment-content">
          <label htmlFor="comment"></label>
          <textarea
            id="comment"
            name="comment"
            value={formData.comment}
            onChange={handleChange}
            rows="4"
            placeholder="Digite seu comentário aqui..."
          ></textarea>
          <button id="comment-button" onClick={handleSubmit}>
            Enviar
          </button>
        </div>
      </div>
    </div>
  )
}

export default ModalComment
