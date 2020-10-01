from tmsproviderapisdk import TmsConfig, TmsConfigHolder
from tmsproviderapisdk import TmsAccount
from tmsproviderapisdk.tms_exceptions import ApiHTTPError

# Configure
config = TmsConfig('http://ms-test.o.tvip.ru', 'den-test-api', 'dentest-api', None)

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
