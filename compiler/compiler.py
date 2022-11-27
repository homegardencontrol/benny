import sys,os
print(os.getcwd())
file_name = sys.argv[1]
f = open(file_name, 'r')
lines = f.readlines()
out_text = ''
__benny__class__ = []
__indent__ = 0
__first__line__ = True
for line in lines:
    #print('>>>',end=' ')
    if __first__line__ and not line.isspace():
        __first__line__ = False
        for i,c in enumerate(line):
            if c.isspace():
                __indent__ = i+1
            else:
                break
    __line__indent__ = __indent__
    if not __first__line__:
        for i,c in enumerate(line):
            if c.isspace():
                __line__indent__ = i
            else:
                break
    __benny__syntax__ = line[__indent__:].strip()+'\n'
    if __benny__syntax__.find('if ')>=0 or __benny__syntax__.find('for ')>=0 or __benny__syntax__.find('while ')>=0 or __benny__syntax__.find('match ')>=0 or __benny__syntax__.find('case ')>=0:
        out_text = out_text +line[__indent__:__line__indent__]+ __benny__syntax__
        continue
    if __benny__syntax__.find('.')<0 and len(__benny__syntax__.split('['))==2 and __benny__syntax__.find('=')>__benny__syntax__.find('[') and __benny__syntax__.find('=')<__benny__syntax__.find(']'):
        __benny__object__ = __benny__syntax__
        __benny__list__ = __benny__object__[__benny__object__.find('[')+1:__benny__object__.find(']')].split(',')
        __benny__object__=__benny__object__[0:__benny__object__.find('[')]
        if not __benny__object__ in __benny__class__:
            #exec('class '+__benny__object__+':\n __benny__list__=[]\n pass')
            out_text = out_text +line[__indent__:__line__indent__]+ 'class '+__benny__object__+':\n __benny__list__=[]\n pass\n'
            __benny__class__.append(__benny__object__)
        for __benny__inlist__ in __benny__list__:
            #exec(__benny__object__+'.__benny__list__.append("'+__benny__inlist__[0:__benny__inlist__.find('=')].strip()+'")')
            out_text = out_text +line[__indent__:__line__indent__]+ 'if not "'+__benny__inlist__[0:__benny__inlist__.find('=')].strip()+'" in '+__benny__object__+'.__benny__list__ :\n'
            out_text = out_text +line[__indent__:__line__indent__]+ ' '+ __benny__object__+'.__benny__list__.append("'+__benny__inlist__[0:__benny__inlist__.find('=')].strip()+'")\n'
            #exec(__benny__object__+'.'+__benny__inlist__)
            out_text = out_text +line[__indent__:__line__indent__]+ __benny__object__+'.'+__benny__inlist__+'\n'
            continue
    if __benny__syntax__.find('.')<__benny__syntax__.find('=') and __benny__syntax__.find('.')>=0:
        if len(__benny__syntax__.split('['))>2 or len(__benny__syntax__.split(']'))>2 or __benny__syntax__.find('{')>=0:
            print('Benny error more than [1 block] in sentense and dict not allow')
            exit()
        if __benny__syntax__[0:__benny__syntax__.find('=')].find('(')>=0:
            #exec(__benny__syntax__)
            out_text = out_text +line[__indent__:__line__indent__]+ __benny__syntax__
            continue
        __benny__object__list__ = __benny__syntax__.split('.')
        __root__object__ = ''
        __root__dot__object__ = ''
        for __benny__object__ in __benny__object__list__:
            __benny__list__type__ = False
            if __benny__object__.find('[')>0 and __benny__object__[__benny__object__.find('[')+1:__benny__object__.find(']')].find('=')>=0:
                __benny__list__ = __benny__object__[__benny__object__.find('[')+1:__benny__object__.find(']')].split(',')
                __benny__object__=__benny__object__[0:__benny__object__.find('[')]
                __benny__list__type__ = True
            __benny__type__value__ = False
            if __benny__object__.find('=')>0:
                __benny__value__ = __benny__object__[__benny__object__.find('=')+1:]
                __benny__object__=__benny__object__[0:__benny__object__.find('=')]
                __benny__type__value__ = True
            if __root__object__ == '':
                if not __benny__object__ in __benny__class__:
                    #exec('class '+__benny__object__+':\n __benny__list__=[]\n pass')
                    __benny__class__.append(__benny__object__)
                    out_text = out_text +line[__indent__:__line__indent__]+'class '+__benny__object__+':\n __benny__list__=[]\n pass\n'
            else:
                if not(__benny__type__value__):
                    if not __root__object__+'_'+__benny__object__ in __benny__class__:
                        #exec('class '+__root__object__+'_'+__benny__object__+':\n __benny__list__=[]\n pass')
                        __benny__class__.append(__root__object__+'_'+__benny__object__)
                        out_text = out_text+line[__indent__:__line__indent__]+'class '+__root__object__+'_'+__benny__object__+':\n __benny__list__=[]\n pass\n'
                        #exec(__root__dot__object__+'.'+__benny__object__+'='+__root__object__+'_'+__benny__object__)
                        out_text = out_text +line[__indent__:__line__indent__]+ __root__dot__object__+'.'+__benny__object__+'='+__root__object__+'_'+__benny__object__+'\n'
            if __benny__list__type__:
                for __benny__inlist__ in __benny__list__:
                    #exec(__root__object__+'.'+__benny__object__+'.__benny__list__.append("'+__benny__inlist__[0:__benny__inlist__.find('=')].strip()+'")')
                    out_text = out_text +line[__indent__:__line__indent__]+'if not "'+__benny__inlist__[0:__benny__inlist__.find('=')].strip()+'" in '+__root__object__+'.'+__benny__object__+'.__benny__list__ :\n'
                    out_text = out_text +line[__indent__:__line__indent__]+ ' '+__root__object__+'.'+__benny__object__+'.__benny__list__.append("'+__benny__inlist__[0:__benny__inlist__.find('=')].strip()+'")\n'
                        #exec(__root__object__+'.'+__benny__object__+'.'+__benny__inlist__)
                    out_text = out_text +line[__indent__:__line__indent__]+ __root__object__+'.'+__benny__object__+'.'+__benny__inlist__+'\n'
            else:
                if __benny__type__value__:
                    #exec(__root__object__+'.__benny__list__.append("'+__benny__object__.strip()+'")')
                    out_text = out_text +line[__indent__:__line__indent__]+ 'if not "'+__benny__object__.strip()+'" in '+__root__object__+'.__benny__list__ :\n'
                    out_text = out_text +line[__indent__:__line__indent__]+ ' '+__root__object__+'.__benny__list__.append("'+__benny__object__.strip()+'")\n'
                    #exec(__root__object__+'.'+__benny__object__+'='+__benny__value__)
                    out_text = out_text +line[__indent__:__line__indent__]+ __root__object__+'.'+__benny__object__+'='+__benny__value__+'\n'
            if __root__object__=='':
                __root__object__ = __benny__object__
                __root__dot__object__ = __benny__object__
            else:
                __root__object__ = __root__object__+'_'+__benny__object__
                __root__dot__object__ = __root__dot__object__+'.'+__benny__object__
    else:
        #exec(__benny__syntax__)
        out_text = out_text +line[__indent__:__line__indent__]+ __benny__syntax__ +'\n'

file_name = file_name[:file_name.find('.')]
file_name = file_name+'.py'
f = open(file_name, 'w')
f.write(out_text)
f.close()
