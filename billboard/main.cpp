#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

/*
1 2 3 5
6 0 10 4
2 1 8 3
 */

pair<pair<int, int>, pair<int, int>> bill1, bill2;

bool isCovered(pair<int, int> point) {

    if (point.first >= bill1.first.first && point.first < bill1.second.first) {
        if (point.second < bill1.second.second && point.second >= bill1.first.second) {
            return true;
        }
    }
    if (point.first >= bill2.first.first && point.first < bill2.second.first) {
        if (point.second < bill2.second.second && point.second >= bill2.first.second) {
            return true;
        }
    }

    return false;
}

int main() {
    fstream in_file {"billboard.in", ios::in};

    pair<pair<int, int>, pair<int, int>> truck;

    in_file >> bill1.first.first >> bill1.first.second >> bill1.second.first >> bill1.second.second;
    in_file >> bill2.first.first >> bill2.first.second >> bill2.second.first >> bill2.second.second;
    in_file >> truck.first.first >> truck.first.second >> truck.second.first >> truck.second.second;

    in_file.close();

    cout << "(" << bill1.first.first << ", " << bill1.first.second << "), (" << bill1.second.first << ", " << bill1.second.second  << ")" << endl;
    cout << "(" << bill2.first.first << ", " << bill2.first.second << "), (" << bill2.second.first << ", " << bill2.second.second << ")" << endl;
    cout << "(" << truck.first.first << ", " << truck.first.second << "), (" << truck.second.first << ", " << truck.second.second << ")" << endl;

    int area1 = abs((bill1.first.first - bill1.second.first) * (bill1.second.second - bill1.first.second));
    int area2 = abs((bill2.first.first - bill2.second.first) * (bill2.second.second - bill2.first.second));
    cout << area1 << endl;
    cout << area2 << endl;
    int count = 0;
    for (int x = truck.first.first; x < truck.second.first; x++) {
        for (int y = truck.first.second; y < truck.second.second; y++) {
            pair<int, int> point(x, y);

            if (isCovered(point)) {
                count++;
            }


        }
    }

    fstream out_file {"billboard.out", ios::out};
    out_file << area1 + area2 - count << endl;
    out_file.close();

    return 0;
}
