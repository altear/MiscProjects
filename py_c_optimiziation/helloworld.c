#include<stdio.h>
//has exit
#include <stdlib.h>
//header file
#include "helloworld.h"
#include <string.h>

/*
 * Arguments: FileName 
 */
int main(int argc, const char * argv[])
{	
	//prereqs
	FILE* f= getFile(argc, argv);
	parseFile(f);
	fclose(f);
	
	printf("DONE!");
	
	return 0;
}

void setFirstBuffer(sbuffer* buffer){
	buffer->start = buffer->firstBuffer;
	buffer->current = buffer->firstBuffer;
	buffer->end = buffer->firstBuffer + max_number_characters;
	
}

void setSecondBuffer(sbuffer* buffer){
	buffer->start = buffer->secondBuffer;
	buffer->current = buffer->secondBuffer;
	buffer->end = buffer->secondBuffer + max_password_length;
}

void resetBuffer(sbuffer* buffer){
	setFirstBuffer(buffer);
	*buffer->firstBuffer = '\0';
	*buffer->secondBuffer = '\0';
}

item* copyBuffer(sbuffer* buffer, item* line){
	
	char **endPtr;
	if (!buffer->brokenline && buffer->current != buffer->start) {
		writeBuffer(buffer, '\0');
		line->count=strtoumax(buffer->firstBuffer,endPtr,10);
		strcpy(line->password,buffer->secondBuffer);
		
		//count must have been valid for entry to be valid
		if (!line->count){
			line->next = malloc(sizeof(item));
			line = line->next;
		}
		
	}
	
}

int writeBuffer(sbuffer* buffer, char c){
	if (buffer->current <= buffer->end){
		if (c = ' ') {
			//clear leading spaces before number
			if (buffer->start == buffer->firstBuffer){
				if (buffer->current == buffer->firstBuffer) return 1;
				setSecondBuffer(buffer);
				return 1;
			}
		}
		
		*(buffer->current++)=c;
		return 1;
	}
	buffer->brokenline=1;
	return 0;
}

int parseFile(FILE *fp){
	char c;
	sbuffer* buffer = malloc(sizeof(sbuffer));
	resetBuffer(buffer);
	item *firstline = malloc(sizeof(item));
	item *line = firstline;
	
	int gah =0;
	for (c=getc(fp) ; c != EOF; c=getc(fp)) {
		//start of a new line, reset everything
		if (c == '\n'){
			gah++;
			copyBuffer(buffer, line);
			resetBuffer(buffer);
		}
		//this line is busted for some reason
		else if (buffer->brokenline) continue;
		else {
			writeBuffer(buffer, c);
		}
		
	}	
	
	
	printf("%i\n", gah);
	return 0;
}

/*
 * ##############
 * Handles Errors
 * ##############
 * 
 * 1: File argument not provided
 */
void errorHandler(int errNum){
	printf("Error %i: ", errNum);
	switch (errNum){
		case 1:
			printf("A file argument must be provided\n");
			
		case 2:
			printf("Line could not be turned into int");		
	}	
}

FILE* getFile(int argc, const char * argv[]){
	FILE* f;
	if (argc <2 || !(f=fopen(argv[1], "r"))) errorHandler(1);
	return f;
}