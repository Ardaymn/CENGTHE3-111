import math

def forward_pass(network, sample):
    nl=[]
    for i in network:
        if "relu" in i:
            for a in sample:
                yer=sample.index(a)
                if a<=0:
                    sample[yer]=0
        if "sigmoid" in i:
            for b in sample:
                yer=sample.index(b)
                if b>=700:
                    sample[yer]=1
                elif -700<b<700:
                    sample[yer]=1/(1+((math.e)**(-b)))
                elif -700>=b:
                    sample[yer]=0
        if "linear" in i[0]:
            a=0
            b=0
            for sayac in range(0,len(i[1])):
                for sn in range(0,len(sample)):
                    b=b+(sample[sn]*i[1][a][sn])
                a=a+1
                nl.append(b)
                b=0
            sample = list(nl)
            nl=[]
    return sample