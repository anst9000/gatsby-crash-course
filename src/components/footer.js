import React from "react"
import PropTypes from "prop-types"

const Footer = ({ siteAuthor }) => {
  const { name, email, copyright } = siteAuthor

  return (
    <div className="footer">
      <div className="footer-name">{name}</div>
      <div className="footer-name">{email}</div>
      <p className="footer-copyright">{copyright}</p>
    </div>
  )
}

Footer.propTypes = {
  siteAuthor: PropTypes.string,
}

Footer.defaultProps = {
  siteAuthor: ``,
}

export default Footer
