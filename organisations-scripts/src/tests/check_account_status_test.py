import pytest
import os
import boto3
from moto import mock_aws
from unittest.mock import patch
from check_account_status import check_account_status


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"


@pytest.fixture(scope="function")
def orgs(aws_credentials):
    """Mocked Organizations client."""
    with mock_aws():
        client = boto3.client("organizations", region_name="eu-west-1")

        # Create a mock organization
        client.create_organization(FeatureSet="ALL")

        # Create a mock account
        account_id = "123456789012"
        response = client.create_account(AccountName="TestAccount", Email="test@example.com")

        # Mock the describe_account response to return our specific account ID
        with patch('botocore.client.BaseClient._make_api_call') as mock_call:
            def side_effect(operation_name, kwargs):
                if operation_name == 'ListAccounts':
                    return {
                        'Accounts': [{
                            'Id': account_id,
                            'Name': 'TestAccount',
                            'Email': 'test@example.com',
                            'Status': 'SUSPENDED',
                        }]
                    }
                return response

            mock_call.side_effect = side_effect
            yield client

def test_check_account_status(orgs):
    # Call the function and assert the result
    account_id = "123456789012"
    result = check_account_status(account_id)
    assert result[account_id]['status'] == "SUSPENDED"
    assert result[account_id]['name'] == "TestAccount"