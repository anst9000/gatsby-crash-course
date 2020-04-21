import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const BlogPage = ({data}) => (
  <Layout>
    <SEO title="Blog" />
    <h1>Latest Posts</h1>
    {data.allMarkdownRemark.edges.map(post => (
      <div class="card" key={ post.node.id }>
        <div class="container">
          <h3><b>{post.node.frontmatter.title}</b></h3>
          <hr />
          <p>{post.node.frontmatter.summary}</p>
          <br/>
          <div class="card-bottom">
            <Link className="button" to={post.node.frontmatter.path}>Read More</Link>
            <small className="author">Posted by {post.node.frontmatter.author} on {post.node.frontmatter.date}</small>
          </div>
        </div>
      </div>
    ))}
  </Layout>
)

export const pageQuery = graphql`
  query BlogIndexQuery
  {
    allMarkdownRemark
    (
      sort: {
        fields: [frontmatter___date]
        order: DESC
      }
    )
    {
      edges
      {
        node
        {
          id
          frontmatter
          {
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
