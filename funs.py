import numpy as np
import random
#import Bio.Seq
NTS=('A','C','G','T')


def rand_nuc(k) : 
    return ''.join(random.choices(NTS,k=k))


def gen_spacer_like() : 
    return rand_nuc(20)

def gen_pbs_like(spacer,length=None) : 

    if length is None : 
        length=random.randint(4,12)+random.randint(4,12)

    remnant=len(spacer)-3-length
    spmatch=spacer[max(remnant,0):-3]

    if remnant < 0 : 
        rest=rand_nuc(-1*remnant)
    else : 
        rest=''

    return spmatch+rest

def gen_rtt_like(length=None) : 
    if length is None : 
        length=random.randint(4,20)+random.randint(4,20)
    return rand_nuc(length)

def gen_triple() : 
    spacer=gen_spacer_like()
    return (spacer,gen_pbs_like(spacer),gen_rtt_like())

def gc_aberration(s) : 
    pgc=sum([ 1 for c in s if c == 'G' or c == 'C' ])/len(s)
    return (pgc-0.5)*2

def length_aberration(s) : 
    ls=len(s)
    if ls == 25 : 
        return 0
    if ls < 25 : 
        return (ls-8)/17 #from 0 to 17
    return np.sqrt((ls-25))/np.sqrt(30)


def f3_worker(triple) : 
    ext3=triple[1]+triple[2]
    dev=(gc_aberration(ext3)+length_aberration(ext3))**2
    score=1/(1+3*dev)
    score=score*100
    return score


def fun1(s: str, i: int, c: str) -> (bool, str):
    # Example: reject if string empty
    if not s:
        return False, 'Input string cannot be empty.'
    return True, 'OK'

def fun2(s: str, i: int, c: str):
    # Return an (n,3) list of strings (n capped at 1024)
    n=random.randint(1,512)+random.randint(1,512)
    return [ gen_triple() for _n in range(n) ] 

def fun3(arr):
    # Return a float score per row (e.g., sum of string lengths)
    scores=[ f3_worker(triple) for triple in arr ]
    return [ (*_arr,s) for _arr,s in zip(arr,scores) ]
