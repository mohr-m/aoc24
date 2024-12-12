#/usr/bin/perl

use warnings;
use strict;
use Data::Dumper;

my $file = 'input.txt';
#my $file = 'testinput.txt';

open(my $fh, '<', $file);
my %rules;
my $sum = 0;
while (my $row = <$fh>) {
	chomp $row;
	if ($row =~ /(\d+)\|(\d+)/) {
		if (defined $rules{$1}) {
			$rules{$1} .= "|$2";
		} else {
			$rules{$1} = "$2";
		}
	} elsif ($row ne '') {
		my $correct = 1;
		while (my ($before, $after) = each %rules) {
			my $re= qr/($after).*$before/;
			if ($row =~ /${re}/) {
				$correct = 0;
				last;
			}
		}
		my @vals =  split(/,/, $row);
		if ($correct) {
			$sum += $vals[int(scalar(@vals)/2)] if $correct;
		}
	}
}
close($fh);

print "sum: $sum\n";
