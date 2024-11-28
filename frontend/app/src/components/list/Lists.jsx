import './Lists.css'
import React from 'react'

import { GoPlusCircle } from 'react-icons/go'
import ListItem from '../listitem/ListItem'

const Lists = () => {
  return (
    <div className="ListContent">
      <div className="info">
        <h2>Listas de Livros</h2>
        <GoPlusCircle id="add-icon" size={28} />
      </div>
      <div className="lists">
        <ListItem
          listName={'Livros 2025'}
          numBooks={'10'}
          description={'Livros para ler até o final do ano de 2025'}
          books={['Livro 1', 'Livro 2']}
        />
        <ListItem
          listName={'Romance'}
          numBooks={'5'}
          description={'Livros de romance que todos deveriam ler'}
          books={['Livro 3', 'Livro 4', 'Livro 5']}
        />
      </div>
    </div>
  )
}

export default Lists
