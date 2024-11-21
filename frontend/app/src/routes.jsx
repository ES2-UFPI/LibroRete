import Error from './pages/Error'
import Feed from './pages/Feed/Feed'
import Profile from './pages/Profile/Profile'
import BatePapo from './pages/BatePapo/BatePapo'
import Pesquisa from './pages/Pesquisa/Pesquisa'
import CriarPost from './pages/CriaPost/CriaPost'
import Comunidade from './pages/Comunidade/Comunidade'

import { Routes, Route } from 'react-router-dom'

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Feed />} />
      <Route path="*" element={<Error />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/pesquisa" element={<Pesquisa />} />
      <Route path="/bate-papo" element={<BatePapo />} />
      <Route path="/criar-post" element={<CriarPost />} />
      <Route path="/comunidade" element={<Comunidade />} />
    </Routes>
  )
}

export default AppRoutes
