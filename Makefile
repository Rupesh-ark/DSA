CXX := c++
CXXFLAGS := -std=c++20 -Wall -Wextra -Wpedantic
PYTHON := python3
BUILD_DIR := build

EXERCISES := $(sort $(patsubst exercises/%.cpp,%,$(shell find exercises -name '*.cpp' 2>/dev/null)))

.PHONY: help today log stats list build run check clean

help:
	@echo "DSA learning project"
	@echo
	@echo "Commands:"
	@echo "  make today                             Show today's quest and reviews"
	@echo "  make log                               Record a completed study session"
	@echo "  make stats                             Show XP, streaks, and mastery"
	@echo "  make list                              List local C++ exercises"
	@echo "  make build EXERCISE=arrays/reverse_array  Compile one exercise"
	@echo "  make run EXERCISE=arrays/reverse_array    Compile and run one exercise"
	@echo "  make check                             Verify the tracker and exercises"
	@echo "  make clean                             Remove generated files"

today:
	@$(PYTHON) tools/tracker.py today

log:
	@$(PYTHON) tools/tracker.py log

stats:
	@$(PYTHON) tools/tracker.py stats

list:
	@printf '%s\n' $(EXERCISES)

build:
	@test -n "$(EXERCISE)" || (echo "Set EXERCISE, for example: make build EXERCISE=arrays/reverse_array" && exit 1)
	@test -f "exercises/$(EXERCISE).cpp" || (echo "Unknown exercise: $(EXERCISE)" && exit 1)
	@mkdir -p "$(dir $(BUILD_DIR)/$(EXERCISE))"
	$(CXX) $(CXXFLAGS) "exercises/$(EXERCISE).cpp" -o "$(BUILD_DIR)/$(EXERCISE)"

run: build
	@"$(BUILD_DIR)/$(EXERCISE)"

check:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests
	@set -e; for exercise in $(EXERCISES); do \
		$(MAKE) --no-print-directory run EXERCISE="$$exercise"; \
	done

clean:
	rm -rf "$(BUILD_DIR)"
