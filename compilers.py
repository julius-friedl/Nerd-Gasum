def compiler(str2betranslated, language):
    if (language == "Morse-Code"):
        strword_space = '/ '
        Aa = '.- '
        Bb = '-... '
        Cc = '-.-. '
        Dd = '-.. '
        Ee = '. '
        Ff = '..-. '
        Gg = '--. '
        Hh = '.... '
        Ii = '.. '
        Jj = '.--- '
        Kk = '-.- '
        Ll = '.-.. '
        Mm = '-- '
        Nn = '-. '
        Oo = '--- '
        Pp = '.--. '
        Qq = '--.- '
        Rr = '.-. '
        Ss = '... '
        Tt = '- '
        Uu = '..- '
        Vv = '...- '
        Ww = '.-- '
        Xx = '-..- '
        Yy = '-.-- '
        Zz = '--.. '
        str2betranslated 
        global str2morse_output
        str2betranslated = [s.replace(' ', strword_space)for s in str2betranslated]
    
        str2betranslated = [s.replace('A', Aa)for s in str2betranslated]
        str2betranslated = [s.replace('a', Aa)for s in str2betranslated]
    
        str2betranslated = [s.replace('B', Bb)for s in str2betranslated]
        str2betranslated = [s.replace('b', Bb)for s in str2betranslated]
    
        str2betranslated = [s.replace('C', Cc)for s in str2betranslated]
        str2betranslated = [s.replace('c', Cc)for s in str2betranslated]
    
        str2betranslated = [s.replace('D', Dd)for s in str2betranslated]
        str2betranslated = [s.replace('d', Dd)for s in str2betranslated]
    
        str2betranslated = [s.replace('E', Ee)for s in str2betranslated]
        str2betranslated = [s.replace('e', Ee)for s in str2betranslated]
    
        str2betranslated = [s.replace('F', Ff)for s in str2betranslated]
        str2betranslated = [s.replace('f', Gg)for s in str2betranslated]
    
        str2betranslated = [s.replace('G', Gg)for s in str2betranslated]
        str2betranslated = [s.replace('g', Gg)for s in str2betranslated]
        
        str2betranslated = [s.replace('H', Hh)for s in str2betranslated]
        str2betranslated = [s.replace('h', Hh)for s in str2betranslated]
        
        str2betranslated = [s.replace('I', Ii)for s in str2betranslated]
        str2betranslated = [s.replace('i', Ii)for s in str2betranslated]
        
        str2betranslated = [s.replace('J', Jj)for s in str2betranslated]
        str2betranslated = [s.replace('j', Jj)for s in str2betranslated]
        
        str2betranslated = [s.replace('K', Kk)for s in str2betranslated]
        str2betranslated = [s.replace('k', Kk)for s in str2betranslated]
        
        str2betranslated = [s.replace('L', Ll)for s in str2betranslated]
        str2betranslated = [s.replace('l', Ll)for s in str2betranslated]
        
        str2betranslated = [s.replace('M', Mm)for s in str2betranslated]
        str2betranslated = [s.replace('m', Mm)for s in str2betranslated]
        
        str2betranslated = [s.replace('N', Nn)for s in str2betranslated]
        str2betranslated = [s.replace('n', Nn)for s in str2betranslated]
        
        str2betranslated = [s.replace('O', Oo)for s in str2betranslated]
        str2betranslated = [s.replace('o', Oo)for s in str2betranslated]
        
        str2betranslated = [s.replace('P', Pp)for s in str2betranslated]
        str2betranslated = [s.replace('p', Pp)for s in str2betranslated]
        
        str2betranslated = [s.replace('Q', Qq)for s in str2betranslated]
        str2betranslated = [s.replace('q', Qq)for s in str2betranslated]
        
        str2betranslated = [s.replace('R', Rr)for s in str2betranslated]
        str2betranslated = [s.replace('r', Rr)for s in str2betranslated]
        
        str2betranslated = [s.replace('S', Ss)for s in str2betranslated]
        str2betranslated = [s.replace('s', Ss)for s in str2betranslated]
        
        str2betranslated = [s.replace('T', Tt)for s in str2betranslated]
        str2betranslated = [s.replace('t', Tt)for s in str2betranslated]
        
        str2betranslated = [s.replace('U', Uu)for s in str2betranslated]
        str2betranslated = [s.replace('u', Uu)for s in str2betranslated]
        
        str2betranslated = [s.replace('V', Vv)for s in str2betranslated]
        str2betranslated = [s.replace('v', Vv)for s in str2betranslated]
        
        str2betranslated = [s.replace('W', Ww)for s in str2betranslated]
        str2betranslated = [s.replace('w', Ww)for s in str2betranslated]
        
        str2betranslated = [s.replace('X', Xx)for s in str2betranslated]
        str2betranslated = [s.replace('x', Xx)for s in str2betranslated]
        
        str2betranslated = [s.replace('Y', Yy)for s in str2betranslated]
        str2betranslated = [s.replace('y', Yy)for s in str2betranslated]
        
        str2betranslated = [s.replace('Z', Zz)for s in str2betranslated]
        str2betranslated = [s.replace('z', Zz)for s in str2betranslated]
        
        str2morse_output = ''.join(str2betranslated)
        output_text.SetValue("str2morse_output")
        return