import './CriaPost.css'
import axios from 'axios'
import { React, useState } from 'react'

import { CiImageOn } from 'react-icons/ci'
import { IoIosCamera } from 'react-icons/io'
import { FaPhotoVideo } from 'react-icons/fa'
import { IoNewspaperOutline } from 'react-icons/io5'

function CriaPost() {
  const [selectedOption, setSelectedOption] = useState('publicacao')

  const [formData, setFormData] = useState({
    type: selectedOption,
    media: null,
    text: '',
    caption_create: '',
  })

  const handleChange = e => {
    const { name, value } = e.target
    setFormData({ ...formData, [name]: value })
  }

  const handleChangeOption = e => {
    const value = e.target.value
    setSelectedOption(value)
    setFormData({ ...formData, type: value })
  }

  // const handleFileChange = e => {
  //   const file = e.target.files[0]

  //   if (file && file.type.startsWith('image/')) {
  //     const reader = new FileReader()
  //     reader.onloadend = () => {
  //       setFormData({ ...formData, media: reader.result })
  //     }
  //     reader.readAsDataURL(file)
  //   }
  // }

  const handleSubmit = e => {
    e.preventDefault()

    const json_post = {
      conteudo: formData.caption_create,
      midia: formData.media,
      id_usuario: 1,
      data: '',
    }

    axios
      .post('http://localhost:8000/api/novo-post/', json_post, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        console.log('Response:', response.data)
        alert('Post enviado com sucesso!')
      })
      .catch(error => {
        console.error('Erro ao enviar o post:', error)
        alert('Erro ao enviar o post:', error)
      })
  }

  return (
    <form onSubmit={handleSubmit} id="cria-post-form">
      <div className="info-text">
        <h3>Crie um novo post</h3>
        <p>Compartilhe com a rede suas atualizações</p>
      </div>
      <div className="post-info">
        <div className="select-type">
          <p className="label-info">Selecione o tipo de post</p>
          <div className="types">
            <button
              type="button"
              value="publicacao"
              className={`type-button ${
                selectedOption === 'publicacao' ? 'active' : ''
              }`}
              onClick={handleChangeOption}
            >
              <FaPhotoVideo size={18} />
              Publicação
            </button>
            <button
              type="button"
              className={`type-button ${
                selectedOption === 'resenha' ? 'active' : ''
              }`}
              onClick={handleChangeOption}
              disabled
            >
              <IoNewspaperOutline size={18} />
              Resenha
            </button>
          </div>
        </div>
        <div className="media-text">
          <p className="label-info">Upload de mídia</p>
          <label htmlFor="fileInput" className="file-button">
            <IoIosCamera size={20} /> Insira a url para ver a prévia
          </label>
          <input
            type="text"
            id="fileInput"
            name="media"
            value={formData.media || ''}
            onChange={handleChange}
            placeholder="Cole o link da imagem aqui..."
          />

          {formData.media ? (
            <img src={formData.media} alt="Prévia da mídia" />
          ) : (
            <CiImageOn size={200} id="image-placeholder" />
          )}
        </div>
      </div>
      <div className="legenda">
        <label htmlFor="caption_create" className="label-info">
          Legenda
        </label>
        <textarea
          id="caption_create"
          name="caption_create"
          value={formData.caption_create}
          onChange={handleChange}
          rows="4"
          placeholder="Digite sua legenda aqui..."
        ></textarea>
      </div>
      <button type="submit" id="submit-button">
        Publicar
      </button>
    </form>
  )
}

export default CriaPost
