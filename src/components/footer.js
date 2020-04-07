import React from 'react'
import PropTypes from "prop-types"

const Footer = ({ siteAuthor }) => (
  <div className="footer">
    <div className="footer-name">{siteAuthor}</div>
    <p className="footer-copyright">Copyright 2020</p>
  </div>
)

Footer.propTypes = {
  siteAuthor: PropTypes.string,
}

Footer.defaultProps = {
  siteAuthor: ``,
}


export default Footer
