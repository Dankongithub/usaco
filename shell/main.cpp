// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main() {
	fstream in_file {"shell.in", ios::in};


	int N;
	in_file >> N;

	vector<char> board{'a', '1', '2', '3'};

	map<char, int> scores = {{'1', 0}, {'2', 0}, {'3', 0}};

	char max = '1';

	for (int i = 0; i < N; i++) {
		int sw1, sw2, guess;
		in_file >> sw1 >> sw2 >> guess;

		char tmp = board[sw1];
		board[sw1] = board[sw2];
		board[sw2] = tmp;

		scores[board[guess]]++;

		if (scores[board[guess]] > scores[max]) {
			max = board[guess];
		}
		
	}
	in_file.close();

	fstream out_file {"shell.out", ios::out};
	out_file << scores[max];
}
