import React from 'react'
import Link from 'gatsby-link'

const Menu = () => (
    <div>
      <ul style={{
        listStyle: 'none',
        display: 'flex',
        justifyContent: 'space-evenly',
        background: '#f4f4f4',
        marginTop: `0rem`,
        height: `3rem`,
        padding: `15px 0px`,
        backgroundColor: `#777`,
      }}>
        <li><Link className="menu-link" to="/">Home</Link></li>
        <li><Link className="menu-link" to="/about">About</Link></li>
        <li><Link className="menu-link" to="/services">Services</Link></li>
        <li><Link className="menu-link" to="/blog">Blog</Link></li>
      </ul>
    </div>
  )

export default Menu