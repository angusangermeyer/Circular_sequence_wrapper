test_sequence = "IONCEWENTTOTHEMARKETTOPURCHASEEGGSBUTTHEYONLYHADFISH"


def genome_wrapper(nuc_sequence, hit_strt_loc, hit_stop_loc, flank_length):
	"""
	Provide the nucleotide sequence (as either string or list).
	This function is designed to use to parse BLAST results, so seq locations are called "hits".
	The start and stop locations of a hit region ('left' must be smaller so consider hit orientation).
	The length you want for each flank ('5000' will return 5000bp on each side of the hit).
	"""

	left_flank_edge = hit_strt_loc - flank_length #Find the furthest left edge of the full region
	rght_flank_edge = hit_stop_loc + flank_length #Find the furthest right edge of the full region
	
	if left_flank_edge < 0:
		#Concatenate sequences splits if flank wraps around left edge of linear genome
		left_flank = nuc_sequence[left_flank_edge:] + nuc_sequence[:hit_strt_loc]
	elif left_flank_edge >= 0:
		left_flank = nuc_sequence[left_flank_edge:hit_strt_loc]


	if rght_flank_edge > len(nuc_sequence):
		#Concatenate sequences splits if flank wraps around right edge of linear genome
		right_flank = nuc_sequence[hit_stop_loc:] + nuc_sequence[:rght_flank_edge-len(nuc_sequence)]
	elif rght_flank_edge <= len(nuc_sequence):
		right_flank = nuc_sequence[hit_stop_loc:rght_flank_edge]
	
	
	combined_sequence = left_flank + nuc_sequence[hit_strt_loc:hit_stop_loc] + right_flank
		
	return(combined_sequence)
		


print(genome_wrapper(test_sequence, 10, 15, 5))