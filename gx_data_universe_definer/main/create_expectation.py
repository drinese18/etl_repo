import great_expectations as gx
from great_expectations.checkpoint import SimpleCheckpoint
from great_expectations.core.batch import BatchRequest
from great_expectations.core.yaml_handler import YAMLHandler

context: gx.DataContext = gx.get_context()

yaml=gx.core.yaml_handler.YAMLHandler()

datasource_config = {
    "name": "reference_data",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors":{
        "new_connector":{ 
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory":'C:\GIT\sandbox\etl_repo\gx_data_universe_definer\data',
            "default_regex": {
                "group_names": ['data_asset_name'],
                "pattern": "(.*)",
                    
                },
            }
        }
    }

datasource = context.test_yaml_config(yaml.dump(datasource_config))

datasource = context.add_datasource(**datasource_config)

batch_request = gx.core.batch.BatchRequest(
    datasource_name ="reference_data",
    data_connector_name ="reference_data_connector",
    data_asset_name ="exchange_code",
)

exact=context.assistants.onboarding.run(batch_request=batch_request,estimation="exact")
outliers=context.assistants.onboarding.run(batch_request=batch_request,estimation="flag_outliers")

exact.plot_metrics()
outliers.plot_expectations_and_metrics()

suite = exact.get_expectation_suite("test")
context.save_expectation_suite(suite)