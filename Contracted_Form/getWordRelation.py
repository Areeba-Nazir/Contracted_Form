
def getRelation(response_dict , key):
    # key = key
    for i in response_dict['result']['token_list']:
        if i['index'] == key:
            # key = i['index']
            response_dict['CW'] = i['word']
            response_dict['CTag'] = i['pos']
            response_dict['CWOffset'] = i['characterOffsetBegin']
    # # Pre Words
        if key == 1 :
            response_dict['PreW'] =  ''
            response_dict['PreWloc'] =  ''
            response_dict['PreTag'] =  ''   
        else :
            response_dict['PreWloc'] = key  - 1
            if i['index'] == response_dict['PreWloc']:
                response_dict['PreW'] = i['word']
                response_dict['PreTag'] = i['pos']
                response_dict['PreOffset'] = i['characterOffsetBegin']
        # #  Post Words 
        if key == response_dict['last_index']:
            response_dict['PostW'] =  ''
            response_dict['PostWloc'] =  ''
            response_dict['PostTag'] =  ''
        else:
            response_dict['PostWloc'] = key + 1
            if i['index'] == response_dict['PostWloc']:
                response_dict['PostW'] = i['word']
                response_dict['PostTag'] = i['pos']
                response_dict['PostOffset'] = i['characterOffsetBegin']
    return response_dict
