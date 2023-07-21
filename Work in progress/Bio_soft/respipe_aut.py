import subprocess

# Run with sudo privileges

#Following 3 dependencies are not included
#kraken2 (v2.0.8-beta) https://github.com/DerrickWood/kraken2
#bracken (1.0.0) https://ccb.jhu.edu/software/bracken/
#centrifuge (1.0.3-beta) https://ccb.jhu.edu/software/centrifuge/manual.shtml

# Define the list of bioinformatics tools to install
tools = [
    "-c bioconda nextflow",
    "-c bioconda fastqc",
    "-c bioconda cutadapt",
    "-c bioconda bbmap",
    "-c bioconda samtools", 
    "-c conda-forge ncurses",
    "-c bioconda bedtools",
    "-c bioconda trim-galore",
    "-c bioconda seqtk",
    "-c bioconda hmmer",
    "-c bioconda orfm",
    "-c bioconda diamond", 
    "pandas"]

# Specify the full path to the conda executable
conda_path = input("your full conda executable PATH:")

# Install each tool using conda
for tool in tools:
    print(f"Installing {tool}...")
    subprocess.run([conda_path, "install", tool], check=True)
    print(f"{tool} installed successfully!")
