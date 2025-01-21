import './ProfilePosts.css'
import React from 'react'
import axios from 'axios'
import { useEffect, useState } from 'react'

import ProfilePostItem from '../ProfilePostItem/ProfilePostItem'
const ProfilePosts = () => {
  const [data, setData] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  function hoursToText(hours) {
    if (hours === 0) return 'há menos de 1h'

    if (hours <= 24) {
      return `há ${hours}} ${hours} === 1 ? 'hora' : 'horas'}`
    }

    const data = new Date()
    data.setHours(data.getHours() - hours)

    const dia = String(data.getDate()).padStart(2, '0')
    const mes = String(data.getMonth() + 1).padStart(2, '0')
    const ano = data.getFullYear()

    return `${dia}/${mes}/${ano}`
  }

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/posts/@eduarda?format=json')
      .then(response => {
        console.log('Raw Response:', response.data)
        setData(response.data)
        setLoading(false)
      })
      .catch(error => {
        setError(error)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Carregando ...</div>
  if (erro) return <div>Erro ao carregar os dados: {erro.message}</div>

  return (
    <div className="ProfilePostContent">
      <div className="profile-posts">
        {data.map((post, index) => (
          <ProfilePostItem
            key={index}
            id={post.id}
            conteudo={post.conteudo}
            midia={post.midia}
            curtidas={post.curtidas}
            comentarios={post.comentarios}
            lista_comentarios={post.lista_comentarios}
            time={hoursToText(post.time)}
            foto={
              'https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png'
            }
          />
        ))}
      </div>
    </div>
  )
}

export default ProfilePosts
