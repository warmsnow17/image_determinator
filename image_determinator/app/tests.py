import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from PIL import Image as PILImage

from app.forms import ImageUploadForm
from app.image_determinator import image_determinator

from app.models import Image
from image_determinator.settings import MEDIA_ROOT


class ImageUploadFormTest(TestCase):
    def test_form_with_valid_data(self):
        path_to_image = 'media/images/longhairedgermanshepherd4_B8KezbA.jpg'
        with open(path_to_image, 'rb') as image_file:
            uploaded_file = SimpleUploadedFile(name='test_image.jpg',
                                               content=image_file.read(),
                                               content_type='image/jpeg')
            form = ImageUploadForm(data={}, files={'image': uploaded_file})
            self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = ImageUploadForm(data={}, files={})
        self.assertFalse(form.is_valid())


class ImageDeterminatorTest(TestCase):
    def test_image_determinator(self):
        path_to_image = 'media/images/longhairedgermanshepherd4_B8KezbA.jpg'
        pil_image = PILImage.open(path_to_image)
        width, height, result = image_determinator(path_to_image)
        self.assertEqual((width, height), pil_image.size)
        self.assertIsInstance(result, str)


class ImageModelTest(TestCase):
    def test_create_image(self):
        path_to_image = 'media/images/longhairedgermanshepherd4_B8KezbA.jpg'
        with open(path_to_image, 'rb') as image_file:
            uploaded_file = SimpleUploadedFile(name='test_image.jpg',
                                               content=image_file.read(),
                                               content_type='image/jpeg')
            image = Image.objects.create(image=uploaded_file)
            self.assertTrue(os.path.isfile(os.path.join(MEDIA_ROOT, image.image.name)))
            self.assertEqual(image.result, '')


class UploadImageViewTest(TestCase):
    def test_upload_image_view_with_GET(self):
        response = self.client.get(reverse('upload_image'))
        self.assertEqual(response.status_code, 200)

    def test_upload_image_view_with_POST(self):
        path_to_image = 'media/images/longhairedgermanshepherd4_B8KezbA.jpg'
        with open(path_to_image, 'rb') as image_file:
            uploaded_file = SimpleUploadedFile(name='test_image.jpg',
                                               content=image_file.read(),
                                               content_type='image/jpeg')
            images_before = Image.objects.count()
            response = self.client.post(reverse('upload_image'),
                                        data={'image': uploaded_file})
            images_after = Image.objects.count()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(images_after, images_before + 1)
