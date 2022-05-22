/*
ID: corbin.1
LANG: C++
TASK: wormhole
 */

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>


using namespace std;
#define MAX_N 12

string strN;
int N;

int partner[MAX_N+1];
vector<pair<int, int>> pairs;

void printPairs(vector<pair<int, int>> coords) {
    for (pair<int, int> pair : coords) {
        cout<< "(" << pair.first << ", " << pair.second << ") ";
    }
    cout << endl;
}

void printPartner() {
    for (int i : partner) {
        cout << i << " ";
    }
    cout << endl;
}

int FindNextOnRight(int point) {
    pair<int, int> pair = pairs[point];
    int next_on_right = -1;

    for (int l = 0; l < N; l++) {
        if (l != point) {
            if (next_on_right == -1) {
                if (pair.second == pairs[l].second && pair.first < pairs[l].first) {
                    next_on_right = l;
                }
            } else {
                if (pair.second == pairs[l].second && pair.first < pairs[l].first && pairs[l].first - pair.first < pairs[next_on_right].first - pair.first) {
                    next_on_right = l;
                }
            }
        }
    }
    return next_on_right;
}

bool checkLoop() {
    int start, location;

    // for every start point
    for (int i = 1; i <= N; i++) {
        start = location = i-1;
        while (true) {
            int next_on_right = FindNextOnRight(location);

            if (next_on_right == -1) {
                break;
            }

            location = partner[next_on_right + 1] - 1;

            if (start == location) {
                return true;
            }
        }
    }
    return false;
}

int solve() {
    int i, total=0;
    for (i=1; i<=N; i++)
        if (partner[i] == 0) break;

    if (i > N) {
        printPartner();
        if (checkLoop()) {
            return 1;
        } else {
            return 0;
        }
    }

    for (int j=i+1; j<=N; j++)
        if (partner[j] == 0) {
            partner[i] = j;
            partner[j] = i;
            total += solve();
            partner[i] = partner[j] = 0;
        }
    return total;
}

int main() {
    // input
    fstream in_file {"wormhole.in", ios::in};
    getline(in_file, strN);
    N = stoi(strN);

    for (int i = 0; i < N; i++) {
        int x, y;
        in_file >> x >> y;
        pair<int, int> pair = {x, y};
        pairs.push_back(pair);
    }
    in_file.close();

    fstream out_file {"wormhole.out", ios::out};

    out_file << solve() << endl;
    out_file.close();

}