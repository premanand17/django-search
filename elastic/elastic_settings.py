''' Used to manage and retrieve Elastic settings. '''
from django.conf import settings
from elastic.exceptions import SettingsError


class ElasticSettings:
    ''' Manage settings for the Elastic elastic app '''

    @classmethod
    def attrs(cls, cluster='default'):
        ''' Return list of attributes for a elastic cluster '''
        return getattr(settings, 'ELASTIC').get(cluster, None)

    @classmethod
    def getattr(cls, name, cluster='default'):
        ''' Get a named attribute '''
        return cls.attrs(cluster).get(name, None)

    @classmethod
    def idx(cls, name='DEFAULT', idx_type=None, cluster='default'):
        ''' Given the index name and optionally a type get the index URL path.
        If 'DEFAULT' is requested but not defined return the random index. '''
        idxs = cls.getattr('IDX', cluster=cluster)
        if name in idxs:
            if isinstance(idxs[name], dict):
                idx = idxs[name]['name']
                if 'idx_type' not in idxs[name]:
                    raise SettingsError('Index type key (idx_type) not found for '+idx)
                if idx_type is not None:
                    if idx_type in idxs[name]['idx_type']:
                        return idx+'/'+idxs[name]['idx_type'][idx_type]
                    else:
                        raise SettingsError('Index type key ('+idx_type+') not found.')
                else:
                    return idx
            return idxs[name]
        else:
            if name == 'DEFAULT':
                name = list(idxs.keys())[0]
                return ElasticSettings.idx(name=name, idx_type=idx_type, cluster=cluster)
        return None

    @classmethod
    def url(cls, cluster='default'):
        ''' Return the Elastic URL '''
        return cls.getattr('ELASTIC_URL', cluster=cluster)

    @classmethod
    def indices_str(cls, cluster='default'):
        ''' Get a comma separated list of indices '''
        attrs = cls.attrs(cluster).get('IDX')
        s = set()
        for v in attrs.values():
            if isinstance(v, dict):
                s.add(v['name'])
            else:
                s.add(v)
        return ','.join(str(e) for e in s)
