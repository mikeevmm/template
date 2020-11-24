EXE?=main

SRC_DIR=src
OBJ_DIR=obj
DEPDIR=$(OBJ_DIR)/.deps

CC?=gcc
CXX?=g++
RM?=rm -r
DBG?=gdb
CFLAGS+=
CXXFLAGS+=-std=c++17
CPPFLAGS+=-g -Iinclude/..
LDFLAGS+=-g -Llib
LDLIBS+=
DEPFLAGS=-MT $@ -MMD -MP -MF $(DEPDIR)/$*.d

C_SRC=$(wildcard $(SRC_DIR)/*.c)
CC_SRC=$(wildcard $(SRC_DIR)/*.cc)
CPP_SRC=$(wildcard $(SRC_DIR)/*.cpp)
SRC=$(C_SRC) $(CC_SRC) $(CPP_SRC)

C_OBJ=$(C_SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.c.o)
CC_OBJ=$(CC_SRC:$(SRC_DIR)/%.cc=$(OBJ_DIR)/%.cc.o)
CPP_OBJ=$(CPP_SRC:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.cpp.o)
OBJ=$(C_OBJ) $(CC_OBJ) $(CPP_OBJ)

COMPILE.c=$(CC) $(DEPFLAGS) $(CFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c
COMPILE.cc=$(CXX) $(DEPFLAGS) $(CXXFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c

all: $(EXE)

$(EXE): $(OBJ)
	$(CXX) $(LDFLAGS) -o $(EXE) $(OBJ) $(LDLIBS)

$(OBJ_DIR)/%.c.o : $(SRC_DIR)/%.c $(DEPDIR)/%.c.d | $(DEPDIR)
	$(COMPILE.c) $< -o $@ 

$(OBJ_DIR)/%.cc.o : $(SRC_DIR)/%.cc $(DEPDIR)/%.cc.d | $(DEPDIR)
	$(COMPILE.cc) $< -o $@

($OBJ_DIR)/%.cpp.o : $(SRC_DIR)/%.cpp $(DEPDIR)/%.cpp.d | $(DEPDIR)
	$(COMPILE.cc) $< -o $@

$(DEPDIR): ; @mkdir -p $@

DEPFILES=$(C_SRC:$(SRC_DIR)/%.c=$(DEPDIR)/%.c.d) $(CC_SRC:$(SRC_DIR)/%.cc=$(DEPDIR)/%.cc.d) $(CPP_SRC:$(SRC_DIR)/%.cpp=$(DEPDIR)/%.cpp.d)
$(DEPFILES):

include $(wildcard $(DEPFILES))
