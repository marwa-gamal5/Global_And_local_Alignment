# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
#
# def input(request):
#     data=request.POST.get('name')
#     print(data)
#     return render(request,'global.html',{'data':data})
# def load(request):
#     return render(request,'loading.html')
# def output(request):
#     return render(request,'index.html')
# def home(request):
#     return render(request,'home.html')
# def input_local(request):
#     return render(request,'local.html')
# def output_local(request):
#     return render(request,'local_align.htm')

from django.shortcuts import render
# from  django.urls import path, include
from django.http import HttpResponse ,HttpResponseRedirect


import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns

# Create your views here.

def input(request):
    print("m")
    if(request.method=='GET'):
        return render(request,'global.html')
    else:
        seq1=request.POST.get['seq1']
        seq2=request.POST.get['seq2']
        Match_score=request.POST.get['match_score']
        mismatch_score=request.POST.get['mismatch_score']
        gap_score=request.POST.get['gap_score']
    return render(request,'global.html')
def load(request):
    return render(request,'loading.html')
def output(request):
    def needleman_wunsch(seq1, seq2, Match_score, mismatch_score, gap_score):
        n = len(seq1)
        m = len(seq2)

        global score
        score = np.zeros((m+1, n+1))

        def match_score(alpha, beta):
            if alpha == beta:
                return Match_score
            else:
                return mismatch_score

            for i in range(0, m + 1):
                score[i][0] = gap_penalty * i

            for j in range(0, n + 1):
                score[0][j] = gap_score * j

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    diag = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
                    delete = score[i - 1][j] + gap_score
                    insert = score[i][j - 1] + gap_score
                    score[i][j] = max(diag, delete, insert)


            align1 = ""
            align2 = ""
            i = m
            j = n

            while i > 0 and j > 0:  # end touching the top or the left edge
                score_current = score[i][j]
                score_diagonal = score[i-1][j-1]
                score_up = score[i][j-1]
                score_left = score[i-1][j]

                if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
                    align1 += seq1[j-1]
                    align2 += seq2[i-1]
                    i -= 1
                    j -= 1
                elif score_current == score_up + gap_score:
                    align1 += seq1[j-1]
                    align2 += '-'
                    j -= 1
                elif score_current == score_left + gap_score:
                    align1 += '-'
                    align2 += seq2[i-1]
                    i -= 1

            while j > 0:
                align1 += seq1[j-1]
                align2 += '-'
                j -= 1
            while i > 0:
                align1 += '-'
                align2 += seq2[i-1]
                i -= 1
            align1 = align1[::-1]
            align2 = align2[::-1]
            s=int(score[m, n])
            return HttpResponse(align1, align2,s)
        a1,a2,sco=needleman_wunsch(seq1,seq2,Match_score,mismatch_score,gap_score)
        content={"a1":a1,"a2":a2,"sco":sco}
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def input_local(request):
    return render(request,'local.html')

def output_local(request):
    return render(request,'local_align.html')

def home(request):
    return render(request,'home.html')