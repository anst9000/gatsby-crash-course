import React from "react"
import PropTypes from "prop-types"

const Footer = ({ siteAuthor }) => {
  const { name, email, copyright } = siteAuthor

  return (
    <footer className="footer">
      <div className="footer-name">{name}</div>
      <div className="footer-name">{email}</div>
      <p className="footer-copyright">{copyright}</p>
    </footer>
  )
}

Footer.propTypes = {
  siteAuthor: PropTypes.object,
}

Footer.defaultProps = {
  siteAuthor: ``,
}

export default Footer
