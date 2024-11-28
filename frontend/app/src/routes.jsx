import { Routes, Route } from 'react-router-dom'

import Error from './pages/Error'
import Feed from './pages/Feed/Feed'
import Profile from './pages/Profile/Profile'
import Pesquisa from './pages/Pesquisa/Pesquisa'
import BatePapo from './pages/BatePapo/BatePapo'
import CriaPost from './pages/CriaPost/CriaPost'
import Comunidade from './pages/Comunidade/Comunidade'

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Feed />} />
      <Route path="*" element={<Error />} />
      <Route path="/profile/*" element={<Profile />} />
      <Route path="/pesquisa" element={<Pesquisa />} />
      <Route path="/bate-papo" element={<BatePapo />} />
      <Route path="/cria-post" element={<CriaPost />} />
      <Route path="/comunidade" element={<Comunidade />} />
    </Routes>
  )
}

export default AppRoutes
