import './Pesquisa.css'
import axios from 'axios'
import SearchResults from '../../components/searchResults/SearchResults'

import { React, useState } from 'react'
import { LuSearch } from 'react-icons/lu'

function Pesquisa() {
  const [adicFilters, setAdicFilters] = useState({
    genero: '',
    autor: '',
  })
  const [erro, setError] = useState(null)
  const [userData, setUserData] = useState([])
  const [bookData, setBookData] = useState([])
  const [loading, setLoading] = useState(false)
  const [searchData, setSearchData] = useState('')
  const [answerReceived, setAnswerReceived] = useState(false)
  const [selectedFilter, setSelectedFilter] = useState('all')

  const fetchUsers = async () => {
    setLoading(true)

    try {
      const response = await axios.get(
        `http://localhost:8000/api/buscar-usuarios/?username=${searchData}`
      )
      setUserData(response.data.results)
    } catch (error) {
      setError(error)
    } finally {
      setLoading(false)
    }
  }

  const fetchBooks = async () => {
    setLoading(true)

    try {
      const response = await axios.get(
        `http://localhost:8000/api/buscar-livros/?titulo=${searchData}`
      )

      const booksWithGenres = response.data.map(book => {
        return {
          ...book,
          genero: book.genero ? book.genero.split(',').map(g => g.trim()) : [],
        }
      })

      setBookData(booksWithGenres)
    } catch (error) {
      setError(error)
    } finally {
      setLoading(false)
    }
  }

  const handleSearchBarSubmit = e => {
    e.preventDefault()

    setUserData([])
    setBookData([])
    setAnswerReceived(false)

    if (searchData.trim() !== '') {
      setAnswerReceived(true)
      setLoading(true)
      fetchUsers()
      fetchBooks()
    }
  }

  const handleSearchBarChange = e => {
    setSearchData(e.target.value)
  }

  const handleChangeFilter = e => {
    const value = e.target.value

    setSelectedFilter(value)

    if (value === 'all') {
      setAdicFilters({ genero: '', autor: '' })
    }
  }

  const handleApplyFilters = () => {
    const autor = document.getElementById('autor').value
    const genero = document.getElementById('genero').value

    setAdicFilters({
      genero: genero,
      autor: autor,
    })
  }

  const filterBooks = (books, filters) => {
    return books.filter(book => {
      const generoMatch = filters.genero
        ? book.genero.some(g =>
            g.toLowerCase().includes(filters.genero.toLowerCase())
          )
        : true

      const autorMatch = filters.autor
        ? book.autor.toLowerCase().includes(filters.autor.toLowerCase())
        : true

      return generoMatch && autorMatch
    })
  }

  if (loading) return <div>Carregando ...</div>

  return (
    <form onSubmit={handleSearchBarSubmit} id="search-form">
      <div className="search-container">
        <div className="search-bar-container">
          <label htmlFor="search_bar" className="input-label"></label>
          <input
            id="search_bar"
            name="search_bar"
            type="text"
            value={searchData}
            onChange={handleSearchBarChange}
            className="text-input"
            placeholder="Busque por livros ou usuários ..."
          ></input>
        </div>
        <button type="submit" className="search-button">
          <LuSearch size={24} />
        </button>
      </div>
      <div className="filter-container">
        <button
          type="button"
          value="all"
          className={`filter-op-button ${
            selectedFilter === 'all' ? 'active' : ''
          }`}
          onClick={handleChangeFilter}
        >
          Todos
        </button>
        <button
          type="button"
          value="users"
          className={`filter-op-button ${
            selectedFilter === 'users' ? 'active' : ''
          }`}
          onClick={handleChangeFilter}
        >
          Usuários
        </button>
        <button
          type="button"
          value="books"
          className={`filter-op-button ${
            selectedFilter === 'books' ? 'active' : ''
          }`}
          onClick={handleChangeFilter}
        >
          Livros
        </button>
      </div>
      <div
        className="adic-filter-container"
        style={{ display: selectedFilter === 'books' ? 'block' : 'none' }}
      >
        <p style={{ fontWeight: 600 }}>Filtros adicionais</p>
        <div className="adic-filters">
          <div className="adic-filter">
            <label htmlFor="genero" className="input-label">
              Gênero
            </label>
            <input
              id="genero"
              name="genero"
              type="text"
              className="text-input"
            ></input>
          </div>
          <div className="adic-filter">
            <label htmlFor="autor" className="input-label">
              Autor
            </label>
            <input
              id="autor"
              name="autor"
              type="text"
              className="text-input"
            ></input>
          </div>
        </div>
        <div className="adic-filters">
          <div className="adic-filter">
            <label htmlFor="ano-publi" className="input-label">
              Ano de publicação
            </label>
            <input
              id="ano-publi"
              name="ano-publi"
              type="text"
              className="text-input"
              disabled
            ></input>
          </div>
          <button
            type="button"
            className="adic-filter-button"
            onClick={handleApplyFilters}
          >
            Aplicar filtros
          </button>
        </div>
      </div>
      <SearchResults
        books={filterBooks(bookData, adicFilters)}
        users={userData}
        filter={selectedFilter}
        answerReceived={answerReceived}
      />
    </form>
  )
}

export default Pesquisa
