import sys
import markdown2
from markdown2 import Markdown
import frontmatter
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

dir = f'./MD/taiex.md'

post = frontmatter.load(dir)

post_title = post.metadata['title']

markdowner = Markdown()
post_content_html = markdowner.convert(post.content)
post_content_html = post_content_html.encode("utf-8")

wp = Client('https://i-stock.xyz/xmlrpc.php', 's02260441', 'simontp6nm06')

post = WordPressPost()
post.post_status = 'publish'
post.title = post_title
post.content =post_content_html
post.slug = post_title
post.terms_names = {
    'category' : ['台股晨訊']
}

wp.call(NewPost(post))