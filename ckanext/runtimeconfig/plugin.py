import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class RuntimeconfigPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'runtimeconfig')

    def update_config_schema(self, schema):

        ignore_missing = toolkit.get_validator('ignore_missing')
        is_positive_integer = toolkit.get_validator('is_positive_integer')

        schema.update({
            # This is an existing CKAN core configuration option, we are just
            # making it available to be editable at runtime
            'ckan.datasets_per_page': [ignore_missing, is_positive_integer],
             
            #schemas
            'scheming.dataset_schemas' : [ingore_missing, unicode],

            # This is a custom configuration option
            'ckanext.example_iconfigurer.test_conf': [ignore_missing, unicode],
        })

        return schema
