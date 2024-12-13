import { Routes, Route } from 'react-router-dom'

import ProfilePosts from '../../components/profilePosts/ProfilePosts'
import Lists from '../../components/Lists/Lists'
import Resenhas from '../../components/resenhas/Resenhas'

const ProfileRoutes = () => {
  return (
    <Routes>
      <Route path="" element={<ProfilePosts />} />
      <Route path="lists" element={<Lists />} />
      <Route path="resenhas" element={<Resenhas />} />
    </Routes>
  )
}

export default ProfileRoutes
