#include <cstdlib>
#include <cstdio>
#include <vector>

void run_test(size_t test_size) {
	std::vector<size_t> v;

	for (size_t i = 0; i < test_size; i++) {
		v.push_back(i);
	}

	printf("OK\n");
	fflush(stdout);
	getchar();
}

int main(int argc, char* argv[]) {
	if (argc < 2) {
		printf("Usage: ./vec_ram.exe 1000\n");
		exit(-1);
	}

	size_t test_size;

	sscanf(argv[1], "%zu", &test_size);

	run_test(test_size);

	return 0;
}
