#include <iostream>
#include <random>
#include <fstream>

using namespace std;

int random_value(int from, int to) {
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> segment(from, to);
	return segment(gen);
}

int main() {
	int mas[128];
	for (int i = 0; i < 128; i++)
		mas[i] = random_value(0, 1);
	ofstream out;
	out.open("C:/Users/nasty/isb/lab_2/sequence_c.txt");
	if (out.is_open())
		for (auto i : mas)
			out << i;
	out.close();
	cout << "File has been written" << std::endl;
	return 0;
}