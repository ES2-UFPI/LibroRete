import { React, useState } from 'react'
import './ModalShare.css'

import { FaCog } from 'react-icons/fa'
import { IoCloseCircleSharp } from 'react-icons/io5'
import { IoCloseCircleOutline } from 'react-icons/io5'

const ModalShare = ({ isOpen, onClose }) => {
  const [isHovered, setIsHovered] = useState(false)
  const [isActive, setIsActive] = useState(false)

  const handleChange = e => {
    const { name, value } = e.target
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
      <div className="modal-share" onClick={e => e.stopPropagation()}>
        <div className="modal-share-header">
          <h3>Compartilhe com seus amigos!</h3>
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
        <div className="modal-share-content">
          <p>Em breve ...</p>
          <FaCog size={20} className="fa-cog" />
        </div>
      </div>
    </div>
  )
}

export default ModalShare
