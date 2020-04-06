import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <h1>Everything worth knowing about coding and rabbits.</h1>
    <p>If you want to read about my thoughts, daily encounters, strugglings with coding and evertything that matters to me.</p>
    <p>Currently I have approximately 3 months left of the university program in Computer Science.</p>
    <p>So of course I will share all my tips and tricks and how-tos with you.</p>
    <p>But I plan to balance this with some content from the 'real world' also.</p>
    <p>My rabbit Skrutte is a wonderful animal and filled with joy and funny small projects.</p>
    <div style={{ maxWidth: `300px`, marginBottom: `1.45rem` }}>
      <Image />
    </div>
  </Layout>
)

export default IndexPage
