from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile,Comment


# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        self.user = User.objects.create_user("vector", "pass")
        self.profile_test = Profile(profile_picture='images/default.png',
                                            bio="test bio",
                                            user=self.user)
        self.profile_test.save()

    def test_instance_true(self):
        self.profile_test.save()
        self.assertTrue(isinstance(self.profile_test, Profile))


class ImageTestClass(TestCase):
    """test class for Image model"""

    def setUp(self):

        self.user = User.objects.create_user("vector", "pass")

        self.new_profile = Profile(profile_picture='images/default.png',bio="test bio",
                                     user=self.user)
        self.new_profile.save()

        self.new_image = Image(image='images/ford.png',
                               caption="image", name='ford', author=self.user)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()



class CommentTestClass(TestCase):

    """Test class for Comment Model"""

    def setUp(self):
        self.new_user = User.objects.create_user("vector", "pass")

        self.new_profile = Profile(profile_picture='images/default.png',
                                     bio="test bio",
                                     user=self.new_user)
        self.new_profile.save()

        self.new_image = Image(pic='images/ford.jpg',
                               caption="test image", caption='cool car',author=self.new_user)
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, name=self.new_profile, comment="this is a  test comment on a post")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()

