"""Excepions for MyUplink library."""

class MyUplinkException(Exception):
  """Generic MyUplnk exception."""

class MyUplinkAuthException(MyUplinkException):
  """MyUplink Authentication exception."""

class MyUplinkConflictException(MyUplinkException):
  """MyUplink Conflict exception."""

class MyUplinkRateLimitingException(MyUplinkException):
  """MyUplink Authentication exception."""
