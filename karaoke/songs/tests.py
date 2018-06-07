from django.core.urlresolvers import reverse
from django.test import TestCase


from .models import Performer, Song


class PerformerModelTests(TestCase):
    def test_performer_string(self):
        '''String version of Performer should be Performer's name attribute'''
        perf = Performer.objects.create(name='Mike the Frog')
        self.assertEqual(str(perf), perf.name)


class SongModelTests(TestCase):
    def setUp(self):
        self.performer = Performer.objects.create(name='Andrew Chalkley')

    def test_song_string(self):
        '''String version of Song should contain the title and artist'''
        song = Song.objects.create(
            title="Don't Stop Believing",
            artist="Journey",
            length=250,
            performer=self.performer)
        self.assertIn(song.title, str(song))
        self.assertIn(song.artist, str(song))


class ViewTests(TestCase):
    def setUp(self):
        self.performer = Performer.objects.create(name='Craig Dennis')
        self.song = Song.objects.create(
            title='I Wanna Be Sedated',
            artist='The Ramones',
            length=149,
            performer=self.performer)

    def test_song_list_view(self):
        '''The song_list view should:
           * return a 200
           * have self.song in the context
           * use the songs/song_list.html template
        '''
        resp = self.client.get(reverse('songs:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.song, resp.context['songs'])
        self.assertTemplateUsed(resp, 'songs/song_list.html')

    def test_song_detail_view(self):
        '''The song_detail view should:
           * return a 200
           * have self.song in the context
           * use the songs/song_detail.html template
        '''
        resp = self.client.get(reverse('songs:detail',
                                       kwargs={'pk': self.song.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['song'], self.song)
        self.assertTemplateUsed(resp, 'songs/song_detail.html')

    def test_performer_detail_view(self):
        '''The performer_detail view should:
           * return a 200
           * have self.performer in the context
           * use the songs/performer_detail.html template
           * show the string version of self.song in the template
        '''
        resp = self.client.get(reverse('songs:performer',
                                       kwargs={'pk': self.performer.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['performer'], self.performer)
        self.assertTemplateUsed(resp, 'songs/performer_detail.html')
        self.assertContains(resp, str(self.song))