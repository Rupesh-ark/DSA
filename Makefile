CXX := c++
CXXFLAGS := -std=c++20 -Wall -Wextra -Wpedantic
BUILD_DIR := build

EXERCISES := $(patsubst exercises/%.cpp,%,$(shell find exercises -name '*.cpp' 2>/dev/null))

.PHONY: help list build run clean

help:
	@echo "DSA learning project"
	@echo
	@echo "Commands:"
	@echo "  make list                              List available exercises"
	@echo "  make build EXERCISE=arrays/reverse_array  Compile one exercise"
	@echo "  make run EXERCISE=arrays/reverse_array    Compile and run one exercise"
	@echo "  make clean                             Remove generated files"

list:
	@printf '%s\n' $(EXERCISES)

build:
	@test -n "$(EXERCISE)" || (echo "Set EXERCISE, for example: make build EXERCISE=arrays/reverse_array" && exit 1)
	@test -f "exercises/$(EXERCISE).cpp" || (echo "Unknown exercise: $(EXERCISE)" && exit 1)
	@mkdir -p "$(dir $(BUILD_DIR)/$(EXERCISE))"
	$(CXX) $(CXXFLAGS) "exercises/$(EXERCISE).cpp" -o "$(BUILD_DIR)/$(EXERCISE)"

run: build
	@"$(BUILD_DIR)/$(EXERCISE)"

clean:
	rm -rf "$(BUILD_DIR)"
