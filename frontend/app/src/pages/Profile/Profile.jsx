import React from 'react'
import './Profile.css'

import { GrApps } from 'react-icons/gr'
import { IoList } from 'react-icons/io5'
import { BsPersonCircle } from 'react-icons/bs'
import { IoNewspaperOutline } from 'react-icons/io5'

function Profile() {
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
          <div className="bar-item">
            <GrApps className="bar-icon" size={15} />
            <span className="bar-label">PUBLICAÇÕES</span>
          </div>
          <div className="bar-item">
            <IoNewspaperOutline className="bar-icon" size={15} />
            <span className="bar-label">RESENHAS</span>
          </div>
          <div className="bar-item">
            <IoList className="bar-icon" size={15} />
            <span className="bar-label">LISTAS</span>
          </div>
        </div>
        <div className="posts">
          <h3>Não há publicações</h3>
        </div>
      </div>
    </>
  )
}

export default Profile
