class Message
	Private theTxt
	Public Property Let TXT(S)
		theTxt = S
	End Property
	Public Sub Print()
		Wscript.echo theTxt
	End Sub
End Class

Dim M
set M = new Message 
M.TXT = "Hello world"
m.Print()
