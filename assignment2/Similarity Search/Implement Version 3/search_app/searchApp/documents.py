from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Car
from .models import Neighbor


@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'similartest'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Car  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'similarity',
            'master_pi',
            'similar_pi',
        ]


@registry.register_document
class NeighborDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'neighbors'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Neighbor  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'similarity',
            'master_pi',
            'master_url',
            'similar_pi',
            'similar_url',
        ]
