import json
import great_expectations as gx
import pandas as pd
from great_expectations.data_context import DataContext

context = gx.get_context()

# Get data
validator = context.sources.pandas_default.read_csv(r"C:\GIT\sandbox\etl_repo\gx_data_universe_definer\data\ref_file_2024_05_06.csv")

validator.expect_column_values_to_not_be_null("exchange_code")

checkpoint = gx.checkpoint.SimpleCheckpoint(
    name="version-0.18.21 universe_definer_checkpoint",
    data_context=context,
    validator=validator,
)

checkpoint_result = checkpoint.run()

validation_result_identifier = checkpoint_result.list_validation_result_identifiers()[0]
context.open_data_docs(resource_identifier=validation_result_identifier)