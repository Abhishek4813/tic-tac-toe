from tkinter import *
root=Tk()
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
state=[[0,0,0],
       [0,0,0],
       [0,0,0]]
player='x'
stop_game=False
def callback(i,j):
    global player
    if player=='x' and state[i][j]==0 and stop_game==False:
        b[i][j].configure(text='X')
        state[i][j]='x'
        player='O'
    if player=='O' and state[i][j]==0 and stop_game==False:
        b[i][j].configure(text='O')
        state[i][j]='O'
        player='x'
    check_for_winner()
def check_for_winner():
    global stop_game
    for i in range(3):
        if state[i][0]==state[i][1]==state[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True
    for i in range(3):
        if state[0][i]==state[1][i]==state[2][i]!=0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True
    if state[0][0]==state[1][1]==state[2][2]!=0:
        b[0][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][2].configure(bg='grey')
        stop_game = True
    if state[2][0]==state[1][1]==state[0][2]!=0:
        b[2][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[0][2].configure(bg='grey')
        stop_game = True
for p in range(3):
    for q in range(3):
        b[p][q]=Button(width=3,font=('vardana',56),bg='blue',fg='black',command=lambda i=p,j=q:callback(i,j))
        b[p][q].grid(row=p,column=q)
mainloop()
