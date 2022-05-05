import React from "react"
import Link from "gatsby-link"

import Layout from "../components/layout"

export default function Template({ data }) {
  const post = data.markdownRemark
  const { title, author, date } = post.frontmatter
  const { html } = post.html

  return (
    <Layout>
      <div class="container">
        <div class="single-blog-header">
          <h1 className="single-blog-header">{title}</h1>
          <Link className="btn btn-secondary" to="/blog">
            Go Back
          </Link>
        </div>
        <h4>
          {author} on {date}
        </h4>
        <div
          className="code-snippet"
          dangerouslySetInnerHTML={{ __html: html }}
        />
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
      }
    }
  }
`
