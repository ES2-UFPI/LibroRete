import './ProfilePosts.css'
import React from 'react'

import ProfilePostItem from '../ProfilePostItem/ProfilePostItem'

const ProfilePosts = () => {
  const posts = [
    {
      media:
        'https://gratisography.com/wp-content/uploads/2024/03/gratisography-funflower-800x525.jpg',
      id: '1',
    },
    {
      media:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw1abqacQ-yPtTfIcXPVCrXTRo24o61MjN3A&s',
      id: '2',
    },
    {
      media:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXJA32WU4rBpx7maglqeEtt3ot1tPIRWptxA&s',
      id: '3',
    },
    {
      media:
        'https://gratisography.com/wp-content/uploads/2024/03/gratisography-funflower-800x525.jpg',
      id: '4',
    },
    {
      media:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw1abqacQ-yPtTfIcXPVCrXTRo24o61MjN3A&s',
      id: '5',
    },
    {
      media:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXJA32WU4rBpx7maglqeEtt3ot1tPIRWptxA&s',
      id: '5',
    },
    {
      media:
        'https://gratisography.com/wp-content/uploads/2024/03/gratisography-funflower-800x525.jpg',
      id: '6',
    },
    {
      media:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw1abqacQ-yPtTfIcXPVCrXTRo24o61MjN3A&s',
      id: '7',
    },
    {
      media:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXJA32WU4rBpx7maglqeEtt3ot1tPIRWptxA&s',
      id: '8',
    },
  ]

  return (
    <div className="ProfilePostContent">
      <div className="profile-posts">
        {posts.map((post, index) => (
          <ProfilePostItem key={index} media={post.media} id={post.id} />
        ))}
      </div>
    </div>
  )
}

export default ProfilePosts
