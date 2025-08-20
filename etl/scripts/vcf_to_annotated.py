import sys
import csv

# Minimal VCF to annotated CSV simulation
vcf_path = sys.argv[1]
csv_path = sys.argv[2]

with open(vcf_path) as vcf, open(csv_path, 'w', newline='') as out:
    reader = csv.DictReader(
        (row for row in vcf if not row.startswith('#')),
        delimiter='\t',
        fieldnames=['CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO']
    )
    writer = csv.writer(out)
    writer.writerow(['CHROM','POS','REF','ALT','CLIN_SIG'])
    for row in reader:
        writer.writerow([row['CHROM'], row['POS'], row['REF'], row['ALT'], 'benign'])
