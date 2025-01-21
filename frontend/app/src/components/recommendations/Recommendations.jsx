import './Recommendations.css'
import axios from 'axios'
import BookRecommendation from '../bookRecommendation/BookRecommendation'
import UserRecommendation from '../userRecommendation/UserRecommendation'

import { FaUser } from 'react-icons/fa'
import { FaBookOpen } from 'react-icons/fa6'

import { React, useState, useEffect } from 'react'

const Recommendations = () => {
  const [userRecommendations, setUserRecommendations] = useState([])
  const [bookRecommendations, setBookRecommendations] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  const fetchBookRecommendations = async () => {
    setLoading(true)

    try {
      const response = await axios.get(
        'http://localhost:8000/api/livros-recom/@eduarda/?format=json'
      )

      const booksWithGenres = response.data.map(book => {
        return {
          ...book,
          genero: book.genero ? book.genero.split(',').map(g => g.trim()) : [],
        }
      })

      setBookRecommendations(booksWithGenres)
    } catch (error) {
      setError(error)
    } finally {
      setLoading(false)
    }
  }

  const fetchUsersRecommendations = async () => {
    setLoading(true)

    try {
      const response = await axios.get(
        'http://localhost:8000/api/usuarios-recom/@eduarda/?format=json'
      )

      setUserRecommendations(response.data)
    } catch (error) {
      setError(error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchBookRecommendations()
    fetchUsersRecommendations()
  }, [])

  if (loading) return <div>Carregando ...</div>
  if (erro) return <div>Erro ao carregar os dados: {erro.message}</div>

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
            {bookRecommendations.map((book, index) => (
              <BookRecommendation
                key={index}
                title={book.titulo}
                author={book.autor}
                genre={book.genero}
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
            {userRecommendations.map((user, index) => (
              <UserRecommendation
                key={index}
                username={user.username}
                photo={user.foto}
              />
            ))}
          </div>
        </div>
      </div>
    </>
  )
}

export default Recommendations
