"""
    Usage: python btc_address_validator.py <btc_address>

    Example: $ python btc_address_validator.py 1DJJoJ4sxwJdwExTsoDg8qXL1FEozDGQEFA                                            ─╯
    Output: Address with type Bitcoin Address is not a valid Bitcoin address.

    Example: $ python btc_address_validator.py 1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ                                             ─╯
    Output: Address with type Bitcoin Address is a valid Bitcoin address.
"""

from base58 import b58decode
from hashlib import sha256
import sys

# Taking the bitcoin address as command line input
btc_address_to_validate = sys.argv[1]

if __name__ == "__main__":

    btc_address_decoded = b58decode(btc_address_to_validate)

    version_plus_payload = btc_address_decoded[:-4]
    checksum_found = btc_address_decoded[-4:]

    # calculate real checksum
    checksum_real = sha256(sha256(version_plus_payload).digest()).digest()[:4]

    address_type = None
    version_prefix = version_plus_payload.hex()[0:8]
    if version_prefix[0:2] == "00":
        address_type = "Bitcoin Address"
    elif version_prefix[0:2] == "05":
        address_type = "Pay-to-Script-Hash Address"
    elif version_prefix[0:2] == "6F":
        address_type = "Bitcoin Testnet Address"
    elif version_prefix[0:2] == "80":
        address_type = "Private Key WIF"
    elif version_prefix[0:4] == "0142":
        address_type = "BIP-38 Encrypted Private Key"
    elif version_prefix[0:8] == "0488B21E":
        address_type = "BIP-32 Extended Public Key"

    if checksum_real == checksum_found:
        print(f"Address with type {address_type} is a valid Bitcoin address.")
    else:
        print(f"Address with type {address_type} is not a valid Bitcoin address.")