import './Pesquisa.css'
import photo_user1 from '../../imgs/photo_user1.png'
import photo_user2 from '../../imgs/photo_user2.png'
import photo_user3 from '../../imgs/photo_user3.png'
import SearchResults from '../../components/searchResults/SearchResults'

import { React, useState } from 'react'
import { LuSearch } from 'react-icons/lu'

function Pesquisa() {
  const [books] = useState([
    {
      title: '1984',
      author: 'George Orwell',
      genre: ['Distopia', 'Ficção Científica'],
      year: '2020',
    },
    {
      title: 'Orgulho e Preconceito',
      author: 'Jane Austen',
      genre: ['Romance', 'Clássico'],
      year: '2020',
    },
    {
      title: 'O Hobbit',
      author: 'J.R.R, Tolkien',
      genre: ['Fantasia', 'Aventura'],
      year: '2010',
    },
    {
      title: '1984',
      author: 'George Orwell',
      genre: ['Distopia', 'Ficção Científica'],
      year: '2010',
    },
    {
      title: '1984',
      author: 'George Orwell',
      genre: ['Distopia', 'Ficção Científica'],
      year: '2010',
    },
  ])

  const [users] = useState([
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
  ])

  const [answerReceived, setAnswerReceived] = useState(false)
  const [selectedFilter, setSelectedFilter] = useState('')
  const [searchData, setSearchData] = useState('')
  const [adicFilters, setAdicFilters] = useState({
    genre: '',
    author: '',
    year: '',
  })

  const handleSearchBarChange = e => {
    const value = e.target.value
    if (value !== '') {
      setSearchData(value)
    }
  }

  const handleChangeFilter = e => {
    const value = e.target.value
    setSelectedFilter(value)

    if (value === 'all') {
      setAdicFilters({
        genre: '',
        author: '',
        year: '',
      })
    }
  }

  const handleSearchBarSubmit = e => {
    e.preventDefault()
    if (searchData !== '') {
      alert(searchData)
      setAnswerReceived(true)
      setSelectedFilter('all')
    }
  }

  const handleApplyFilters = () => {
    setAdicFilters({
      genre: document.getElementById('genero').value,
      author: document.getElementById('autor').value,
      year: document.getElementById('ano-publi').value,
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
        books={filterBooks(books, adicFilters)}
        users={users}
        filter={selectedFilter}
        answerReceived={answerReceived}
      />
    </form>
  )
}

export default Pesquisa
