import { render, screen, fireEvent } from '@testing-library/react'
import ProfilePostItem from './ProfilePostItem'
import '@testing-library/jest-dom/extend-expect' // Para usar as matchers como "toBeInTheDocument"

describe('ProfilePostItem', () => {
  test('Deve renderizar o post corretamente', () => {
    const media =
      'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXJA32WU4rBpx7maglqeEtt3ot1tPIRWptxA&s'
    const id = '1'

    render(<ProfilePostItem media={media} id={id} alt="post de teste" />)

    // Verificar se o post está presente no DOM
    const postElement = screen.getByAltText(/post de teste/i)
    expect(postElement).toHaveAttribute('src', media)
  })

  test('Deve exibir o alerta com o media e o id após clicar no post', () => {
    const media =
      'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXJA32WU4rBpx7maglqeEtt3ot1tPIRWptxA&s'
    const id = '1'

    const postData = {
      media: media,
      id: id,
    }
    const alertText = JSON.stringify(postData, null, 2)

    render(<ProfilePostItem media={media} id={id} alt="post de teste" />)

    // Obter o post e clicar nele
    const postElement = screen.getByAltText(/post de teste/i)
    fireEvent.click(postElement)

    // Verificar se o alerta foi chamado após o clique
    expect(global.alert).toHaveBeenCalledTimes(1) // Verifica se o alert foi chamado uma vez
    expect(global.alert).toHaveBeenCalledWith(alertText) // Verifica se o alert foi chamado com o texto correto
  })
})
