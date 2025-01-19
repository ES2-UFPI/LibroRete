import './FeedPosts.css'
import Post from '../post/Post'
import image1 from '../../imgs/img1.jpg'
import image2 from '../../imgs/img2.jpg'

import React from 'react'

const FeedPosts = () => {
  const posts = [
    {
      id: '1',
      user_id: '1',
      liked: false,
      time: 'há 1 h',
      num_likes: 150,
      num_shares: 10,
      num_comments: 0,
      username: 'booklover123',
      image_url: image1,
      caption: 'Acabei de terminar esse livro incrível! 📚✨ #leituradodia',
    },
    {
      id: '2',
      user_id: '1',
      liked: false,
      time: 'há 2 h',
      num_likes: 50,
      num_shares: 5,
      num_comments: 2,
      username: 'best_reader',
      image_url: image2,
      caption: 'Uma história cheia de emoção e mistério. Recomendo! 🕵️‍♂️💡',
    },
  ]

  return (
    <div className="FeedPostsContent">
      {posts.map((post, index) => (
        <Post
          key={index}
          id={post.id}
          user_id={post.user_id}
          time={post.time}
          liked={post.liked}
          image={post.image_url}
          caption={post.caption}
          username={post.username}
          num_likes={post.num_likes}
          num_shares={post.num_shares}
          num_comments={post.num_comments}
        />
      ))}
    </div>
  )
}

export default FeedPosts
