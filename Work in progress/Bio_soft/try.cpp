#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

// Function to calculate DNA statistics
void calculateDNAStatistics(const string& sequence) {
    int countA = 0, countT = 0, countC = 0, countG = 0;
    int totalCount = 0;

    // Count the occurrence of each nucleotide
    for (char nucleotide : sequence) {
        switch (nucleotide) {
            case 'A':
                countA++;
                break;
            case 'T':
                countT++;
                break;
            case 'C':
                countC++;
                break;
            case 'G':
                countG++;
                break;
            default:
                // Ignore any other characters
                break;
        }
        totalCount++;
    }

    // Calculate GC content
    int countGC = countG + countC;
    double gcContent = (totalCount > 0) ? (static_cast<double>(countGC) / totalCount) * 100.0 : 0.0;

    // Display the statistics
    cout << "DNA Statistics:" << endl;
    cout << "Total Nucleotides: " << totalCount << endl;
    cout << "A: " << countA << endl;
    cout << "T: " << countT << endl;
    cout << "C: " << countC << endl;
    cout << "G: " << countG << endl;
    cout << "GC Content: " << fixed << setprecision(2) << gcContent << "%" << endl;
}

int main() {
    // DNA sequence input
    string sequence;
    cout << "Enter the DNA sequence: ";
    getline(cin, sequence);

    // Calculate and display DNA statistics
    calculateDNAStatistics(sequence);

    return 0;
}
