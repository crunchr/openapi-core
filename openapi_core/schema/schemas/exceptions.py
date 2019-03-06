from openapi_core.schema.exceptions import OpenAPIMappingError

import attr


@attr.s
class OpenAPISchemaError(OpenAPIMappingError):
    schema = attr.ib()

    def __str__(self):
        if self.schema.schema_deref is not None and hasattr(self.schema, 'lc'):
            return '[line: {0} col: {1}]'.format(
                self.schema.schema_deref.lc.line,
                self.schema.schema_deref.lc.col,
            )
        return ''


@attr.s
class InvalidSchema(OpenAPISchemaError):
    msg = attr.ib()

    def __str__(self):
        return self.msg + super(self).__str__()


@attr.s
class InvalidFormat(OpenAPISchemaError):
    msg = attr.ib()

    def __str__(self):
        return self.msg + super(self).__str__()


@attr.s
class NoValidSchema(OpenAPISchemaError):
    value = attr.ib()

    def __str__(self):
        return "No valid schema found for value: {0}{1}".format(self.value, super(self).__str__())


@attr.s
class UndefinedItemsSchema(OpenAPISchemaError):
    type = attr.ib()

    def __str__(self):
        return "Null value for schema type {0}{1}".format(self.type, super(self).__str__())


@attr.s
class InvalidSchemaValue(OpenAPISchemaError):
    msg = attr.ib()
    value = attr.ib()
    type = attr.ib()

    def __str__(self):
        return self.msg.format(value=self.value, type=self.type) + super(self).__str__()


@attr.s
class InvalidCustomFormatSchemaValue(InvalidSchemaValue):
    original_exception = attr.ib()

    def __str__(self):
        msg = self.msg.format(value=self.value, type=self.type, exception=self.original_exception)
        return msg + super(self).__str__()


@attr.s
class UndefinedSchemaProperty(OpenAPISchemaError):
    extra_props = attr.ib()

    def __str__(self):
        return "Extra unexpected properties found in schema: {0}{1}".format(
            self.extra_props,
            super(self).__str__(),
        )


@attr.s
class InvalidSchemaProperty(OpenAPISchemaError):
    property_name = attr.ib()
    original_exception = attr.ib()

    def __str__(self):
        return "Invalid schema property {0}: {1}{2}".format(
            self.property_name,
            self.original_exception,
            super(self).__str__(),
        )


@attr.s
class MissingSchemaProperty(OpenAPISchemaError):
    property_name = attr.ib()

    def __str__(self):
        return "Missing schema property: {0}{1}".format(
            self.property_name,
            super(self).__str__(),
        )


@attr.s
class NoOneOfSchema(OpenAPISchemaError):
    type = attr.ib()

    def __str__(self):
        return "Exactly one valid schema type {0} should be valid, None found{1}".format(
            self.type,
            super(self).__str__(),
        )


@attr.s
class MultipleOneOfSchema(OpenAPISchemaError):
    type = attr.ib()

    def __str__(self):
        return "Exactly one schema type {0} should be valid, more than one found{1}".format(
            self.type,
            super(self).__str__(),
        )
