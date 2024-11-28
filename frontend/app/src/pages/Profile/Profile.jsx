import './Profile.css'
import React from 'react'
import ProfileRoutes from './profileRoutes'

import { GrApps } from 'react-icons/gr'
import { IoList } from 'react-icons/io5'
import { BsPersonCircle } from 'react-icons/bs'
import { IoNewspaperOutline } from 'react-icons/io5'
import { Link, useLocation } from 'react-router-dom'

function Profile() {
  const location = useLocation()

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
          <BsPersonCircle id="photo" size={110} />
        </div>
        <div className="details-container">
          <h2>username</h2>
          <div className="info-numbers">
            <div className="number">
              <span>0</span>
              <p>publicações</p>
            </div>
            <div className="number">
              <span>0</span>
              <p>seguidores</p>
            </div>
            <div className="number">
              <span>0</span>
              <p>seguindo</p>
            </div>
          </div>
          <div className="info-text">
            <h3>Name</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            <p>Terror, Romance</p>
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
