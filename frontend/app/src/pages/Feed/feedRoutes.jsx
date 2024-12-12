import { Routes, Route } from 'react-router-dom'

import FeedPosts from '../../components/feedPosts/FeedPosts'
import Recommendations from '../../components/recommendations/Recommendations'

const FeedRoutes = () => {
  return (
    <Routes>
      <Route path="" element={<FeedPosts />} />
      <Route path="recommendations" element={<Recommendations />} />
    </Routes>
  )
}

export default FeedRoutes
