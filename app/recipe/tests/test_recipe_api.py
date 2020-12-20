from core.models import Recipe, Tag, Ingredient
from recipe.serializers import RecipeSerializer, RecipeDetailSerializer
from django.urls import reverse


RECIPES_URL = reverse('recipe:recipe-list')


def sample_tag(user, name='Main course'):
    """Create and return a sample tag"""
    return Tag.objects.create(user=user, name=name)


def sample_ingredient(user, name='Cinnamon'):
    """Create and return a sample ingredient"""
    return Ingredient.objects.create(user=user, name=name)


def detail_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-detail', args=[recipe_id])

...

def test_view_recipe_detail(self):
    """Test viewing a recipe detail"""
    recipe = sample_recipe(user=self.user)
    recipe.tags.add(sample_tag(user=self.user))
    recipe.ingredients.add(sample_ingredient(user=self.user))

    url = detail_url(recipe.id)
    res = self.client.get(url)

    serializer = RecipeDetailSerializer(recipe)
    self.assertEqual(res.data, serializer.data)

def test_create_basic_recipe(self):
    """Test creating recipe"""
    payload = {
        'title': 'Test recipe',
        'time_minutes': 30,
        'price': 10.00,
    }
    res = self.client.post(RECIPES_URL, payload)

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    recipe = Recipe.objects.get(id=res.data['id'])
    for key in payload.keys():
        self.assertEqual(payload[key], getattr(recipe, key))

def test_create_recipe_with_tags(self):
    """Test creating a recipe with tags"""
    tag1 = sample_tag(user=self.user, name='Tag 1')
    tag2 = sample_tag(user=self.user, name='Tag 2')
    payload = {
        'title': 'Test recipe with two tags',
        'tags': [tag1.id, tag2.id],
        'time_minutes': 30,
        'price': 10.00
    }
    res = self.client.post(RECIPES_URL, payload)

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    recipe = Recipe.objects.get(id=res.data['id'])
    tags = recipe.tags.all()
    self.assertEqual(tags.count(), 2)
    self.assertIn(tag1, tags)
    self.assertIn(tag2, tags)

def test_create_recipe_with_ingredients(self):
    """Test creating recipe with ingredients"""
    ingredient1 = sample_ingredient(user=self.user, name='Ingredient 1')
    ingredient2 = sample_ingredient(user=self.user, name='Ingredient 2')
    payload = {
        'title': 'Test recipe with ingredients',
        'ingredients': [ingredient1.id, ingredient2.id],
        'time_minutes': 45,
        'price': 15.00
    }

    res = self.client.post(RECIPES_URL, payload)

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    recipe = Recipe.objects.get(id=res.data['id'])
    ingredients = recipe.ingredients.all()
    self.assertEqual(ingredients.count(), 2)
    self.assertIn(ingredient1, ingredients)
    self.assertIn(ingredient2, ingredients)
