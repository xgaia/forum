from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Thread, Message

def create_user(name):
	return User.objects.create_user(name, "{}@tmp.org".format(name), name)

def create_thread(name, description, author):
    return Thread.objects.create(name=name, description=description, author=author)

def create_comment(message, thread, author):
    return Message.objects.create(message=message, thread=thread, author=author)


class ThreadViewTests(TestCase):

    def test_no_thread(self):
        """
        If no thread exist, no thread are returned
        """
        response = self.client.get(reverse('forum:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['threads'], [])

    def test_one_thread(self):
        """
        If one thread exist, one thread is returned
        """
        user = User.objects.create_user('temporary', 'temporary@tmp.com', 'temporary')
        thread = create_thread("test", "a thread", user)
        response = self.client.get(reverse('forum:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['threads'], [thread])


class CommentViewTests(TestCase):

    def test_no_comment(self):
        """
        If no thread exist, no thread are returned
        """
        user = create_user("test")
        thread = create_thread("test", "a thread", user)
        response = self.client.get(reverse('forum:detail', args=(thread.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['thread'], thread)

    def test_one_comment(self):
        """
        If no thread exist, no thread are returned
        """
        user = create_user("test")
        thread = create_thread("test", "a thread", user)
        comment = create_comment("message", thread, user)
        response = self.client.get(reverse('forum:detail', args=(thread.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['thread'], thread)
        self.assertQuerysetEqual(response.context['thread'].messages.all(), [comment])
