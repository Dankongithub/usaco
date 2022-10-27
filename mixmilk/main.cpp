#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>

using namespace std;


vector<int> caps(3, 0);
vector<int> volumes(3, 0);

void pour(int from, int to) {
    if (volumes[from] <= caps[to] - volumes[to]) {
        volumes[to] += volumes[from];
        volumes[from] = 0;
    } else {
        volumes[from] -= caps[to] - volumes[to];
        volumes[to] = caps[to];
    }
}

int main() {

    fstream fin {"mixmilk.in", ios::in};

    for (int i = 0; i < 3; i++) {
        fin >> caps[i];
        fin >> volumes[i];
    }
    fin.close();

    int from = 0;
    int to = 1;
    for (int i = 0; i < 100; i++) {

        pour(from, to);

        if (from == 2) {
            from = 0;
        } else {
            from += 1;
        }
        if (to == 2) {
            to = 0;
        } else {
            to += 1;
        }
    }

    fstream fout {"mixmilk.out", ios::out};

    fout << volumes[0] << endl << volumes[1] << endl << volumes[2] << endl;
    fout.close();


    return 0;
}
