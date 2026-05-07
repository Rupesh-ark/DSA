CXX = g++
CXXFLAGS = -std=c++17 -O2 -Wall -Wextra -g

# Usage:
#   make new P=arrays/two_sum        (creates problem folder with sol.cpp, input.txt, output.txt)
#   make run P=arrays/two_sum        (compiles and runs, auto-uses input.txt if present)
#   make test P=arrays/two_sum       (compares actual output against output.txt)
#   make debug P=arrays/two_sum      (runs with sanitizers)

P ?=
SRC = $(P)/sol.cpp
INPUT = $(P)/input.txt
OUTPUT = $(P)/output.txt

run:
	@if [ -z "$(P)" ]; then echo "Usage: make run P=topic/problem"; exit 1; fi
	$(CXX) $(CXXFLAGS) -o /tmp/dsa_out $(SRC)
	@if [ -f $(INPUT) ]; then \
		echo "--- Running with $(INPUT) ---"; \
		/tmp/dsa_out < $(INPUT); \
	else \
		/tmp/dsa_out; \
	fi

test:
	@if [ -z "$(P)" ]; then echo "Usage: make test P=topic/problem"; exit 1; fi
	$(CXX) $(CXXFLAGS) -o /tmp/dsa_out $(SRC)
	@if [ ! -f $(INPUT) ]; then echo "Missing $(INPUT)"; exit 1; fi
	@if [ ! -f $(OUTPUT) ]; then echo "Missing $(OUTPUT)"; exit 1; fi
	@/tmp/dsa_out < $(INPUT) > /tmp/dsa_actual
	@if diff -u $(OUTPUT) /tmp/dsa_actual > /tmp/dsa_diff 2>&1; then \
		echo "PASSED"; \
	else \
		echo "FAILED"; \
		cat /tmp/dsa_diff; \
		exit 1; \
	fi

debug:
	@if [ -z "$(P)" ]; then echo "Usage: make debug P=topic/problem"; exit 1; fi
	$(CXX) $(CXXFLAGS) -fsanitize=address,undefined -o /tmp/dsa_debug $(SRC)
	@if [ -f $(INPUT) ]; then \
		/tmp/dsa_debug < $(INPUT); \
	else \
		/tmp/dsa_debug; \
	fi

new:
	@if [ -z "$(P)" ]; then echo "Usage: make new P=topic/problem"; exit 1; fi
	@if [ -d $(P) ]; then echo "$(P) already exists"; exit 1; fi
	@mkdir -p $(P)
	@cp template.cpp $(SRC)
	@touch $(INPUT) $(OUTPUT)
	@echo "Created $(P)/"
	@echo "  sol.cpp  input.txt  output.txt"

.PHONY: run test debug new
