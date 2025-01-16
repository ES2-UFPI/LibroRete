import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import CriaPost from './CriaPost'

import axios from 'axios'

jest.mock('axios')

describe('Criação de Post', () => {
  test('Deve enviar dados corretamente e receber resposta da API', async () => {
    const mockResponse = { data: { message: 'Post enviado com sucesso!' } }
    axios.post.mockResolvedValue(mockResponse)

    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {})

    render(<CriaPost />)

    fireEvent.change(
      screen.getByPlaceholderText('Digite sua legenda aqui...'),
      {
        target: { value: 'Minha nova legenda!' },
      }
    )

    fireEvent.change(
      screen.getByPlaceholderText('Cole o link da imagem aqui...'),
      {
        target: {
          value:
            'https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png',
        },
      }
    )

    fireEvent.click(screen.getByText('Publicar'))

    await waitFor(() => expect(axios.post).toHaveBeenCalledTimes(1))

    const json_post = {
      conteudo: 'Minha nova legenda!',
      midia:
        'https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png',
      id_usuario: '1',
      data: '',
    }

    expect(axios.post).toHaveBeenCalledWith(
      'http://localhost:8000/api/novo-post/',
      json_post,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    )

    await waitFor(() => {
      expect(alertSpy).toHaveBeenCalledWith('Post enviado com sucesso!')
    })

    alertSpy.mockRestore()
  })

  test('Deve exibir erro se a requisição falhar', async () => {
    const error = new Error('Erro ao enviar o post')
    axios.post.mockRejectedValue(error)

    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {})

    render(<CriaPost />)

    fireEvent.change(
      screen.getByPlaceholderText('Digite sua legenda aqui...'),
      {
        target: { value: 'Outra legenda!' },
      }
    )

    fireEvent.change(
      screen.getByPlaceholderText('Cole o link da imagem aqui...'),
      {
        target: {
          value:
            'https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png',
        },
      }
    )

    fireEvent.click(screen.getByText('Publicar'))

    await waitFor(() => {
      expect(alertSpy).toHaveBeenCalledWith('Erro ao enviar o post:', error)
    })

    alertSpy.mockRestore()
  })
})
