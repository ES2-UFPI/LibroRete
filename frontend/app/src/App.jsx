import './App.css'
import React from 'react'
import AppRoutes from './routes'
import NavBar from './components/navbar/NavBar'

function App() {
  return (
    <>
      <NavBar />
      <div className="content">
        <AppRoutes />
      </div>
    </>
  )
}

export default App
