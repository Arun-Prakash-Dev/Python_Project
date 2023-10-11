import re


def validate_aadhaar(string):
  return string.isdigit()


def validate_pan(pan):
  pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
  return re.match(pattern, pan) is not None
