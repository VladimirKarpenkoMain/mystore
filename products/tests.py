from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory
from users.models import User


class ProductsViewTestCase(TestCase):
    fixtures = ['categories.json', 'products.json']

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        products = Product.objects.all()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']),
                         list(products.filter(category_id=category.id))
                         )
