import primer3

input = snakemake.input[0]
output = snakemake.output[0]

sequence = ''
with open(input,'r',encoding='UTF8') as consensus:
    counter = 0
    for line in consensus:
        if counter != 0:
            sequence += line
        else:
            counter += 1

sequence = sequence.replace('\n','')
sequence = sequence.replace('-','N')
sequence = sequence.replace('U','T')


primers = primer3.bindings.design_primers(
    seq_args={
        'SEQUENCE_ID': 'DWV',
        'SEQUENCE_TEMPLATE': sequence,
    },
    global_args={
        'PRIMER_OPT_SIZE': 20,
        'PRIMER_PICK_INTERNAL_OLIGO': 1,
        'PRIMER_INTERNAL_MAX_SELF_END': 8,
        'PRIMER_MIN_SIZE': 18,
        'PRIMER_MAX_SIZE': 25,
        'PRIMER_OPT_TM': 60.0,
        'PRIMER_MIN_TM': 57.0,
        'PRIMER_MAX_TM': 63.0,
        'PRIMER_MIN_GC': 20.0,
        'PRIMER_MAX_GC': 80.0,
        'PRIMER_MAX_POLY_X': 100,
        'PRIMER_INTERNAL_MAX_POLY_X': 100,
        'PRIMER_SALT_MONOVALENT': 50.0,
        'PRIMER_DNA_CONC': 50.0,
        'PRIMER_MAX_NS_ACCEPTED': 0,
        'PRIMER_MAX_SELF_ANY': 12,
        'PRIMER_MAX_SELF_END': 8,
        'PRIMER_PAIR_MAX_COMPL_ANY': 12,
        'PRIMER_PAIR_MAX_COMPL_END': 8,
        'PRIMER_PRODUCT_SIZE_RANGE': [
            [75,100],[100,125],[125,150],
            [150,175],[175,200],[200,225]
        ],
    })

with open(output, 'w', encoding='UTF8') as primer_file:
    for key, value in primers.items():
        primer_file.write(f"{key}: {value}\n")

