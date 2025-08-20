import sys

# Minimal FASTQ to VCF simulation
fastq_path = sys.argv[1]
vcf_path = sys.argv[2]

with open(vcf_path, 'w') as vcf:
    vcf.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
    vcf.write('chr1\t1010\t.\tA\tT\t100\tPASS\t.\n')
    vcf.write('chr1\t1020\t.\tG\tA\t100\tPASS\t.\n')
