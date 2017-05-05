import PythonROUGE
guess_summary_list = ['CFS-Summaries/Guess_Summ_1.txt','CFS-Summaries/Guess_Summ_2.txt','CFS-Summaries/Guess_Summ_3.txt', 'CFS-Summaries/Guess_Summ_4.txt', 'CFS-Summaries/Guess_Summ_5.txt' ]
ref_summary_list = [['CFS-Summaries/Ref_Summ_1_1.txt','CFS-Summaries/Ref_Summ_1_2.txt'] , ['CFS-Summaries/Ref_Summ_2_1.txt','CFS-Summaries/Ref_Summ_2_2.txt'], ['CFS-Summaries/Ref_Summ_3_1.txt','CFS-Summaries/Ref_Summ_3_2.txt'], ['CFS-Summaries/Ref_Summ_4_1.txt','CFS-Summaries/Ref_Summ_4_2.txt'], ['CFS-Summaries/Ref_Summ_5_1.txt','CFS-Summaries/Ref_Summ_5_2.txt']]
recall,precision,F_measure = PythonROUGE.PythonROUGE(guess_summary_list,ref_summary_list,ngram_order=1) 
print "recall = " + str(recall)
print "precision = " + str(precision) 
print "F measure = " + str(F_measure)
