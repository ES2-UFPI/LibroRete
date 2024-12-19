import './UserRecommendation.css'
import React from 'react'

const UserRecommendation = ({ username, photo }) => {
  return (
    <div className="User">
      <img src={photo} alt="my-photo" />
      <h5>{username}</h5>
      <button id="rec-follow-button">Seguir</button>
    </div>
  )
}

export default UserRecommendation
