import './Feed.css'
import React from 'react'

import { CiGrid2H } from 'react-icons/ci'
import { RiUserStarLine } from 'react-icons/ri'
import { Link, useLocation } from 'react-router-dom'
import FeedRoutes from './feedRoutes'

function Feed() {
  const location = useLocation()

  const navItems = [
    { path: '/', icon: <CiGrid2H size={24} /> },
    { path: '/recommendations', icon: <RiUserStarLine size={24} /> },
  ]

  return (
    <div className="Feed">
      <div className="feed-nav">
        {navItems.map(item => (
          <Link
            to={item.path}
            className={`feed-nav-item ${location.pathname === item.path ? 'active' : ''
              }`}
          >
            {item.icon}
          </Link>
        ))}
      </div>
      <FeedRoutes />
    </div>
  )
}

export default Feed
