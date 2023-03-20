
def gen_json (path) :
    skill_json = {}
    with open(path, 'r') as infile:
        for l in infile.readlines():
            cur = l.split(",")
            skill = cur.pop(0).rstrip()
            skill_json[skill] = [x.rstrip() for x in cur if x.rstrip() != ""]
    return skill_json

def dict_to_json (dict, path):
    with open(path,"w") as outfile: 
        json.dump(dict,outfile,indent=4)

if __name__ == '__main__':
    import json
    import sys
    path = sys.argv[1]
    skill_json = gen_json(path)
    dict_to_json(skill_json,sys.argv[2])
       