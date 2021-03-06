from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from au_art.models import Author, Article


class TestAuArt(TestCase):
    def setUp(self):
        author = Author(name="Anonymous")
        author.save()
        self.article = Article(title="New Article", article="Such a wonderful day", author=author)
        self.article.save()

    def test_au_art_view(self):
        resp = self.client.get(reverse('homepage'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.article.title, resp.content.decode('utf8'))

