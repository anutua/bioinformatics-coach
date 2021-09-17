 # -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:04:06 2021

@author: Anutua
"""
from Bio import SeqIO

"""random dna sequence """
dna1="AAACTTG"
dna2="ggactag"
 
sample="AGTTAGCTAGGAG"
a_count=sample.count("A")
g_count=sample.count("G")
t_count=sample.count("T")
c_count=sample.count("C")

samplelength=len(sample)
gc=(g_count+c_count)
ag=a_count+g_count
ct=c_count+t_count
gc_percent=(gc/samplelength) *100
purine_percent=(ag/samplelength) *100 
#Answers' variables
number1=samplelength
number2=round(gc_percent,2)
number3=ag
number4=ct
number5=round(purine_percent,2)

#####Read single sequence fasta data
sequence_directory="D:/Anutua/Documents/waccbip/sequence.fasta"
seq_object=SeqIO.read(sequence_directory,"fasta")