import './NavBar.css'

import { FaPlus } from 'react-icons/fa6'
import { HiUserGroup } from 'react-icons/hi'
import { BsPersonCircle } from 'react-icons/bs'
import { Link, useLocation } from 'react-router-dom'
import { IoMdHome, IoMdSearch, IoIosChatbubbles } from 'react-icons/io'

function NavBar() {
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Feed', icon: <IoMdHome size={24} /> },
    { path: '/pesquisa', label: 'Pesquisar', icon: <IoMdSearch size={24} /> },
    { path: '/cria-post', label: 'Criar Post', icon: <FaPlus size={24} /> },
    {
      path: '/bate-papo',
      label: 'Bate-papos',
      icon: <IoIosChatbubbles size={24} />,
    },
    {
      path: '/comunidade',
      label: 'Comunidades',
      icon: <HiUserGroup size={24} />,
    },
    { path: '/profile', label: 'Perfil', icon: <BsPersonCircle size={24} /> },
  ]

  return (
    <div className="NavBar">
      {navItems.map(item => (
        <Link
          to={item.path}
          key={item.label}
          className={`nav-item ${
            location.pathname === item.path ? 'active' : ''
          }`}
        >
          {item.icon}
          <span className="nav-label">{item.label}</span>
        </Link>
      ))}
    </div>
  )
}

export default NavBar
