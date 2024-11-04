
# Delegator

A tool designed to aid security researchers, penetration testers and red team operators to explore and abuse misconfigurations  related to domain-wide delegations in Google Cloud Platform (GCP) service accounts. By leveraging this tool, users can enumerate API permissions on G Suite APIs and identify various G Suite services for potential data extraction and permission abuses. This tool aims to increase awareness of the security implications surrounding the configuration of service accounts and the delegation of permissions.

# Features

* Enumerate API Permissions: Discover what GSUITE API permissions are available for the service account.
* Identify G Suite Services: List available G Suite services for potential exploitation or data extraction, scope enumeration is performed by bruteforcing and hit and trial.
* Domain-Wide Delegation: Analyze and abuse domain-wide delegations within GCP service accounts.
* Data Extraction Capabilities: Avail methods to extract data from identified G Suite services (ex: Google Sheets, Mail, Google Docs etc)



# Usage 

To get started with Delegator Tool, follow these steps to install the necessary libraries:

**Clone the Repository:**

```
git clone https://github.com/abhiabhi2306/delegator/delegator.git

cd delegator

```

**Install Required Libraries**

Ensure you have Python 3.x installed. You can use pip to install the required libraries:

```
pip install --upgrade google-api-python-client google-auth
``` 

**Example Usage**

```
python3 main.py 
```
