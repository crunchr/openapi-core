from openapi_spec_validator import default_handlers
from jsonschema.validators import RefResolver
from openapi_spec_validator.validators import Dereferencer
from openapi_core.schema.schemas.registries import SchemaRegistry
from openapi_core.schema.schemas.generators import SchemasGenerator
from ruamel.yaml import round_trip_load
from six import StringIO


class TestGenerators(object):

    def test_schema_name(self):

        schema_dict = round_trip_load(StringIO("""\
            {
                'Cat': {},
                'Dog': {},
                'Horse': {}
            }
        """))

        spec_resolver = RefResolver('', {}, handlers=default_handlers)
        dereferencer = Dereferencer(spec_resolver)
        schema_registry = SchemaRegistry(dereferencer)
        generator = SchemasGenerator(dereferencer, schema_registry)

        schema_names_and_lines = [
            (schema.schema_name, schema.schema_deref.lc.line)
            for name, schema in generator.generate(schema_dict)
        ]

        assert schema_names_and_lines == [('Cat', 1), ('Dog', 2), ('Horse', 3)]
