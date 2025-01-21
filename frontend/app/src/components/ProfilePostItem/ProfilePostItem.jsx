import './ProfilePostItem.css'
import ModalPost from '../modalPost/ModalPost'
import { React, useState } from 'react'

const ProfilePostItem = ({
  key,
  id,
  conteudo,
  midia,
  curtidas,
  comentarios,
  lista_comentarios,
  time,
  foto,
}) => {
  const post = {
    id: id,
    time: time,
    liked: false,
    midia: midia,
    conteudo: conteudo,
    nome: '@eduarda',
    curtidas: curtidas,
    comentarios: comentarios,
    lista_comentarios: lista_comentarios,
    foto: foto,
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
