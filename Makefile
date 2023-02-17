CXX = g++
CFLAGS = -O2 -Wall -Wextra -Wpedantic

SRCS = vec_ram.cpp
OBJS =
TARGET = vec_ram.exe

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CFLAGS) -o $(TARGET) $(SRCS)

test:
	python3 measure_ram_consumption.py

clean:
	rm -f $(TARGET) memory.html
