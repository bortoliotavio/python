texto = '       StriNg SeM padRao            '

print('Capitalize => <{}>'.format(texto.capitalize()))
print('Title => <{}>'.format(texto.title()))
print('Lower => <{}>'.format(texto.lower()))
print('Upper => <{}>'.format(texto.upper()))
print('SwapCase => <{}>'.format(texto.swapcase()))
print('Center => <{}>'.format(texto.center(50)))
print('zFill => <{}>'.format(texto.zfill(50)))
print('LJust => <{}>'.format(texto.ljust(50)))
print('RJust => <{}>'.format(texto.rjust(50, '~')))
print('LJust => <{}>'.format(texto.ljust(50, '~')))
print('cocncatenação => <{}>'.format('Concatenei' + 'duas strings'))
print('Multiplicação (Repetição) => <{}>'.format('~' * 50))
print('a in Rafael => <{}>'.format('a' in 'Rafael'))
print('af in Rafael => <{}>'.format('af' in 'Rafael'))
print('ae in Rafael => <{}>'.format('ae' in 'Rafael'))
print('ae not in Rafael => <{}>'.format('ae' not in 'Rafael'))

print('Count => <{}>'.format(texto.count('a')))
print('Count => <{}>'.format(texto.count('a', 0, 4)))
print('Find => <{}>'.format(texto.find('a')))
print('Find => <{}>'.format(texto.find('x')))
print('Index => <{}>'.format(texto.index('a')))
# print('Index => <{}>'.format(texto.index('x')))
print('StartsWith => <{}>'.format(texto.startswith('String')))
print('EndsWith => <{}>'.format(texto.endswith('string')))
print('Replace => <{}>'.format(texto.replace('a', 'python')))
print('Replace => <{}>'.format(texto.replace('a', 'python', 1)))
print('LStrip => <{}>'.format(texto.lstrip()))
print('RStrip => <{}>'.format(texto.rstrip()))
print('Strip => <{}>'.format(texto.strip()))
print('Split => <{}>'.format('14/04/2018'.split('/')))
print('Split => <{}>'.format('14/04/2018'.split('/')[0]))
print('Split => <{}>'.format('14/04/2018'.split('/')[-1]))
print('Split => <{}>'.format('14/04/2018'.split('/')[-2]))
print('Split => <{}>'.format('14/04/2018'.split('0')))
print('Join => <{}>'.format('/'.join(['14', '04', '2018'])))
print('Join => <{}>'.format(', '.join(['João', 'Pedro', 'José'])))


print('Fim')

