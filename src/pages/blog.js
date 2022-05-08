import React from "react"
import { Link } from "gatsby"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const BlogPage = ({ data }) => {
  return (
    <Layout>
      <SEO title="Blog" />
      <h1>Latest Posts</h1>
      {data.allMarkdownRemark.edges.map(post => {
        const { id } = post.node
        const { title, summary, path, author, date } = post.node.frontmatter

        return (
          <div className="card" key={id}>
            <div className="container">
              <h3>
                <b>{title}</b>
              </h3>
              <hr />
              <p>{summary}</p>
              <br />
              <div className="card-bottom">
                <Link className="btn btn-primary" to={path}>
                  Read More
                </Link>
                <small className="author">
                  {author} on {date}
                </small>
              </div>
            </div>
          </div>
        )
      })}
    </Layout>
  )
}

export const pageQuery = graphql`
  query BlogIndexQuery {
    allMarkdownRemark(sort: { fields: [frontmatter___date], order: DESC }) {
      edges {
        node {
          id
          frontmatter {
            path
            date
            title
            summary
            author
          }
        }
      }
    }
  }
`

export default BlogPage
