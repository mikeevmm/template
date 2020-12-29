EXE?=main

SRC_DIR=src
OBJ_DIR=obj
TEST_DIR=tests
DEPDIR=$(OBJ_DIR)/.deps

CC?=gcc
CXX?=g++
RM?=rm -r
DBG?=gdb
CFLAGS+=
CPPFLAGS+=-g -Iinclude/..
LDFLAGS+=-g -Llib
LDLIBS+=
DEPFLAGS=-MT $@ -MMD -MP -MF $(DEPDIR)/$*.d

C_SRC=$(wildcard $(SRC_DIR)/*.c)
SRC=$(C_SRC)

C_OBJ=$(C_SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.c.o)
OBJ=$(C_OBJ)

COMPILE.c=$(CC) $(DEPFLAGS) $(CFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c

all: $(EXE)

$(EXE): $(OBJ)
	$(CC) $(LDFLAGS) -o $(EXE) $(OBJ) $(LDLIBS)

$(OBJ_DIR)/%.c.o : $(SRC_DIR)/%.c $(DEPDIR)/%.c.d | $(DEPDIR)
	$(COMPILE.c) $< -o $@ 

$(DEPDIR): ; @mkdir -p $@

DEPFILES=$(C_SRC:$(SRC_DIR)/%.c=$(DEPDIR)/%.c.d)
$(DEPFILES):

include $(wildcard $(DEPFILES))

TEST_SRC=$(wildcard $(TEST_DIR)/*.c)
TEST_OBJ=$(TEST_SRC:$(TEST_DIR)/%.c=$(TEST_DIR)/.obj/%.c.o)
TESTS=$(TEST_SRC:$(TEST_DIR)/%.c=$(TEST_DIR)/.compiled/%)

check: $(TESTS)

$(TEST_DIR)/.compiled/% : $(TEST_DIR)/.obj/%.c.o $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $< $(filter-out obj/main.c.o, $(OBJ)) $(LDLIBS)
	if valgrind $@; then echo "\e[32m$* passed\e[0m"; else echo "\e[31m$* failed\e[0m"; fi
	$(RM) $@

$(TEST_DIR)/.obj/%.c.o : $(TEST_DIR)/%.c
	$(COMPILE.c) $< -o $@

.PHONY: check
