from datetime import datetime
import pytz
from tmsproviderapisdk import TmsConfig, TmsConfigHolder
from tmsproviderapisdk import TmsAccount
from tmsproviderapisdk.tms_exceptions import ApiHTTPError
from tmsproviderapisdk import TmsAccountSubscription

# Configure
config = TmsConfig('https://tms.example.com', 'provider_admin', 'provider_password')

# apply config
TmsConfigHolder.apply(config)

# Create password hash
pin_md5 = TmsAccount.get_md5_pin("test_password")

# Create new disabled account object
new_account = TmsAccount(login="test_account", fullname="Marshall Mathers", pin_md5=pin_md5, enabled=False)

# Call create method
try:
    account = new_account.create()
except ApiHTTPError as e:
    # Print error message to stout
    print(e)
else:
    # Print account to stout
    print(account)

    # Set account object enabled status
    account.enabled = True

    # Update account on TMS side
    account.update()

# Get all accounts
accounts, total_accounts_count = TmsAccount.get_list()

# Print all accounts to stdin
for account in accounts:
    print(account)

# Get one account by id
try:
    account = TmsAccount.get(1)
except ApiHTTPError as e:
    # Print error message to stout
    print(e)
else:
    # Delete account
    account.delete()

# Create subscription for account with tarif for example with id 1

# Get account
account = TmsAccount.get(1)
# Get now datetime
now = datetime.now(pytz.timezone('Europe/Moscow'))
# Datetime to string with format
now_with_format = now.strftime("%Y-%m-%dT%H:%M:%S%z")

# Create subscription object
subscription = TmsAccountSubscription(account=account.id, start=now_with_format, tarif=1)

# Create subscription on tms side
try:
    subscription = subscription.create()
except ApiHTTPError as e:
    print(e)
else:
    # print subscription to stout
    print(subscription)

# Example functions

# Get all accounts with paging
def get_accounts_with_paging():

    accounts, total = TmsAccount.get_list()

    if total > len(accounts):
        while True:
            if total == len(accounts):
                break
            page_accounts, _ = TmsAccount.get_list(start=len(accounts), limit=50, sort="id")

            accounts.extend(page_accounts)

    return accounts
