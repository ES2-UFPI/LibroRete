import './Recommendations.css'
import BookRecommendation from '../bookRecommendation/BookRecommendation'
import UserRecommendation from '../userRecommendation/UserRecommendation'
import photo_user1 from '../../imgs/photo_user1.png'
import photo_user2 from '../../imgs/photo_user2.png'
import photo_user3 from '../../imgs/photo_user3.png'

import { FaUser } from 'react-icons/fa'
import { FaBookOpen } from 'react-icons/fa6'

import React from 'react'

const Recommendations = () => {
  const book_recommendations = [
    {
      title: '1984',
      author: 'George Orwell',
      genre: ['Distopia', 'Ficcção Científica'],
    },
    {
      title: 'Orgulho e Preconceito',
      author: 'Jane Austen',
      genre: ['Romance', 'Clássico'],
    },
    {
      title: 'O Hobbit',
      author: 'J.R.R, Tolkien',
      genre: ['Fantasia', 'Aventura'],
    },
    {
      title: '1984',
      author: 'George Orwell',
      genre: ['Distopia', 'Ficcção Científica'],
    },
  ]

  const user_recommendations = [
    {
      username: 'joao_',
      photo: photo_user1,
    },
    {
      username: 'ana321',
      photo: photo_user2,
    },
    {
      username: 'user_1',
      photo: photo_user3,
    },
    {
      username: 'joao_',
      photo: photo_user1,
    },
  ]

  return (
    <>
      <h3>Sugestões para você</h3>
      <div className="RecommendationsContent">
        <div className="section">
          <div className="header">
            <div className="label">
              <h4>Livros</h4>
              <FaBookOpen size={24} />
            </div>
          </div>
          <div className="recommendations">
            {book_recommendations.map((book, index) => (
              <BookRecommendation
                key={index}
                title={book.title}
                author={book.author}
                genre={book.genre}
              />
            ))}
          </div>
        </div>
        <div className="section">
          <div className="header">
            <div className="label">
              <h4>Usuários</h4>
              <FaUser size={24} />
            </div>
          </div>
          <div className="recommendations">
            {user_recommendations.map((user, index) => (
              <UserRecommendation
                key={index}
                username={user.username}
                photo={user.photo}
              />
            ))}
          </div>
        </div>
      </div>
    </>
  )
}

export default Recommendations
