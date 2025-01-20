import './ProfilePosts.css'
import React from 'react'
import axios from 'axios'
import { useEffect, useState } from 'react'

import ProfilePostItem from '../ProfilePostItem/ProfilePostItem'
const ProfilePosts = () => {
  const [data, setData] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(true)

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
            midia={post.midia}
            id={post.id}
            conteudo={post.conteudo}
          />
        ))}
      </div>
    </div>
  )
}

export default ProfilePosts
