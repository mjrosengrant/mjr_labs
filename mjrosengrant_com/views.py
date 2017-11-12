"""Views for mjrosengrant.com."""

from pinax.blog.views import BlogIndexView, DateBasedPostDetailView


class IndexView(BlogIndexView):
    """Main landing page for site."""

    template_name = 'mjrosengrant_com/index.html'


class PostView(DateBasedPostDetailView):
    """View to read blog post."""

    template_name = 'mjrosengrant_com/post_detail.html'
