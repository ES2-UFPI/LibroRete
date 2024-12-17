import './BookRecommendation.css'
import React from 'react'

const BookRecommendation = ({ title, author, genre }) => {
  return (
    <div className="Book">
      <h4>{title}</h4>
      <p>{author}</p>
      <p>{genre.join(', ')}</p>
    </div>
  )
}

export default BookRecommendation
