import './ProfilePostItem.css'
import ModalPost from '../modalPost/ModalPost'
import { React, useState } from 'react'

const ProfilePostItem = ({ midia, id, conteudo }) => {
  const post = {
    time: 'há 1h',
    liked: false,
    image: midia,
    caption: conteudo,
    username: 'eduarda',
    num_likes: 10,
    num_shares: 11,
    num_comments: 12,
  }
  const [isModalPostOpen, setIsModalPostOpen] = useState(false)

  const openModalPost = () => {
    setIsModalPostOpen(true)
  }

  const closeModalPost = () => {
    setIsModalPostOpen(false)
  }
  const handleClickProfilePostItem = () => {
    openModalPost()
  }

  return (
    <>
      <img
        className="profile-post-img"
        src={midia}
        id={id}
        alt="Imagem de post de perfil"
        onClick={handleClickProfilePostItem}
      />
      <ModalPost
        isOpen={isModalPostOpen}
        onClose={closeModalPost}
        post={post}
      ></ModalPost>
    </>
  )
}

export default ProfilePostItem
