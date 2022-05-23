/*
ID: corbin.1
LANG: C++
TASK: skidesign
 */

#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int N;

int main() {

    fstream in_file {"skidesign.in", ios::in};
    in_file >> N;
    vector<int> hills(N);
    for (int i = 0; i < N; i++) {
        in_file >> hills[i];
    }
    in_file.close();
    int trueTotal = 2147483647;
    for (int i = 0; i <= 83; i++) {
        int total = 0;
        pair<int, int> range(i, i+17);
        for (int j = 0; j < N; j++) {
            int height = hills[j];
            if (range.first < height && range.second > height) {
                continue;
            } else if (height < range.first) {
                total += (range.first-height)*(range.first-height);
            } else if (height > range.second) {
                total += (height - range.second)*(height - range.second);
            }
        }
        if (total < trueTotal) {
            trueTotal = total;
        }
    }
    fstream out_file {"skidesign.out", ios::out};
    out_file << trueTotal << endl;
    out_file.close();
}
