import * as React from "react"
import PropTypes from "prop-types"
import { Link } from "gatsby"
import { useStaticQuery, graphql } from "gatsby"
import rabbit from "../images/logo_rabbit.png"

const Header = ({ siteTitle }) => {
  const data = useStaticQuery(graphql`
    query SiteHeaderTitleQuery {
      site {
        siteMetadata {
          title
        }
      }
    }
  `)

  return (
    <header>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img
              src={rabbit}
              style={{ margin: ".25rem 1.25rem .25rem 1rem" }}
              className="image-rabbit"
              width={60}
              height={60}
              alt="Logo"
            />
          </Link>
          <h2 style={{ color: `white` }}>{data.site.siteMetadata.title}</h2>

          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarColor03"
            aria-controls="navbarColor03"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarColor03">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link ps-3" activeClassName="active" to="/">
                  Home
                  <span className="visually-hidden">(current)</span>
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className="nav-link ps-3"
                  activeClassName="active"
                  to="/about"
                >
                  About
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className="nav-link ps-3"
                  activeClassName="active"
                  to="/blog"
                >
                  Blog
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  )
}

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header
