print('Benny 0.91')
print('==========')
print('base on Python 3')
print('Type "help", "copyright", "credits" or "license" for more information.')
while True:
	print('>>>',end=' ')
	__benny__syntax__ = input()
	if __benny__syntax__=='help':
		print('Type help() for interactive help, or help(object) for help about object.')
	if __benny__syntax__=='copyright':
		print('Copyright (c) 2022 Benny Research.')
		print('==================================')
		print()
		print('Copyright (c) 2001-2022 Python Software Foundation.')
		print('All Rights Reserved.')
		print()
		print('Copyright (c) 2000 BeOpen.com.')
		print('All Rights Reserved.')
		print()
		print('Copyright (c) 1995-2001 Corporation for National Research Initiatives.')
		print('All Rights Reserved.')
		print()
		print('Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.')
		print('All Rights Reserved.')
	if __benny__syntax__=='credits':
		print('Benny in memory of Supot Sawangpiriyakij')
		print('Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands')
		print('for supporting Python development.  See www.python.org for more information.')
	if __benny__syntax__=='license':
		print('Benny MIT license')
		print('=================')
		print('Type license() to see the full Python license text')
	if __benny__syntax__.find('.')<__benny__syntax__.find('=') and __benny__syntax__.find('.')>=0::
		if len(__benny__syntax__.split('['))>2 or len(__benny__syntax__.split(']'))>2:
			print('Benny error more than [1 block] in sentense')
			try:
				exec(__benny__syntax__)
			except Exception as e: print(e)
			continue
		if __benny__syntax__[0:__benny__syntax__.find('=')].find('(')>=0:
			try:
				exec(__benny__syntax__)
			except Exception as e: print(e)
			continue
		__benny__object__list__ = __benny__syntax__.split('.')
		__root__object__ = ''
		__root__dot__object__ = ''
		for __benny__object__ in __benny__object__list__:
			__benny__list__type__ = False
			if __benny__object__.find('[')>0:
				__benny__list__ = __benny__object__[__benny__object__.find('[')+1:__benny__object__.find(']')].split(',')
				__benny__object__=__benny__object__[0:__benny__object__.find('[')]
				__benny__list__type__ = True
			__benny__type__value__ = False
			if __benny__object__.find('=')>0:
				__benny__value__ = __benny__object__[__benny__object__.find('=')+1:]
				__benny__object__=__benny__object__[0:__benny__object__.find('=')]
				__benny__type__value__ = True
			if __root__object__ == '':
				if not __benny__object__ in locals():
					exec('class '+__benny__object__+':\n pass')
			else:
				if not(__benny__type__value__):
					if not __root__object__+'_'+__benny__object__ in locals():
						exec('class '+__root__object__+'_'+__benny__object__+':\n pass')
						exec(__root__dot__object__+'.'+__benny__object__+'='+__root__object__+'_'+__benny__object__)
			if __benny__list__type__:
				for __benny__inlist__ in __benny__list__:
					exec(__root__object__+'.'+__benny__object__+'.'+__benny__inlist__)
			else:
				if __benny__type__value__:
					exec(__root__object__+'.'+__benny__object__+'='+__benny__value__)
			if __root__object__=='':
				__root__object__ = __benny__object__
				__root__dot__object__ = __benny__object__
			else:
				__root__object__ = __root__object__+'_'+__benny__object__
				__root__dot__object__ = __root__dot__object__+'.'+__benny__object__
	else:
		try:
			exec(__benny__syntax__)
		except Exception as e: print(e)
