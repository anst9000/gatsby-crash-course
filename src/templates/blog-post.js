import React from 'react'
import Link from 'gatsby-link'

import Layout from "../components/layout"


export default function Template({data}) {
  const post = data.markdownRemark

  return(
  <Layout>
    <div class="container">
      <div class="single-blog-header">
        <h1 className="single-blog-header">{post.frontmatter.title}</h1>
        <Link className="button back-link" to="/blog">Go Back</Link>
      </div>
      <h4>Posted by {post.frontmatter.author} on {post.frontmatter.date}</h4>
      <div className="code-snippet" dangerouslySetInnerHTML={{ __html: post.html }} />
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