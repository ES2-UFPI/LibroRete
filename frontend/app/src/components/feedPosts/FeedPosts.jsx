import './FeedPosts.css'
import Post from '../post/Post'
import axios from 'axios'
import { CiStar } from 'react-icons/ci'

import { React, useState, useEffect } from 'react'

const FeedPosts = () => {
  const [data, setData] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/posts/feed/@eduarda?format=json')
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

  const posts = data.feed_posts
  const recommended_posts = data.top_tag_posts

  return (
    <div className="FeedPostsContent">
      {posts.map((post, index) => (
        <Post
          key={index}
          id={post.id}
          user_id={'1'}
          time={post.time}
          liked={false}
          image={post.midia}
          caption={post.conteudo}
          username={post.nome}
          num_likes={post.curtidas}
          num_shares={0}
          num_comments={post.comentarios}
          comments={post.lista_comentarios}
        />
      ))}
      <div className="recommendations-section-text">
        <h2>Recomendações</h2>
        <CiStar size={30} />
      </div>
      {recommended_posts.map((post, index) => (
        <Post
          key={index}
          id={post.id}
          user_id={'1'}
          time={post.time}
          liked={false}
          image={post.midia}
          caption={post.conteudo}
          username={post.nome}
          num_likes={post.curtidas}
          num_shares={0}
          num_comments={post.comentarios}
          comments={post.listas_comentarios}
        />
      ))}
    </div>
  )
}

export default FeedPosts
