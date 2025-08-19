# Simulated Genomic ETL Pipeline
# This script simulates FASTQ -> VCF -> annotated table
import csv
import random
from pathlib import Path

def simulate_fastq_to_vcf(fastq_path, vcf_path):
    # Simulate variant calling: write a few fake variants
    with open(vcf_path, 'w') as vcf:
        vcf.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
        for i in range(1, 6):
            chrom = 'chr1'
            pos = 1000 + i * 10
            ref = random.choice(['A', 'T', 'C', 'G'])
            alt = random.choice([b for b in 'ATCG' if b != ref])
            vcf.write(f'{chrom}\t{pos}\t.\t{ref}\t{alt}\t100\tPASS\t.\n')

def simulate_vcf_to_annotated_table(vcf_path, table_path):
    # Simulate annotation: add a clinical significance column
    with open(vcf_path) as vcf, open(table_path, 'w', newline='') as out:
        reader = csv.DictReader(
            (row for row in vcf if not row.startswith('#')),
            delimiter='\t',
            fieldnames=['CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO']
        )
        writer = csv.writer(out)
        writer.writerow(['CHROM','POS','REF','ALT','CLIN_SIG'])
        for row in reader:
            clin_sig = random.choice(['benign', 'pathogenic', 'VUS'])
            writer.writerow([row['CHROM'], row['POS'], row['REF'], row['ALT'], clin_sig])

def run_pipeline():
    data_dir = Path(__file__).parent / 'data'
    data_dir.mkdir(exist_ok=True)
    fastq = data_dir / 'sample.fastq'
    vcf = data_dir / 'sample.vcf'
    table = data_dir / 'annotated_variants.csv'
    # Create a dummy FASTQ file
    fastq.write_text('@SEQ_ID\nGATTACA\n+\n!!!!!!!\n')
    simulate_fastq_to_vcf(fastq, vcf)
    simulate_vcf_to_annotated_table(vcf, table)
    print(f'Pipeline complete. Annotated table: {table}')

if __name__ == '__main__':
    run_pipeline()
