import './Pesquisa.css'
import axios from 'axios'
import SearchResults from '../../components/searchResults/SearchResults'

import { React, useState } from 'react'
import { LuSearch } from 'react-icons/lu'

function Pesquisa() {
  const [answerReceived, setAnswerReceived] = useState(false)
  const [selectedFilter, setSelectedFilter] = useState('all')
  const [searchData, setSearchData] = useState('')
  const [adicFilters, setAdicFilters] = useState({
    genre: '',
    author: '',
    year: '',
  })
  const [userData, setUserData] = useState([])
  const [bookData, setBookData] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(false)

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

  const handleSearchBarSubmit = e => {
    e.preventDefault()
    if (searchData.trim() !== '') {
      setAnswerReceived(true)
      setLoading(true)
      fetchUsers()
    }
  }

  const handleSearchBarChange = e => {
    setSearchData(e.target.value)
  }

  const handleChangeFilter = e => {
    const value = e.target.value
    setSelectedFilter(value)
    if (value === 'all') {
      setAdicFilters({ genre: '', author: '', year: '' })
    }
  }

  const handleApplyFilters = () => {
    setAdicFilters({
      genre: adicFilters.genre,
      author: adicFilters.author,
      year: adicFilters.year,
    })
  }

  const filterBooks = (books, filters) => {
    return books.filter(book => {
      const genreMatch = filters.genre
        ? book.genre.some(g =>
            g.toLowerCase().includes(filters.genre.toLowerCase())
          )
        : true
      const authorMatch = filters.author
        ? book.author.toLowerCase().includes(filters.author.toLowerCase())
        : true
      const yearMatch = filters.year ? book.year === filters.year : true
      return genreMatch && authorMatch && yearMatch
    })
  }

  if (loading) return <div>Carregando ...</div>
  if (erro) return <div>Erro ao carregar os dados: {erro.message}</div>

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
