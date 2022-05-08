import React from "react"
import Link from "gatsby-link"
import { graphql } from "gatsby"

import Layout from "../components/layout"

export default function Template({ data }) {
  const post = data.markdownRemark
  const { title, author, date, content, code } = post.frontmatter
  const { html } = post.html

  return (
    <Layout>
      <div className="container">
        <div className="single-blog-header">
          <h1 className="single-blog">{title}</h1>
          <Link className="btn btn-secondary" to="/blog">
            Go Back
          </Link>
        </div>
        <h4>
          {author} on {date}
        </h4>
        <div className="single-blog-content">{content}</div>
        <div className="code-snippet">{code}</div>
      </div>
    </Layout>
  )
}

export const postQuery = graphql`
  query BlogPostByPath($path: String!) {
    markdownRemark(frontmatter: { path: { eq: $path } }) {
      html
      frontmatter {
        path
        title
        author
        summary
        date
        content
        code
      }
    }
  }
`
