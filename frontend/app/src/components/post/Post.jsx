import './Post.css'
import React from 'react'

import { AiFillLike } from 'react-icons/ai'
import { AiOutlineLike } from 'react-icons/ai'
import { BsPersonCircle } from 'react-icons/bs'
import { FaRegCommentAlt } from 'react-icons/fa'
import { RiShareForwardLine } from 'react-icons/ri'
import { HiOutlineDotsHorizontal } from 'react-icons/hi'

const Post = ({
  liked,
  time,
  num_likes,
  num_shares,
  num_comments,
  username,
  image,
  caption,
}) => {
  return (
    <div className="Post">
      <div className="header">
        <div className="l-container">
          <BsPersonCircle size={26} />
          <div className="username-container">
            <p id="user">{username}</p>
            <p id="time">{time}</p>
          </div>
        </div>
        <div className="r-container">
          <HiOutlineDotsHorizontal size={20} />
        </div>
      </div>
      <img src={image} alt="my-post" width={600} />
      <div className="footer">
        <div className="interactions">
          {liked ? (
            <AiFillLike className="interaction" size={24} />
          ) : (
            <AiOutlineLike className="interaction" size={24} />
          )}
          <FaRegCommentAlt className="interaction" size={24} />
          <RiShareForwardLine className="interaction" size={24} />
        </div>
        <div className="text">
          <p id="user">{username}</p>
          <p id="caption">{caption}</p>
        </div>
      </div>
    </div>
  )
}

export default Post
