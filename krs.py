def get_krs_obj(krs):
    with open('krs.json', 'r') as f:
        krs_json = json.loads(f.read())
    out_objs = []

    krs = krs_json['Dataobject']
    for obj in krs:
        out = {}
        out['id'] = obj['id']
        out['url'] = obj['url']
        out['nazwa'] = obj['data']['krs_podmioty.nazwa']
        out['nip'] = obj['data']['krs_podmioty.nip']
        out['regon'] = obj['data']['krs_podmioty.regon']
        out['date_created'] = obj['data']['krs_podmioty.data_dokonania_wpisu']
        out_objs.append(out)

    return out_objs