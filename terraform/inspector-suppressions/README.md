# Inspector Suppressions Module

## Global Inspector Suppressions
```hcl
#Example for suppression rule filtered on resource tags, key: example:key, value: example-value
# Approved: Person A
resource "awscc_inspectorv2_filter" "resource_tag_suppression" {
  name          = "${local.name_prefix}-resource-tag"
  description   = "CRSS-XXXX: Suppression rule filtered on resource tags"
  filter_action = "SUPPRESS"
  filter_criteria = {
    resource_tags = [{
      comparison = "EQUALS"
      key        = "example:key"
      value      = "example-value"
      }
    ]
  }
}

#Example for suppression rule filtered on vulnerable package, package name: example-package
# Approved: Person A
resource "awscc_inspectorv2_filter" "package_wide_suppressions" {
  name          = "${local.name_prefix}-package-wide"
  description   = "CRSS-XXXX: Suppression rule for specific packages"
  filter_action = "SUPPRESS"
  filter_criteria = {
    vulnerable_packages = [
      {
        name = {
          comparison = "EQUALS"
          value      = "example-package"
        }
      }
    ]
  }
}
```

## CVE Specific Suppressions
```hcl
# Example for single CVE suppression rule, CVE ID: CVE-2021-1234
# Approved: Person A
resource "awscc_inspectorv2_filter" "single_cve_suppression" {
  name          = "${local.name_prefix}-single-cve"
  description   = "CRSS-XXXX: Suppression rule for a single CVE"
  filter_action = "SUPPRESS"
  filter_criteria = {
    vulnerability_id = [{
      comparison = "EQUALS"
      value      = "CVE-2021-1234"
    }]
  }
}

# Example for multiple CVE suppression rule, CVE IDs: CVE-2021-1234, CVE-2021-5678
# Approved: Person A
resource "awscc_inspectorv2_filter" "multiple_cve_suppressions" {
  name          = "${local.name_prefix}-multiple-cve"
  description   = "CRSS-XXXX: Suppression rule for multiple CVEs"
  filter_action = "SUPPRESS"
  filter_criteria = {
    vulnerability_id = [
      {
        comparison = "EQUALS"
        value      = "CVE-2021-1234"
      },
      {
        comparison = "EQUALS"
        value      = "CVE-2021-5678"
      }
    ]
  }
}
```

## Account Wide Suppressions

```hcl
# Example suppression resource
# Account wide inspector suppression rule
# This resource will suppress all findings for the account with the AWS account ID 123456789012
# Approved: Person A
resource "awscc_inspectorv2_filter" "account_wide_suppressions" {
  name          = "${local.name_prefix}-account-wide"
  description   = "CRSS-XXYY. Suppression rule for account wide suppressions"
  filter_action = "SUPPRESS"
  filter_criteria = {
    aws_account_id = [{
      comparison = "EQUALS"
      value      = "123456789012"
    }]
  }
}
```
