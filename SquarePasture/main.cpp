#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    fstream in_file {"square.in", ios::in};

    vector<int> x, y;

    bool toggle = false;
    for (int i = 0; i < 8; i++) {

        int value;
        in_file >> value;
        if (!toggle) {
            x.push_back(value);
        }
        else {
            y.push_back(value);
        }


        toggle = !toggle;
    }
    in_file.close();

    int xMax = *max_element(x.begin(), x.end());
    int xMin = *min_element(x.begin(), x.end());
    int yMax = *max_element(y.begin(), y.end());
    int yMin = *min_element(y.begin(), y.end());

    int totMax;

    if (xMax - xMin < yMax - yMin) {
        totMax = yMax - yMin;
    } else {
        totMax = xMax - xMin;
    }

    fstream out_file {"square.out", ios::out};
    out_file << totMax * totMax;
    out_file.close();

    return 0;


}
