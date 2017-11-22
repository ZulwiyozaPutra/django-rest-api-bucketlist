from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework import status

from .models import Bucketlist


class ModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='nerd'
        )
        self.bucketlist_name = 'Write world class code'
        self.bucketlist = Bucketlist(
            name=self.bucketlist_name,
            owner=user
        )

    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(
            username='nerd'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = {'name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse(viewname='create'),
            data=self.bucketlist_data,
            format='json'
        )

    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        response = new_client.get(
            path='/bucketlists/7/',
            format='json'
        )
        print('RESPONSE IS HERE:')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse(
                viewname='details',
                kwargs={'pk': bucketlist.id}
            ),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something newer'}
        response = self.client.put(
            reverse(
                viewname='details',
                kwargs={'pk': bucketlist.id},
            ),
            data=change_bucketlist,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse(
                viewname='details',
                kwargs={'pk': bucketlist.id},
            ),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

