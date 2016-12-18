from django import test
from django.core.urlresolvers import reverse
from foo.urls import urlpatterns

class UrlsTest(test.TestCase):
    def test_responses(self):
        for url in urlpatterns:
            response = self.client.get(reverse(url.name))
            self.assertEqual(response.status_code, 200)