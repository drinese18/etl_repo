import json
import great_expectations as ge
import pandas as pd
from great_expectations.data_context import DataContext

# Load the Data Context
context = ge.get_context()

# Get data
df = pd.read_csv(r"C:\GIT\sandbox\data\ref_file_2024_05_06.csv")

context.sources.delete_pandas(name="ref_data")
datasource = context.sources.add_pandas(name="ref_data")
data_asset = datasource.add_dataframe_asset(name="my_dataframe_asset")
batch_request = data_asset.build_batch_request(dataframe=df)

# Specify the path to your Expectation Suite JSON file
suite_path = r"C:\GIT\sandbox\gx\expectations\ref_file_2024_05_06.json"

expectation_suite_name = "ref_file_2024_05_06"

# Load the Expectation Suite
with open(suite_path, "r") as f:
    suite_dict = json.load(f)
    suite = context.get_expectation_suite(expectation_suite_name=suite_dict["expectation_suite_name"])

context.save_expectation_suite(suite)

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name,
)

validation_results = validator.validate()

failed_expectations = []
for validation_result in validation_results.results:
    if not validation_result.success:
        failed_expectations.append(validation_result)

for expectation in failed_expectations:
    if expectation.expectation_config.expectation_type == "expect_column_values_to_be_in_set":
        column_name = expectation.expectation_config.kwargs["column"]
        unexpected_indices = expectation.result["partial_unexpected_list"]
        filtered_df = df[df['exchange_code'] != unexpected_indices[0]]
        #print(filtered_df)

# Print the Expectation Suite
print(suite)
print(validation_results)
print(unexpected_indices[0])
print(filtered_df)