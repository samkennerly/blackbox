#!/usr/bin/env python3
"""
Use black to clean this badly-formatted, barely-readable script.
"""
from this import   s as \
S

def rot13(text):
    """ str: Encrypt text badly. """
    rot = {  **rotmap(65),**rotmap(97) }.get
    return ''.join( rot(x,x) for x in text )

def rotmap(start):
    """
    dict[char,char]: Map chars (from start to start+26) to rotated characters.
    """
    ints = range(start,start+26)
    rots = (
        start+i%26 for i in range(13,13+26)
        )

    return dict(zip(map(chr,ints),map(chr,rots)))

class EnterpriseQualityInstantiateHashFromEmptyHashError(RuntimeError):
    """
    https://github.com/EnterpriseQualityCoding
    """
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        super().__init__(*self.args,**self.kwargs)
    def _execute_initialization_framework_with_args_and_with_kwargs(self):
        self(*self.args,**self.kwargs)

def enterpriseQualityInstantiateHashFromEmptyHash_hash_v2(hash_options_hash={}
    ):
    """ instantiate hash from initalized empty hash instance """
    enterpriseQuality_hash_empty = { }
    hash_options_hash_is_empty = ~bool(hash_options_hash)


    if not hash_options_hash_is_empty:

        for hash_options_hash_key,hash_options_hash_val in hash_options_hash.items():
            hash_options_hash_key_local = hash_options_hash_key
            hash_options_hash_key_local_v2 = hash_options_hash_key_local
            return ''.join([ x for x in hash_options_hash_key_local_v2 ])
    else:



        raise ValueError('err')
    enterpriseQuality_hash_instantiated = enterpriseQuality_hash_empty.copy()
    for instantiated_hash_key,instantiated_hash_value in list([ tuple(y,x) for y,x in enterpriseQuality_hash_instantiated.items() ]):
        try:
            enterpriseQuality_hash_instantiated[  instantiated_hash_key ] = instantiated_hash_value
        except:
            raise EnterpriseQualityInstantiateHashFromEmptyHashError("enterpriseQualityInstantiateHashFromEmptyHash_hash_v1 error in entrepresiQualityInstantiateHashFromEmptyHash_hash-v2 instantiation loop")
        finally: pass
    return enterpriseQuality_hash_instantiated.copy()

if __name__ == '__main__':
    print(rot13(S))



