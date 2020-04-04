---
path: "/post-six"
date: "2018-04-14"
title: "Trying to deploy to Netlify"
author: "Andy Strömberg"
---

Continuous deployment works by connecting a Git repository to a Netlify site and keeping the two in sync.

It works for plain static sites, but it's even more powerful when you're using a static site generator or a frontend build tool like webpack, Gulp, or Grunt.

Netlify will run your build command and deploy the result whenever you push to your Git repo. The benefits of Netlify's continuous deployment include:

No deploying without committing and pushing first
Easy collaboration through pull/merge requests
Fix a typo through your Git provider's web UI from your mobile
Edit content without code by using a static site CMS, Netlify CMS
