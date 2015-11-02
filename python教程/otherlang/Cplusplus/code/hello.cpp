#include <stdio.h>

class Message{
private:
   String txt;
public:
   Message(String s){ txt = s;};
   void Print(){ puts(txt);};
};

void main()
{ Message M("Hello world");
  M.Print();
}
