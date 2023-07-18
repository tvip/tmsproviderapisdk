from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('tmsproviderapisdk').version
except DistributionNotFound:
    __version__ = 'unknown'

from tmsproviderapisdk.tms_config import TmsConfig, TmsConfigHolder
from tmsproviderapisdk.tms_account import TmsAccount
from tmsproviderapisdk.tms_account_subscription import TmsAccountSubscription
from tmsproviderapisdk.tms_channel import TmsChannel
from tmsproviderapisdk.tms_device import TmsDevice
from tmsproviderapisdk.tms_device_subscription import TmsDeviceSubscription
from tmsproviderapisdk.tms_tarif import TmsTarif
from tmsproviderapisdk.tms_tarif_tag import TmsTarifTag
from tmsproviderapisdk.tms_region import TmsRegion
from tmsproviderapisdk.tms_account_network import TmsAccountNetwork
from tmsproviderapisdk.tms_devices_types import TmsDeviceTypes
