import pandas as pd

idiomas = ['cat', 'eng', 'eus', 'glg', 'por', 'spa']

rutaEngKafe = 'engProlog30\wn_g.pl'
rutaAdimenSUMO = ''
rutaBLC = ''
rutaDomains = ''
rutaMarks = ''
rutaTopOntology = ''

for i in idiomas:
    rutaVariant = 'mcr\\'+i+'WN\wei_'+i+'-30_variant.tsv'
    rutaSynset = 'mcr\\'+i+'WN\wei_'+i+'-30_synset.tsv'
    rutaRelation = 'mcr\\'+i+'WN\wei_'+i+'-30_relation.tsv'
    rutaExamples = 'mcr\\'+i+'WN\wei_'+i+'-30_examples.tsv'
    rutaToIli = 'mcr\\'+i+'WN\wei_'+i+'-30_to_ili.tsv'

# FICHERO VARIANT
    print('Abriendo fichero ' + rutaVariant)
    ficheroLecturaVariant = open(rutaVariant,'r', encoding='utf-8')
    lineasVariant = ficheroLecturaVariant.readlines()

    Word = []
    Senses = []
    SynsetPoS = []
    PoS = []
    Conf = []
    Exp = []
    Mark = []

    for linea in lineasVariant:
        linea = linea.split('\t')

        Word.append(linea[0])
        Senses.append(linea[1])
        SynsetPoS.append(linea[2])
        PoS.append(linea[3])
        Conf.append(linea[4])
        Exp.append(linea[5])
        Mark.append(linea[6][0:-1])

    dfVariant = pd.DataFrame({"Word": Word, "Senses": Senses, "SynsetPoS": SynsetPoS, "PoS": PoS, "Conf": Conf, "Exp": Exp, "Mark": Mark})
    dfVariant.to_csv('mcrDF/'+i+'WN/wei_'+i+'-30_variant.csv')

    ficheroLecturaVariant.close()

#FICHERO SYNSET
    print('Abriendo fichero ' + rutaSynset)

    ficheroLecturaSynset = open(rutaSynset,'r', encoding='utf-8')
    lineasSynset = ficheroLecturaSynset.readlines()

    SynsetPoS = []
    PoS = []
    Desc = []
    Glosa = []
    MaxNiv = []
    Niv = []
    Mark = []

    for linea in lineasSynset:
        linea = linea.split('\t')

        SynsetPoS.append(linea[0])
        PoS.append(linea[1])
        Desc.append([linea[2], linea[3], linea[4], linea[5]])
        Glosa.append(linea[6])
        MaxNiv.append(linea[7])
        Niv.append(linea[8])
        Mark.append(linea[9][0:-1])

    dfSynset = pd.DataFrame({"SynsetPoS": SynsetPoS, "PoS": PoS, "Desc": Desc, "Glosa": Glosa, "MaxNiv": MaxNiv, "Niv": Niv, "Mark": Mark})
    dfSynset.to_csv('mcrDF/'+i+'WN/wei_'+i+'-30_synset.csv')

    ficheroLecturaSynset.close()

#FICHERO RELATION
    print('Abriendo fichero ' + rutaRelation)

    ficheroLecturaRelation = open(rutaRelation,'r', encoding='utf-8')
    lineasRelation = ficheroLecturaRelation.readlines()

    Rel_ID = []
    S_Synset = []
    S_PoS = []
    T_Synset = []
    T_PoS = []
    Conf = []
    Info = []

    for linea in lineasRelation:
        linea = linea.split('\t')

        Rel_ID.append(linea[0])
        S_Synset.append(linea[1])
        S_PoS.append(linea[2])
        T_Synset.append(linea[3])
        T_PoS.append(linea[4])
        Conf.append(linea[5])
        Info.append(linea[6])

    dfRelation = pd.DataFrame({"Rel_ID": Rel_ID, "S_Synset": S_Synset, "S_PoS": S_PoS, "T_Synset": T_Synset, "T_PoS": T_PoS, "Conf": Conf, "Info": Info})
    dfRelation.to_csv('mcrDF/'+i+'WN/wei_'+i+'-30_relation.csv')
    
    ficheroLecturaRelation.close()

# FICHERO EXAMPLES
    print('Abriendo fichero ' + rutaExamples)
    ficheroLecturaExamples = open(rutaExamples,'r', encoding='utf-8')
    lineasExamples = ficheroLecturaExamples.readlines()

    Word = []
    Senses = []
    Glosa = []
    PoS = []
    SynsetPoS = []

    for linea in lineasExamples:
        linea = linea.split('\t')

        Word.append(linea[0])
        Senses.append(linea[1])
        Glosa.append(linea[2])
        PoS.append(linea[3])
        SynsetPoS.append(linea[4][:-1])

    dfExamples = pd.DataFrame({"Word": Word, "Senses": Senses, "Glosa": Glosa, "PoS": PoS, "SynsetPoS": SynsetPoS})
    dfExamples.to_csv('mcrDF/'+i+'WN/wei_'+i+'-30_examples.csv')

    ficheroLecturaExamples.close()


# FICHERO TO ILI
    print('Abriendo fichero ' + rutaToIli)
    ficheroLecturaToIli = open(rutaToIli,'r', encoding='utf-8')
    lineasToIli = ficheroLecturaToIli.readlines()

    ili = []
    PoS = []
    to = []
    wn = []
    version = []

    for linea in lineasToIli:
        linea = linea.split('\t')

        ili.append(linea[0])
        PoS.append(linea[1])
        to.append(linea[2])
        wn.append(linea[3])
        version.append(linea[4][:-1])

    dfToIli = pd.DataFrame({"ILI Synset": ili, "PoS": PoS, "TO Synset": to, "WordNet": wn, "Version": version})
    dfToIli.to_csv('mcrDF/'+i+'WN/wei_'+i+'-30_to_ili.csv')

    ficheroLecturaToIli.close()

    print()

#TODO: HACERLO CON TODOS LOS FICHEROS: AdimenSUMO, BLC, Domains, Marks, TopOntology

print('Abriendo fichero ' + rutaEngKafe)

ficheroEng = open('engProlog30\wn_g.pl', encoding='utf-8')

lineasEng = ficheroEng.readlines()

SynsetsENG = []
GlosaENG = []

for linea in lineasEng:
    linea = linea[2:-3]
    GlosaENG.append(linea[11:-1])
    lineaComas = linea.split(',')
    SynsetsENG.append(int(lineaComas[0]))

dfEng = pd.DataFrame({"Synset":SynsetsENG, "Glosa":GlosaENG})
dfEng.to_csv('engProlog30DF\wn_g.csv')

ficheroEng.close()

#WN_G ERIC KAFE
print('Abriendo fichero ' + rutaEngKafe)

ficheroEng = open('engProlog30\wn_g.pl', encoding='utf-8')

lineasEng = ficheroEng.readlines()

SynsetsENG = []
GlosaENG = []

for linea in lineasEng:
    linea = linea[2:-3]
    GlosaENG.append(linea[11:-1])
    lineaComas = linea.split(',')
    SynsetsENG.append(int(lineaComas[0]))

dfEng = pd.DataFrame({"Synset":SynsetsENG, "Glosa":GlosaENG})
dfEng.to_csv('engProlog30DF\wn_g.csv')

ficheroEng.close()