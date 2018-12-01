from __future__ import absolute_import

from xbr._version import __version__
from xbr._abi import XBR_TOKEN_ABI, XBR_NETWORK_ABI, XBR_PAYMENT_CHANNEL_ABI
from xbr._abi import XBR_DEBUG_TOKEN_ADDR, XBR_DEBUG_NETWORK_ADDR
from xbr._buyer import SimpleBuyer
from xbr._seller import SimpleSeller


version = __version__
"""
XBR library version.
"""

xbrToken = None
"""
Contract instance of the token used in the XBR Network.
"""

xbrNetwork = None
"""
Contract instance of the XBR Network.
"""


def setProvider(_w3):
    """
    The XBR library must be initialized (once) first by setting the Web3 provider
    using this function.
    """
    global xbrToken
    global xbrNetwork
    xbrToken = _w3.eth.contract(address=XBR_DEBUG_TOKEN_ADDR, abi=XBR_TOKEN_ABI)
    xbrNetwork = _w3.eth.contract(address=XBR_DEBUG_NETWORK_ADDR, abi=XBR_NETWORK_ABI)


class MemberLevel(object):
    """
    XBR Network member levels.
    """
    NONE = 0
    ACTIVE = 1
    VERIFIED = 2
    RETIRED = 3
    PENALTY = 4
    BLOCKED = 5


class NodeType(object):
    """
    XBR Cloud node types.
    """
    NONE = 0
    MASTER = 1
    CORE = 2
    EDGE = 3


class ActorType(object):
    """
    XBR Market actor types.
    """
    NONE = 0
    NETWORK = 1
    MARKET = 2
    PROVIDER = 3
    CONSUMER = 4


__all__ = (
    'version',
    'setProvider',
    'xbrToken',
    'xbrNetwork',
    'MemberLevel',
    'ActorType',
    'NodeType',
    'XBR_TOKEN_ABI',
    'XBR_NETWORK_ABI',
    'XBR_PAYMENT_CHANNEL_ABI',
    'SimpleBuyer',
    'SimpleSeller',
)
