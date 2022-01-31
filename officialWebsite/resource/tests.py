from django.test import TestCase
from officialWebsite.resource.models import resource
from officialWebsite.topic.models import topic


def create_resource():
    return resource.objects.create(name="Test Resource", url="example.com")


def create_topic():
    return topic.objects.create(
        name="Test Topic",
    )


class TestResourceModel(TestCase):
    def setUp(self):
        resource_new = create_resource()
        topic_new = create_topic()
        resource_new.topic.add(topic_new)
        resource_new.save()
        self.resource_new = resource_new

    def test_resource_creation(self):
        """
        Test Resource creation
        """
        # topic_new = create_team()
        self.assertEqual(self.resource_new.name, "Test Team")
