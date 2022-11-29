// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <vector>
using namespace std;

int search(int value, vector<int> vec) {
	for (int i = 0; i < vec.size(); i++) {
		if (value == vec[i]) {
			return i;
		}
	}
	return -1;
}

void printSet(std::unordered_set<int> const &s)
{
    std::copy(s.begin(),
            s.end(),
            std::ostream_iterator<int>(std::cout, " "));
	cout << endl;
}

void printVec(vector<int> vec) {
	for (int i : vec) {
		cout << i << " ";
	}
	cout << endl;
}

void printVec(vector<vector<int>> vec) {
	for (vector<int> i : vec) {
		for (int j : i) {
			cout << j << " ";
		}
		cout << endl;
	}
}


int main() {
	int K, N;
	cin >> K >> N;
	
	vector<vector<int>> meetData; 

	for (int i = 0; i < K; i++) {
		vector<int> meet;
		for (int j = 0; j < N; j++) {
			int place;
			cin >> place;
			meet.push_back(place);
		}
		meetData.push_back(meet);
	}

	printVec(meetData);

	cout << "-------------" << endl;

	/* For each cow, look to the right and see if one number is consistently
	larger than itself. */

	for (int i = 0; i < N; i++) {

		unordered_set<int> consistents;

		for (int j = 1; j <= N; j++) {
			consistents.insert(j);
		}

		for (int j = 0; j < K; j++) {
			for (int l = 0; l < search(i, meetData[j]); l++) {
				consistents.erase(consistents.find(meetData[j][l]), consistents.end());
			}
		}		
		printSet(consistents);
	}
}
