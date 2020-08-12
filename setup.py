from cx_Freeze import setup, Executable

setup(name = 'SecretMessage',
      version = '0.1',
      description = '',
      executables = [Executable('encryptionScript.py')])
