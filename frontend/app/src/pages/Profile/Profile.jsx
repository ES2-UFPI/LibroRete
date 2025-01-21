import './Profile.css'
import React from 'react'
import axios from 'axios'
import ProfileRoutes from './profileRoutes'

import { GrApps } from 'react-icons/gr'
import { IoList } from 'react-icons/io5'
import { useEffect, useState } from 'react'
import { BsPersonCircle } from 'react-icons/bs'
import { IoNewspaperOutline } from 'react-icons/io5'
import { Link, useLocation } from 'react-router-dom'

function Profile() {
  const location = useLocation()
  const [data, setData] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/perfis/@eduarda?format=json')
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

  const barItems = [
    {
      path: '',
      label: 'PUBLICAÇÕES',
      icon: <GrApps size={15} />,
    },
    {
      path: 'resenhas',
      label: 'RESENHAS',
      icon: <IoNewspaperOutline size={15} />,
    },
    { path: 'lists', label: 'LISTAS', icon: <IoList size={15} /> },
  ]

  return (
    <>
      <div className="ProfileInfo">
        <div className="photo-container">
          {data['foto'] ? (
            <img id="photo" src={data['foto']} alt="Foto de perfil" />
          ) : (
            <BsPersonCircle id="photo" size={110} />
          )}
        </div>
        <div className="details-container">
          <h2>{data['username']}</h2>
          <div className="info-numbers">
            <div className="number">
              <span>{data['numero_posts']}</span>
              <p>publicações</p>
            </div>
            <div className="number">
              <span>{data['numero_seguidores']}</span>
              <p>seguidores</p>
            </div>
            <div className="number">
              <span>{data['numero_seguindo']}</span>
              <p>seguindo</p>
            </div>
          </div>
          <div className="info-text">
            <h3>{data['nome']}</h3>
            <p>{data['bio']}</p>
            <p>{data['interesses']}</p>
          </div>
        </div>
      </div>
      <div className="ProfileContent">
        <div className="bar">
          {barItems.map(item => (
            <Link
              to={item.path}
              key={item.label}
              className={`bar-item ${
                location.pathname === `/profile${item.path}` ||
                location.pathname === `/profile/${item.path}`
                  ? 'active'
                  : ''
              }`}
            >
              {item.icon}
              <span className="bar-label">{item.label}</span>
            </Link>
          ))}
        </div>
        <div className="profile-content">
          <ProfileRoutes />
        </div>
      </div>
    </>
  )
}

export default Profile
