import os
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
	base = 'Win32GUI'

mfcdir = 'c:\\Python27\\Lib\\site-packages\\pythonwin\\'

mfcfiles = [os.path.join(mfcdir,i) for i in ['mfc90.dll','mfc90u.dll','mfcm90.dll','mfcm90u.dll','Microsoft.VC90.MFC.manifest']]

data_files = [('Microsoft.VC90.MFC',mfcfiles),'DataMarket.py']

exe = Executable(
	script='Bats.py',
	base=None,
	compress=True,
	icon='bats.ico'
)

setup(
	name='Bats - Ticker Information',
	version='1.0',
	description='This aplication get ticker information from Bats Exchanges (EUA and Europe), updating information every 5 seconds.',
	author='Rui Alves Costa',
	author_email='rui.alves.costa@finantech.pt',
	data_files = data_files,
	executables=[exe] #,icon='bats.ico')]
	)