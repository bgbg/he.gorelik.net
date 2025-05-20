# he.gorelik.net
https://he.gorelik.net

## Environment Setup (One-time)
Install `chruby`. (This is optional, useful for if you are managing multiple versions of Ruby)

On mac:
```
$ brew install ruby-install chruby
```
Add the following to `~/.zshrc`, making sure to choose the latest version of Ruby in the last line.

```
# enable chruby
source /usr/local/share/chruby/chruby.sh
source /usr/local/share/chruby/auto.sh
chruby ruby-3.3.3
```

Ensure you have the Jekyll requirements installed as listed here:
https://jekyllrb.com/docs/installation/

This site was developed using Ruby 3.3.3.

Here's how to install this specific version using ruby-install from the first step:
```
$ ruby-install ruby 3.3.3
```

Verify this worked by running `ruby -v`.

In the root directory of this project, run `bundle install` to install project dependencies.

Now, to run a local development server, run:
```
bundle exec jekyll serve
```

and the site will be hosted at `http://localhost:4000`

## Description of important files and directories
The configuration for this site is found in the _config.yml file. This is where
site-wide data is defined, such as the URL, the site title, permalink and collection url formats, and
navigation pages.

Generally, Jekyll knows to process files that start with a front matter block: https://jekyllrb.com/docs/front-matter/
Jekyll website content can be defined in either markdown or html pages.

The Jekyll documentation on pages and posts is very thorough. More details are here:
* https://jekyllrb.com/docs/pages/
* https://jekyllrb.com/docs/posts/

Important directories to know:
* `_drafts` - draft posts or pages that are not published when the site is built
* `_layouts` - each file in here is a different layout you can use for a page, as defined in the page or post's front matter
* `_my_categories` - each file represents a blog category, necessary for generating each /category/category-name page
* `_my_tags` - each file represents a blog tag, necessary for generating each /tag/tag-name page
* `_posts` - blog posts are here. Currently organized by year published
* `assets` - where documents, icons, images, javascript and css files live
* `blog` - simply holds the landing page for the list of all blog posts at /blog

Site pages (not blog posts) are generally found in the root directory of this project, including the index.md file.

## Note on Categories and Tags

One interesting note is that for blog posts, you can specify tags and categories in the frontmatter, but if you
are creating a new tag or category, Jekyll does not automatically create a page at /tag/tag-name/
or /category/category-name/ for you.  You must create a file for each new tag or category in
`_my_categories` or `_my_tags` containing this frontmatter:
```
---
name: "new-tag-name-here"
slug: "new-tag-slug-here"
---
```
Once you do that, and the blog posts have the relevant tags or categories in their frontmatter,
they will appear the tag/category page that matches the correct tag/category.

The tags and categories are known as a Jekyll "collection" data structure.

## Creating a new blog post
All of the old WordPress posts were exported to Markdown, but new blog posts may be either Markdown or HTML. The Jekyll documentation
is pretty good https://jekyllrb.com/docs/posts/ , but here are some notes specific to this site:

To add new images to a post, first put the images in the `assets/img` directory. WordPress organized photos using the
`YYYY/MM` structure, so that's how the old photos were imported here, but going forward you may designate a new organization scheme
if desired. To add them to a post, you may use this structure: `![My helpful screenshot]({{ site.baseurl }}/assets/img/2025/05/screenshot.jpg)`
The `{{ site.baseurl }}` is a Liquid tag that will automatically pull your URL from the _config.yml file.
The image will default to using the full width of the space available, so if you would like to limit the size or alignment of the image,
you can use something like this: `![My helpful screenshot]({{ site.baseurl }}/assets/img/2025/05/screenshot.jpg){:width="50"}{:class="alignleft"}`
This example will make the image 50px wide and align the photo to the left of the page.

## Publishing updates to GitHub Pages
GitHub pages supports Jekyll by default, but it only allows a certain version of Jekyll and a certain list of plugins. The theme that
was imported does not work with those defaults, so the workaround is to define a custom Git Workflow to publish the site. The configuration
for this is found at `.github/workflows/jekyll.yml`.

To enable publishing through this workflow, go to Settings > Pages > Build & Deployment > Source and choose GitHub Actions. No need to create a new
workflow here, it should use the one defined in the repo.
