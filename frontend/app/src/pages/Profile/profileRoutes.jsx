import { Routes, Route } from 'react-router-dom'

import Posts from '../../components/post/Post'
import Lists from '../../components/list/Lists'
import Resenhas from '../../components/resenha/Resenha'

const ProfileRoutes = () => {
  return (
    <Routes>
      <Route path="" element={<Posts />} />
      <Route path="lists" element={<Lists />} />
      <Route path="resenhas" element={<Resenhas />} />
    </Routes>
  )
}

export default ProfileRoutes
