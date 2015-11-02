package Message;

# Message class constructor
sub new {
   my $class = shift;
   my $txt = shift;
   my $self = {};
   $self->{txt} = $txt;
   bless ($self, $class);
   return $self;
}

#Message->print() method
sub print{
   my $self = shift;
   if ($self->{txt} eq ""){
        print "No message";
   }else{
        for($i=0;$i<3;$i++){
                print $self->{txt},"\n";
        }
   }
   return $self
}

1;

