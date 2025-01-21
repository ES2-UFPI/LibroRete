import './SearchResults.css'
import BookRecommendation from '../bookRecommendation/BookRecommendation'
import UserRecommendation from '../userRecommendation/UserRecommendation'
import React from 'react'

function SearchResults({ books, users, filter, answerReceived }) {
  return (
    <>
      {answerReceived && (
        <div className="results">
          <p style={{ fontWeight: 600 }}>Resultados</p>
          {filter !== 'users' && (
            <div className="books-results">
              {books.length === 0 ? (
                <p>Livro não encontrado</p>
              ) : (
                books.map((book, index) => (
                  <BookRecommendation
                    key={index}
                    title={book.titulo}
                    author={book.autor}
                    genre={book.genero}
                  />
                ))
              )}
            </div>
          )}
          {filter !== 'books' && (
            <div className="users-results">
              {users.length === 0 ? (
                <p>Usuário não encontrado</p>
              ) : (
                users.map((user, index) => (
                  <UserRecommendation
                    key={index}
                    username={user.username}
                    photo={user.foto}
                  />
                ))
              )}
            </div>
          )}
        </div>
      )}
    </>
  )
}

export default SearchResults
