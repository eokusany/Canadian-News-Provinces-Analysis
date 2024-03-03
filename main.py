import urllib
from urllib import request
import re
import ssl
# remember to focus on the body of the code (<body>) not the head. look for headline span for cbc

cbcUrl = 'https://www.cbc.ca/news'
windSpeakUrl = 'https://windspeaker.com/'
cbcRequest = request.Request(cbcUrl)
windSpeakRequest = request.Request(windSpeakUrl)
cbcConnection = request.urlopen(cbcRequest)
windSpeakConnection = request.urlopen(windSpeakRequest)
cbcResult = cbcConnection.read()
windSpeakResult = windSpeakConnection.read()
cbcText = str(cbcResult)
windSpeakText = str(windSpeakResult)
windSpeakText = windSpeakText.upper()
cbcText = cbcText.upper()


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# define functions

def clean_text(text):
    # remove HTML commands
    text = re.sub(r'<.*?>', '', text)
    # convert to lowercase and split into words
    word = re.findall(r'\b\w+\b', text.lower())
    # remove words that are shorter than four characters
    word = [w for w in word if len(w) >= 4]
    # remove common prepositions
    prepositions = ['aboard', 'about', 'above', 'across', 'after',
                    'against', 'along', 'amid', 'among', 'anti',
                    'around', 'as', 'at', 'before', 'behind', 'below',
                    'beneath', 'beside', 'besides', 'between',
                    'beyond', 'but', 'by', 'concerning', 'considering',
                    'despite', 'down', 'during', 'except',
                    'excepting', 'excluding', 'following', 'for', 'from',
                    'in', 'inside', 'into', 'like', 'minus',
                    'near', 'of', 'off', 'on', 'onto', 'opposite',
                    'outside', 'over', 'past', 'per', 'plus',
                    'regarding', 'round', 'save', 'since', 'than',
                    'through', 'to', 'toward', 'towards', 'under',
                    'underneath', 'unlike', 'until', 'up', 'upon', 'versus',
                    'via', 'with', 'within', 'without']
    word = [w for w in word if w not in prepositions]
    return word


# function to build the frequency dictionary
def build_frequency_dict(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict



def countProvence(text):
    """ method to count provence mentions in a given website text and returns the results in a list"""
    # make variables
    idx = 0
    AB_count = 0
    BC_count = 0
    PEI_count = 0
    NWT_count = 0
    NS_count = 0
    NL_count = 0
    NB_count = 0
    nunavutCount = 0
    manitobaCount = 0
    ontarioCount = 0
    quebecCount = 0
    saskatchawanCount = 0
    yukonCount = 0
    # make provence name list variables to ensure some names are the same for computer.
    BC = ['british columbia', "british columbia's", "B.C.'s"]
    AB = ['alberta', "alberta's", 'A.B.', "A.B.'s"]
    PEI = ['price edward island', 'P.E.I.', "price edward island's", "P.E.I's"]
    NWT = ['northwest territories', 'N.W.T.', "N.W.T.'s"]
    NS = ['nova scotia', 'N.S.', "nova scotia's", "N.S.'s"]
    NL = ['newfoundland', "newfoundland's", 'N.L.', "newfoundland and labrador's", "N.L.'s"]
    NB = ['new brunswick', 'N.B.', "new brunswick's", "N.B.'s"]
    provenceNames = [AB, BC, PEI, NWT, NS, ['Nunavut', "Nunavut's"], ['Manitoba', "Manitoba's"],
                     ['ontario', "ontario's"], ['quebec', "quebec's"], ['saskatchawan', "saskatchawan's"],
                     ['yukon', "yukon's"], NL, NB]
    # convert text into universal uppercase
    text = text.upper()
    previous = 0
    # find provenances in the text
    for PL in provenceNames:
        for provenceName in PL:
            textFound = text.find(provenceName.upper())
            if textFound != -1:
                if idx == 0:
                    while textFound != -1:
                        AB_count = AB_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 1:
                    while textFound != -1:
                        BC_count = BC_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 2:
                    while textFound != -1:
                        PEI_count = PEI_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 3:
                    while textFound != -1:
                        NWT_count = NWT_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 4:
                    while textFound != -1:
                        NS_count = NS_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 5:
                    while textFound != -1:
                        nunavutCount = nunavutCount + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 6:
                    while textFound != -1:
                        manitobaCount = manitobaCount + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 7:
                    while textFound != -1:
                        ontarioCount = ontarioCount + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 8:
                    while textFound != -1:
                        quebecCount = quebecCount + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 9:
                    while textFound != -1:
                        saskatchawanCount = saskatchawanCount + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 10:
                    while textFound != -1:
                        yukonCount = yukonCount + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                elif idx == 11:
                    print('found a mach for N&L:', provenceName)
                    while textFound != -1:
                        NL_count = NL_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
                    print('number of', provenceName, 'found was:', NL_count - previous)
                    previous = NL_count
                elif idx == 12:
                    while textFound != -1:
                        NB_count = NB_count + 1
                        text = text.replace(provenceName.upper(), '', 1)
                        textFound = text.find(provenceName.upper())
        idx = idx + 1
    # put the variables into a list
    provenceCountList = [AB_count, BC_count, PEI_count, NWT_count, NS_count, NL_count, NB_count, nunavutCount,
                         manitobaCount, ontarioCount, quebecCount, saskatchawanCount, yukonCount]
    return provenceCountList



def printGrid(valueList1, valueList2, totalList):
    """function to print a grid of values given for CBC, windS and their total values"""
    print('provence/territory', 'CBC', 'windS', 'total')
    for idx in range(0, 14):
        if idx == 0:
            print('alberta', '          ', valueList1[idx], '', valueList2[idx], '   ', totalList[idx])
        elif idx == 1:
            print('BC', '               ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 2:
            print('PEI', '              ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 3:
            print('NWT', '              ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 4:
            print('NS', '               ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 5:
            print('N&L', '              ', valueList1[idx], '', valueList2[idx], '   ', totalList[idx])
        elif idx == 6:
            print('NB', '               ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 7:
            print('nunavut', '          ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 8:
            print('manitoba', '         ', valueList1[idx], '', valueList2[idx], '   ', totalList[idx])
        elif idx == 9:
            print('ontario', '          ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 10:
            print('quebec', '           ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 11:
            print('saskatchawan', '     ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        elif idx == 12:
            print('yukon', '            ', valueList1[idx], ' ', valueList2[idx], '   ', totalList[idx])
        else:
            print('')


# execute the functions, save returned values and create total list
cbcList = countProvence(cbcText)
windSpeakList = countProvence(windSpeakText)


idx = 0
totalList = []
for num in cbcList:
    num = num + windSpeakList[idx]
    idx = idx + 1
    totalList.append(num)


printGrid(cbcList, windSpeakList, totalList)


# open the URL and read the HTML content

url = 'https://windspeaker.com/news/windspeaker-news'

response = urllib.request.urlopen(url, context=ctx)
html = response.read().decode()

# extract the text from the body of the page
body_start = html.find('<body')
body_end = html.find('</body')
body = html[body_start:body_end]

# clean the text and build the frequency dictionary
words = clean_text(body)
freq_dict = build_frequency_dict(words)

# sort the dictionary by the frequency of the words and take the top 10 most frequent words
mostFrequent = sorted(freq_dict, key=freq_dict.get, reverse=True)[:10]

# print the top words
idx = 0
print('top ten most frequent topics:')
for key in mostFrequent:
    idx = idx + 1
    print(str(idx) + ')', 'topic:', key)
    print('number of instances:', freq_dict[key])
