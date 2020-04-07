import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <h1>Coding from Python to Gatsby.</h1>
    <p>I will share with you my thoughts, daily encounters, strugglings with coding and evertything that matters to me.</p>
    <p>Currently I have approximately 3 months left of the university program in Computer Science.</p>
    <p>So of course this will be part of my tips and tricks and how-tos presented here.</p>
    <div>
      <Image />
    </div>
  </Layout>
)

export default IndexPage
