import sys

hindi_kw={
        'False':'झूठ',
        'None':'खाली',
        'True':'सच',
        'and':'और',
        'as':'जैसा',
        'assert':'दावा',
        'async':'अतुल ',
        'await':'प्रत्याश ',
        'break':'बाहर',
        'class':'वर्ग',
        'continue':'जारी',
        'def':'परिभाषा',
        'del':'मिटाओ',
        'elif':'वरनायदि ',
        'else':'वरना',
        'except':'सिवाय',
        'finally':'अंततह',
        'for':'सभी',
        'from':'द्वारा',
        'global':'वैश्विक',
        'if':'यदि',
        'import':'आयात',
        'in':'अंदर',
        'is':'है',
        'lambda':'फलन',
        'nonlocal':'व्यापी',
        'not':'न',
        'or':'अथवा',
        'pass':'सफल',
        'raise':'त्रुटि',
        'return':'वापस',
        'try':'प्रयास',
        'while':'जबतक',
        'with':'साथ',
        'yield':'उपज',
    }

hindi_func={
        'print':'लिखो',
        'str':'उक्ति',
        'sum':'जोड़',
        'list':'सूची',
        'type':'जाती',
        'range':'लड़ी'
    }

hindi_numerals={
        '0':'०',
        '1':'१',
        '2':'२',
        '3':'३',
        '4':'४',
        '5':'५',
        '6':'६',
        '7':'७',
        '8':'८',
        '9':'९',
}
hindi_dict={**hindi_kw,**hindi_func,**hindi_numerals}
inv_hindi_dict=inv_dict = dict(map(reversed, hindi_dict.items()))
##print(hindi_dict,inv_hindi_dict)

try:
    filename = sys.argv[1]
except:
    filename=input("Enter file name : ")

if not filename.endswith(".py"):
    filename+=".py"
    
fin = open(filename, 'r', encoding="utf8")
exec_script=[]
for read_line in fin:
    line_list = read_line.split('"')
    for n,line in enumerate(line_list):
        if n%2==1:
            continue
        for key,value in inv_hindi_dict.items():
            line = str(line).replace(key,value)
        line_list[n] = line
    exec_line='\"'.join(line_list)
    exec_script.append(exec_line)
exec('\n'.join(exec_script))
fin.close()


##import re
##def find_matches(d, item):
##    for k in d:
##        if re.match(k, item):
##            return d[k]
##
##d = {'a.*': 'a match', 'b.*': 'b match'}
##for item in ['apple', 'beer']:
##    print(find_matches(d, item))

##import keyword as kw
##print(kw.kwlist)

##english_kw={
##        'False',
##        'None',
##        'True',
##        'and',
##        'as',
##        'assert',
##        'async',
##        'await',
##        'break',
##        'class',
##        'continue',
##        'def',
##        'del',
##        'elif',
##        'else',
##        'except',
##        'finally',
##        'for',
##        'from',
##        'global',
##        'if',
##        'import',
##        'in',
##        'is',
##        'lambda',
##        'nonlocal',
##        'not',
##        'or',
##        'pass',
##        'raise',
##        'return',
##        'try',
##        'while',
##        'with',
##        'yield'
##    }
