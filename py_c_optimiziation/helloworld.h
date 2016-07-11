#ifndef MY_HEADER_H
# define MY_HEADER_H

#define max_number_characters 9
#define max_password_length 40

struct switchbuffer {
	char firstBuffer[max_number_characters];
	char secondBuffer[max_password_length];
	char* start;
	char* end;
	char* current;
	int brokenline;
};

struct listitem {
	uint count;
	char password[max_password_length];
	struct listitem* next;
}; 

typedef struct switchbuffer sbuffer;
typedef struct listitem item;


//put your function headers here
void errorHandler(int errNum);
int parseFile(FILE *fp);
FILE* getFile(int argc, const char * argv[]);
int writeBuffer(sbuffer* buffer, char c);

#endif