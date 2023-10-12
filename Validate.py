import re


def validate_aadhaar(string):
  return len(string) and string.isdigit()


def validate_pan(pan):
  pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
  return re.match(pattern, pan) is not None


def validate_DOB(date):
  pattern = r'^\d{2}-\d{2}-\d{4}$'
  return re.match(pattern, date) is not None


def validate_accnt_type(accnt_type):
  return accnt_type in ['savings', 'current']


def validate_accnt_num(string):
  return len(string) == 16 and string.isdigit()
