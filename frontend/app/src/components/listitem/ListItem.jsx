import './ListItem.css'
import React from 'react'

import { useState } from 'react'
import { IoMdShare } from 'react-icons/io'
import { MdOutlineEdit } from 'react-icons/md'
import { IoMdArrowDropup } from 'react-icons/io'
import { IoMdArrowDropdown } from 'react-icons/io'

const ListItem = ({ listName, numBooks, description, books }) => {
  const [isOpen, setIsOpen] = useState(false)

  const toggleListItem = () => {
    setIsOpen(prev => !prev)
  }

  return (
    <div className="ListItem">
      <div className="about">
        <div className="info-list">
          <div className="title">
            <h3>{listName}</h3>
            <p>{numBooks} livros</p>
          </div>
          <div className="description">
            <p>{description}</p>
          </div>
        </div>
        <div className="buttons">
          {isOpen ? (
            <IoMdArrowDropup
              className="button"
              onClick={toggleListItem}
              size={24}
            />
          ) : (
            <IoMdArrowDropdown
              className="button"
              onClick={toggleListItem}
              size={24}
            />
          )}
          <MdOutlineEdit className="button" size={24} />
          <IoMdShare className="button" size={24} />
        </div>
      </div>
      <div className="books" style={{ display: isOpen ? 'block' : 'none' }}>
        <ul>
          {books.map((book, index) => (
            <li key={index}>{book}</li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default ListItem
