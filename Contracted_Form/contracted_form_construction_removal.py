from .getWordRelation import * 
def cfcr_start(response_dict):
    print("---------  Contracted Form Construction and Removal ---------------- ")
    matches = []
    for i in response_dict['result']['token_list']:
        response_dict ['cfcr'] = ''
        if( i['word'] in ("'ll", "'d","'ve","'m","'re","'s") ):
            response_dict['CWloc'] = i['index']
            response_dict['DW'] = i['index']
            response_dict = cfcr_top(response_dict)
            if (response_dict ['cfcr'] != ''):
                matches.append(response_dict ['cfcr'])
    cfcr = {}
    cfcr['cfcr'] = matches
    return cfcr
def cfcr_top(response_dict):
    key = response_dict['CWloc']
    wordRel_1 = getRelation(response_dict , key)
    if (wordRel_1 is False):
        return response_dict
    """ Check if Current Word of CW is 'll , 'd , 're , 'm """
    if( wordRel_1 ['CW'] in ("'ll", "'d","'re","'m") ):
        if (wordRel_1 ['PreTag'] in ("NN" , "NNS","NNP","NNPS")) or (wordRel_1 ['PreW'].lower() in ("you","he","she","it","they","how","what","where","who","why","when","that","here","there","those","these")):
            response_dict['AW'] = wordRel_1 ['PreWloc']
            key = response_dict['AW']
            wordRel_2 = getRelation(response_dict , key)
            if (wordRel_2 is False):
                return response_dict
            """ Check if Current Word of CW is 'll , 'd , 're , 'm """
            if(wordRel_2 ['CTag'] in ("NN" , "NNS","NNP","NNPS")):
                key = response_dict['DW']
                wordRel_3 = getRelation(response_dict , key)
                values = {}
                mat = {}
                mat['wrong'] = wordRel_3 ['CW']
                mat['length'] = len(wordRel_3['CW'])
                mat['msg'] = "vague construction, try changing auxiliary/modal into full form."
                mat['offset'] = wordRel_3 ['CWOffset']
                if (wordRel_3 ['CW'] == "'d"):
                    values['value'] = "would"
                    values['value'] = "had"
                elif(wordRel_3 ['CW'] == "'re"):
                    values['value'] = "are"
                elif(wordRel_3 ['CW'] == "'ll"):
                    values['value'] = "will"
                    values['value'] = "shall"
                elif(wordRel_3 ['CW'] == "'m"):
                    values['value'] = "am"
                mat['value']  = values
                matching = match(mat)
                response_dict ['cfcr'] = matching

        elif(wordRel_1 ['PreW'].lower() in ("'ll", "'d","'ve","'m","'re","'s")):
            values = {}
            values['value'] = wordRel_1 ['PreW']
            mat = {}
            mat['wrong'] = wordRel_1 ['PreW']+" "+wordRel_1 ['CW']
            mat['length'] = len(wordRel_1 ['PreW']+" "+wordRel_1 ['CW'])
            mat['msg'] = "Misused contracted form, consider removing it"
            mat['value']  = values
            mat['offset'] = wordRel_1 ['PreOffset']
            matching = match(mat)
            response_dict ['cfcr'] = matching
        else:

            values = {}
            values['value'] = ''
            mat = {}
            mat['wrong'] = wordRel_1 ['PreW']+" "+wordRel_1 ['CW']+" "+wordRel_1 ['PostW']
            mat['length'] = len(wordRel_1 ['PreW']+" "+wordRel_1 ['CW']+" "+wordRel_1 ['PostW'])
            mat['msg'] = "ambiguous construction, try re-writting contracted form with a noun or a pronoun"
            mat['value']  = values
            mat['offset'] = wordRel_1 ['PreOffset']
            matching = match(mat)
            response_dict ['cfcr'] = matching
    elif(wordRel_1 ['CW'] == "'s"):
        if(wordRel_1 ['PreW'].lower() in ("'ll", "'d","'ve","'m","'re","'s")):
            values = {}
            values['value'] = wordRel_1 ['PreW']
            mat = {}
            mat['wrong'] = wordRel_1 ['PreW']+" "+wordRel_1 ['CW']
            mat['length'] = len(wordRel_1 ['PreW']+" "+wordRel_1 ['CW'])
            mat['msg'] = "Misused contracted form, consider removing it"
            mat['value']  = values
            mat['offset'] = wordRel_1 ['PreOffset']
            matching = match(mat)
            response_dict ['cfcr'] = matching
    else:
        if(wordRel_1 ['CW'] == "'ve"):
         
            if (wordRel_1 ['PreTag'] in ("NN" , "NNS","NNP","NNPS")) or (wordRel_1 ['PreW'].lower() in ("you","he","she","it","they","how","what","where","who","why","when","that","here","will","shall","may","might","can","could","would","must","should","there","those","these")):
                response_dict['AW'] = wordRel_1 ['PreWloc']
                key = response_dict['AW']
                wordRel_2 = getRelation(response_dict , key)
                if (wordRel_2 is False):
                    return response_dict
                """ Check if Current Word of CW is 'll , 'd , 're , 'm """
                if(wordRel_2 ['CTag'] in ("NN" , "NNS","NNP","NNPS")):
                    key = response_dict['DW']
                    wordRel_3 = getRelation(response_dict , key)
                    values = {}
                    mat = {}
                    mat['wrong'] = wordRel_3 ['CW']
                    mat['length'] = len(wordRel_3['CW'])
                    mat['msg'] = "vague construction, try changing auxiliary/modal into full form."
                    mat['offset'] = wordRel_3 ['CWOffset']
                    values['value'] = "have"
                    mat['value']  = values
                    matching = match(mat)
                    response_dict ['cfcr'] = matching
            elif(wordRel_1 ['PreW'].lower() in ("'ll", "'d","'ve","'m","'re","'s")):
                values = {}
                values['value'] = wordRel_1 ['PreW']
                mat = {}
                mat['wrong'] = wordRel_1 ['PreW']+" "+wordRel_1 ['CW']
                mat['length'] = len(wordRel_1 ['PreW']+" "+wordRel_1 ['CW'])
                mat['msg'] = "Misused contracted form, consider removing it"
                mat['value']  = values
                mat['offset'] = wordRel_1 ['PreOffset']
                matching = match(mat)
                response_dict ['cfcr'] = matching
            else:
                values = {}
                values['value'] = ''
                mat = {}
                mat['wrong'] = wordRel_1 ['PreW']+" "+wordRel_1 ['CW']+" "+wordRel_1 ['PostW']
                mat['length'] = len(wordRel_1 ['PreW']+" "+wordRel_1 ['CW']+" "+wordRel_1 ['PostW'])
                mat['msg'] = "ambiguous construction, try re-writting contracted form with a noun or a pronoun"
                mat['value']  = values
                mat['offset'] = wordRel_1 ['PreOffset']
                matching = match(mat)
                response_dict ['cfcr'] = matching
    return response_dict
def match(matc): 
    rule = {
        "category": {
            "id": "contracted_forms_cons_rem",
            "name": "Contracted Forms Construction and Removal"
        },
        "description":"Use of ContrConstructRem",
        "id": "contracted_forms_cons_rem",
        "issueType": "misspelling"
    }
    context = {}
    context['length'] = matc['length']
    context['offset'] = matc['offset']
    matches = {}
    matches["errorHeading"] = "Misspelling Mistake"
    matches['context'] = context
    matches['message'] = matc['msg']
    matches['replacements'] =[ matc['value']]
    matches['length'] = matc['length']
    matches['offset'] = matc['offset']
    matches['wrong'] = matc['wrong']
    matches['rule'] = rule
    return matches