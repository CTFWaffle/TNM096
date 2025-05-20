#TASK B
fair = 0.9
nofair = 1-fair
smart = 1
nosmart = 1-smart
study = 0.0
nostudy = 1-study

prep =  0.5*smart*nostudy 
noprep = 1-prep

print('Probability to be prepared:', prep)

pass_test = 0.9*smart*prep*fair + 0.1*smart*prep*nofair + 0.7*smart*noprep*fair + 0.1*smart*noprep*nofair
nopass = 1-pass_test

print('Probability to pass the exam:', pass_test)