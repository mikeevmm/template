EXE ?= main.out
DBG ?= gdb

SRC_DIR = src
OBJ_DIR = obj
PYTHON_DIR = python
TEST_DIR = tests
EXAMPLE_DIR = examples

SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
TEST_SRC = $(wildcard $(TEST_DIR)/*.c)

CPPFLAGS += -Iinclude/.. 
CDBGFLAGS = -g -O0
CRLSFLAGS = -O3
CFLAGS += -Wall -Wextra -Wconversion -Wno-unused -pedantic -Wmissing-prototypes -Wstrict-prototypes
LDFLAGS += -Llib
LDLIBS += -lm

ifndef no_user
PYFLAGS = --user
endif

all: release

release:
	OPT="$(CRLSFLAGS)" make $(EXE)

$(EXE): $(OBJ)
	$(CC) $(LDFLAGS) $^ $(LDLIBS) -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CPPFLAGS) $(OPT) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJ)

fresh:
	make clean
	make all

run:
	./$(EXE)

debug:
	make clean
	OPT="$(CDBGFLAGS)" make $(EXE)
	$(DBG) -q ./$(EXE)

check:
	make all
	valgrind --leak-check=full ./$(EXE)

$(TEST_SRC): $(TEST_DIR)/%.c: $(filter-out $(OBJ_DIR)/main.o, $(OBJ))
	$(CC) $(CPPFLAGS) $(CDBGFLAGS) $(CFLAGS) $(OPT) -c $@ -o $(OBJ_DIR)/$*.o
	$(CC) $(LDFLAGS) $^ $(OBJ_DIR)/$*.o $(LDLIBS) -o $(TEST_DIR)/$*.out
	$(TEST_DIR)/$*.out

build: $(SRC_DIR)/*.c $(PYTHON_DIR)/*.c
	python3 buildext.py build --force
ifndef no_install
	python3 buildext.py install $(PYFLAGS) --force
endif

test:
	gdb -q -ex start --args python3 $(TEST_DIR)/test_ext.py

.PHONY: all clean $(TEST_SRC)
