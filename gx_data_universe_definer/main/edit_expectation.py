import great_expectations as gx
from great_expectations.core.expectation_suite import ExpectationSuite

context = gx.get_context()

config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_between",
    kwargs={
        "auto": True,
        "column": "passenger_count",
        "domain": "column",
        "max_value": 6,
        "min_value": 1,
        "mostly": 1.0,
        "strict_max": False,
        "strict_min": False,
    },
)