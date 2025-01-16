import './ProfilePostItem.css'
import React from 'react'

const ProfilePostItem = ({ media, id }) => {
  const handleClickProfilePostItem = () => {
    const postData = {
      media: media,
      id: id,
    }

    alert(JSON.stringify(postData, null, 2))
  }

  return (
    <img
      className="profile-post-img"
      src={media}
      id={id}
      alt="Imagem de post de perfil"
      onClick={handleClickProfilePostItem}
    />
  )
}

export default ProfilePostItem
