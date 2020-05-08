"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class connect_request(object):
    __slots__ = ["is_special"]

    __typenames__ = ["boolean"]

    __dimensions__ = [None]

    def __init__(self):
        self.is_special = False

    def encode(self):
        buf = BytesIO()
        buf.write(connect_request._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">b", self.is_special))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != connect_request._get_packed_fingerprint():
            raise ValueError("Decode error")
        return connect_request._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = connect_request()
        self.is_special = bool(struct.unpack('b', buf.read(1))[0])
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if connect_request in parents: return 0
        tmphash = (0x91bbb4ec9e35ec8c) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if connect_request._packed_fingerprint is None:
            connect_request._packed_fingerprint = struct.pack(">Q", connect_request._get_hash_recursive([]))
        return connect_request._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
