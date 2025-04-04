import boto3
from typing import List, Dict


def check_account_status(account_ids: List[str]) -> Dict[str, str]:
    """
    Check the status of AWS accounts using Organizations API

    Args:
        account_ids: List of AWS account IDs to check

    Returns:
        Dictionary mapping account IDs to their current status
    """
    try:
        # Initialize Organizations client
        org_client = boto3.client('organizations')

        account_status = {}

        # Paginate through all accounts in organization
        paginator = org_client.get_paginator('list_accounts')

        for page in paginator.paginate():
            for account in page['Accounts']:
                # Check if account ID is in our target list
                if account['Id'] in account_ids:
                    account_status[account['Id']] = {
                        'status': account['Status'],
                        'name': account['Name']
                    }

        # Check for accounts not found
        for acc_id in account_ids:
            if acc_id not in account_status:
                account_status[acc_id] = {
                    'status': 'NOT_FOUND',
                    'name': 'Unknown'
                }

        return account_status

    except Exception as e:
        print(f"Error checking account status: {str(e)}")
        return {}


def main():
    # Example usage
    account_ids = [
        "123456789012",
        "123345678901", # Replace with real account IDs
    ]

    results = check_account_status(account_ids)

    # Print results
    for account_id, details in results.items():
        print(f"Account ID: {account_id}")
        print(f"Status: {details['status']}")
        print(f"Name: {details['name']}")
        print("-" * 50)


if __name__ == "__main__":
    main()