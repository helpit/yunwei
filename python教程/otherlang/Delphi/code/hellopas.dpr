program hellopas;
{$APPTYPE CONSOLE}
uses windows;

type Message = class
	txt : string;
	constructor create(s:string);
	procedure print;
end;

constructor Message.Create(s:string);
begin
	txt := s
end;
procedure Message.print;
begin
	writeln(txt)
end;

var m : Message;

begin
	m := Message.Create('Hello world');
	m.print()
end.
