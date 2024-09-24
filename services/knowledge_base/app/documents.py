# Регистрация документа для Elastic Search (для релевантного поиска в уч.материалах)
# Материал https://django-elasticsearch-dsl.readthedocs.io/en/latest/quickstart.html
# Cannot convert model field author to an Elasticsearch field! fix: https://stackoverflow.com/questions/57635588/django-throwing-error-cannot-convert-model-field-category-to-an-elasticsearch-f
# python3 manage.py search_index --rebuild
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document, fields
from KnowledgeBase.models import StudyMaterial, Subject, MaterialType
from users.models import User, Grade

@registry.register_document
class StudyMaterialDocument(Document):
    author = fields.ObjectField(properties={
        'first_name': fields.TextField(),
        'second_name': fields.TextField(),
        'last_name': fields.TextField(),
    })
    subject = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
    grade = fields.ObjectField(properties={
        'grade_number': fields.IntegerField(),
    })
    material_type = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
    class Index:
        name = 'study_material'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    class Django:
        model = StudyMaterial
        fields = ['title', 'description','views']

    related_models = [User, Grade, Subject, MaterialType]
    def save(self, **kwargs):
        return super().save(**kwargs)
    

        # Configure how the index should be refreshed after an update.
        # See Elasticsearch documentation for supported options:
        # https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-refresh.html
        # This per-Document setting overrides settings.ELASTICSEARCH_DSL_AUTO_REFRESH.
        # auto_refresh = False
