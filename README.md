# PDRename_EventBridgeAction

Python Script to rename an EventBridge Custom Incident Action

There is no way in the PagerDuty UI to rename a Custom Incident Action that is 
automatically added by the Amazon EventBridge integration.

## Usage:

```
usage: rename_ca.py [-h] api new_name

Rename Custom Incident Action for Amazon EventBridge

positional arguments:
  api         PagerDuty API Token
  new_name    The new name of the Custom Action for Amazon EventBridge

optional arguments:
  -h, --help  show this help message and exit
  
  ````
## Example:

```
  python3 rename_ca.py 01234567231313123 "Run a Lambda in AWS"
  
  ````
